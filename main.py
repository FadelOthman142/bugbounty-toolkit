import asyncio
import sys
import time
from colorama import init, Fore, Style
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

from core.subdomain import run_subdomain_enum
from core.payloadtester import run_payload_test
from core.headerscan import run_header_scan
from core.open_redirect import run_open_redirect_scan
from core.reflection_tester import run_reflection_test
from core.http_methods import run_http_method_scan
from core.dirbrute import run_dir_brute


init(autoreset=True)


console = Console()

def pew_shooting_star_animation(width=40):
    
    print(Fore.LIGHTRED_EX + "Pew!" + Style.RESET_ALL, end=' ', flush=True)
    time.sleep(0.5)
    
    square = "[■]"  
    
    for pos in range(width):
      
        print('\r' + ' ' * (width + len(square) + 10), end='')
        
       
        line = ' ' * pos + Fore.YELLOW + '*' + Style.RESET_ALL
        line += ' ' * (width - pos) + Fore.MAGENTA + square + Style.RESET_ALL
        
        print('\r' + line, end='', flush=True)
        time.sleep(0.05)
    
    
    time.sleep(0.5)
    print('\r' + ' ' * (width + len(square) + 10), end='')  
    print() 

def print_banner():
    banner_text = Text()
    banner_text.append("🔫  BUG BOUNTY TOOLKIT 🔫\n", style="bold cyan")
    banner_text.append("Reconnaissance & Exploitation Assistant\n", style="bold yellow")
    banner_text.append("Created by Fadel Othman", style="bold magenta")

    console.print(Panel(banner_text, title="[bold green]🚀 Welcome[/bold green]", subtitle="v1.0", style="red", box=box.DOUBLE))

def loading_animation(message="Loading menu", duration=2):
    for i in range(duration * 4):
        dots = "." * (i % 4)
        print(f"\r{Fore.CYAN}{message}{dots}{Style.RESET_ALL}", end='')
        time.sleep(0.25)
    print()

def show_menu_with_animation():
    options = [
        (Fore.CYAN, "1. Subdomain Enumeration"),
        (Fore.BLUE, "2. Directory Brute Force"),
        (Fore.RED, "3. XSS/SQLi Payload Tester"),
        (Fore.YELLOW, "4. Security Header Scanner"),
        (Fore.MAGENTA, "5. Open Redirect Scanner"),
        (Fore.LIGHTRED_EX, "6. Reflection Tester"),
        (Fore.LIGHTBLUE_EX, "7. HTTP Method Scanner"),
        (Fore.GREEN, "0. Exit")
    ]

    print(f"\n{Fore.GREEN}📡 Bug Bounty Toolkit - Recon & Exploit CLI{Style.RESET_ALL}\n")
    for color, text in options:
        print(color + text + Style.RESET_ALL)
        time.sleep(0.3)  

def main():
    pew_shooting_star_animation()
    print_banner()
    loading_animation("Launching Bug Bounty Toolkit")

    while True:
        show_menu_with_animation()

        choice = input(f"\n{Fore.LIGHTWHITE_EX}Choose an option: {Style.RESET_ALL}").strip()

        if choice == '1':
            target = input("Enter target domain: ")
            run_subdomain_enum(target)

        elif choice == '2':
            url = input("Enter target URL (include http:// or https://): ")
            asyncio.run(run_dir_brute(url))

        elif choice == '3':
            run_payload_test()

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
