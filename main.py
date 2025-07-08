import asyncio
import sys
import time
from colorama import init, Fore, Style

from core.subdomain import run_subdomain_enum
from core.payloadtester import run_payload_test
from core.headerscan import run_header_scan
from core.open_redirect import run_open_redirect_scan
from core.reflection_tester import run_reflection_test
from core.http_methods import run_http_method_scan
from core.dirbrute import run_dir_brute  # async

init(autoreset=True)

def shooting_stars_animation(duration=3, width=50):
    start_time = time.time()
    while time.time() - start_time < duration:
        for pos in range(width):
            print('\r' + ' ' * width, end='')
            line = ' ' * pos + Fore.YELLOW + '*' + Style.RESET_ALL
            print('\r' + line, end='')
            time.sleep(0.03)
            if time.time() - start_time >= duration:
                break
    print('\r' + ' ' * width, end='')  # Clear line after animation

def type_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # newline

def print_banner():
    lines = [
        f"{Fore.YELLOW}*  {Fore.RED}+-------------------------------------------------+  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}|                                                 |  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}|    🔫          {Fore.CYAN}BUG BOUNTY TOOLKIT{Fore.RED}               🔫   |  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}|                                                 |  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}|       {Fore.YELLOW}Reconnaissance & Exploitation Assistant{Fore.RED}        |  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}|                                                 |  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}|           {Fore.MAGENTA}Created by Fadel Othman{Fore.RED}           |  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}|                                                 |  {Fore.YELLOW}*",
        f"{Fore.YELLOW}*  {Fore.RED}+-------------------------------------------------+  {Fore.YELLOW}*"
    ]
    for line in lines:
        type_print(line, delay=0.01)
    print()  # extra newline

def main():
    shooting_stars_animation()
    print_banner()

    while True:
        print(f"{Fore.GREEN}📡 Bug Bounty Toolkit - Recon & Exploit CLI{Style.RESET_ALL}\n")
        print("1. Subdomain Enumeration")
        print("2. Directory Brute Force")
        print("3. XSS/SQLi Payload Tester")
        print("4. Security Header Scanner")
        print("5. Open Redirect Scanner")
        print("6. Reflection Tester")
        print("7. HTTP Method Scanner")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == '1':
            target = input("Enter target domain: ")
            run_subdomain_enum(target)

        elif choice == '2':
            url = input("Enter target URL (include http:// or https://): ")
            asyncio.run(run_dir_brute(url))

        elif choice == '3':
            run_payload_test()  # handles its own input

        elif choice == '4':
            url = input("Enter target URL: ")
            run_header_scan(url)

        elif choice == '5':
            url = input("Enter target URL with query string (e.g. ?url=...): ").strip()
            run_open_redirect_scan(url)

        elif choice == '6':
            url = input("Enter target URL with query string: ").strip()
            param = input("Optional: enter parameter name to test (press Enter to test all): ").strip() or None
            run_reflection_test(url, param)

        elif choice == '7':
            url = input("Enter target URL (include http:// or https://): ").strip()
            run_http_method_scan(url)

        elif choice == '0':
            print(f"{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
