import asyncio
import aiohttp
import random
import os
from core.utils import print_success, print_warning, print_error, save_results

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
]

REFERERS = [
    "https://google.com",
    "https://bing.com",
    "https://duckduckgo.com",
    "https://yahoo.com",
]

XFF_HEADERS = [
    "127.0.0.1",
    "192.168.1.1",
    "10.0.0.1",
    "8.8.8.8",
]

CONCURRENT_REQUESTS = 20

async def fetch(session, url):
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": random.choice(REFERERS),
        "X-Forwarded-For": random.choice(XFF_HEADERS),
    }

    try:
        async with session.get(url, headers=headers, timeout=10, allow_redirects=False) as response:
            status = response.status
            location = response.headers.get('Location', '')
            return url, status, location

    except asyncio.TimeoutError:
        return url, None, None
    except Exception as e:
        return url, f"Error: {e}", None

async def bound_fetch(sem, session, url):
    async with sem:
        await asyncio.sleep(random.uniform(0.05, 0.2))  # slight random delay
        return await fetch(session, url)

async def run_dir_brute(base_url):
    print(f"\n🚀 Starting async directory brute force on: {base_url}")

    if not base_url.endswith('/'):
        base_url += '/'

    wordlist_path = os.path.join('wordlists', 'common.txt')

    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            paths = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print_error(f"Wordlist not found at {wordlist_path}")
        return

    sem = asyncio.Semaphore(CONCURRENT_REQUESTS)

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(bound_fetch(sem, session, base_url + path)) for path in paths]

        for future in asyncio.as_completed(tasks):
            url, status, location = await future

            if isinstance(status, int):
                if status == 200:
                    print_success(f"[200] Found: {url}")
                    save_results("output/dirbrute_200.txt", url)
                elif status == 403:
                    print_warning(f"[403] Forbidden: {url}")
                    save_results("output/dirbrute_403.txt", url)
                elif status in (301, 302):
                    print(f"[{status}] Redirect: {url} -> {location}")
                    save_results("output/dirbrute_redirects.txt", f"{url} -> {location}")
                else:
                    print(f"[{status}] {url}")
            else:
                print_error(f"[!] Request error for {url}: {status}")
