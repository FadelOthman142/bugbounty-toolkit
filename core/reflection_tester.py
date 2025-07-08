import requests
from core.utils import print_success, print_warning, print_error, save_results

def run_reflection_test(url, param_name=None):
    """
    Send a request with a unique payload and check if it is reflected in the response body.

    If param_name is None, tries to detect query params from URL automatically.
    """

    print(f"\n🔍 Running Reflection Test on: {url}")

    unique_payload = "refleCtTesT12345"  # Unique string to look for

    try:
        from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

        parsed = urlparse(url)
        query = parse_qs(parsed.query)

        if not query:
            print_error("[!] No query parameters found in URL.")
            return

        # Prepare params with unique payload
        params = {k: unique_payload if (param_name is None or k == param_name) else v[0] for k, v in query.items()}

        new_query = urlencode(params)
        test_url = urlunparse(parsed._replace(query=new_query))

        response = requests.get(test_url, timeout=10)
        body = response.text

        if unique_payload in body:
            print_success(f"[+] Parameter '{param_name or 'all'}' reflected in response!")
            print(f"Test URL: {test_url}")
            save_results("output/reflection_results.txt", test_url)
        else:
            print_warning("[!] Payload NOT reflected in response.")

    except Exception as e:
        print_error(f"[!] Exception during test: {e}")
