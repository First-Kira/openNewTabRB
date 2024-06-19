import webbrowser
import time

def open_url_in_browser(url):
    webbrowser.open_new_tab(url)

def open_urls_in_new_tabs_with_delay(urls, delay):
    for url in urls:
        open_url_in_browser(url)
        time.sleep(delay)

# List of URLs to open in new tabs
urls = ["https://www.hackthebox.com", "https://www.github.com", "https://www.tryhackme.com"]

# Delay in seconds
delay = 30

open_urls_in_new_tabs_with_delay(urls, delay)

