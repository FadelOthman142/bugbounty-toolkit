import requests
from core.utils import print_success, print_warning, print_error, save_results

DANGEROUS_METHODS = ['OPTIONS', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH']

def run_http_method_scan(url):
    print(f"\n🔎 Scanning HTTP methods on: {url}")

    try:
        response = requests.options(url, timeout=10)
        allowed_methods = response.headers.get('Allow', '')

        if not allowed_methods:
            print_warning("[!] 'Allow' header not found in response.")
            return

        allowed = [method.strip() for method in allowed_methods.split(',')]
        print(f"Allowed methods: {allowed_methods}")

        vulnerable = [m for m in DANGEROUS_METHODS if m in allowed]

        if vulnerable:
            print_error(f"[!] Dangerous HTTP methods enabled: {', '.join(vulnerable)}")
            save_results("output/http_methods.txt", f"{url} allows {', '.join(vulnerable)}")
        else:
            print_success("[+] No dangerous HTTP methods detected.")

    except requests.RequestException as e:
        print_error(f"[!] Request error: {e}")
