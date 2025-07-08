import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from core.utils import print_success, print_warning, print_error, save_results

PAYLOADS = [
    "https://evil.com",
    "//evil.com",
    "/evil",
    "http://127.0.0.1",
    "http://localhost",
    "http://google.com@evil.com"
]

def run_open_redirect_scan(url):
    print(f"\n🧭 Testing open redirect on: {url}")

    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    if not query:
        print_error("URL has no query parameters to test.")
        return

    base_params = {k: v[0] for k, v in query.items()}

    for param in base_params:
        for payload in PAYLOADS:
            test_params = base_params.copy()
            test_params[param] = payload

            test_query = urlencode(test_params)
            test_url = urlunparse(parsed._replace(query=test_query))

            try:
                response = requests.get(test_url, allow_redirects=False, timeout=5)
                location = response.headers.get('Location', '')

                if response.status_code in [301, 302, 303, 307, 308] and any(p in location for p in ["evil.com", "127.0.0.1", "localhost"]):
                    print_success(f"[Open Redirect] {param} may be vulnerable → {test_url}")
                    print(f" → Redirects to: {location}")
                    save_results("output/open_redirects.txt", test_url)
            except requests.RequestException as e:
                print_warning(f"[!] Request failed: {e}")
