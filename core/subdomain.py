import requests
from core.utils import print_success, print_error, save_results

def run_subdomain_enum(domain):
    print(f"\n🔍 Enumerating subdomains for: {domain}")

    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print_error(f"[!] Error fetching data from crt.sh (Status {response.status_code})")
            return

        data = response.json()
        subdomains = set(entry['name_value'] for entry in data)

        if not subdomains:
            print_error("[-] No subdomains found.")
            return

        print_success(f"[+] Found {len(subdomains)} unique subdomains:\n")

        for sub in sorted(subdomains):
            print(f" - {sub}")
            save_results(f"output/subdomains_{domain}.txt", sub)

    except Exception as e:
        print_error(f"[!] Exception: {e}")
