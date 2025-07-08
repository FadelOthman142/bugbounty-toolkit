import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy",
]

def run_header_scan(url):
    print(f"\n🔐 Scanning security headers for: {url}")

    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        print("\nSecurity Headers Check:")

        for header in SECURITY_HEADERS:
            if header in headers:
                print(f"✅ {header}: {headers[header]}")
            else:
                print(f"❌ {header} header is missing!")

    except requests.RequestException as e:
        print(f"[!] Request error: {e}")
