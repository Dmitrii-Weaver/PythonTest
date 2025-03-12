# Write a Python program that performs concurrent HTTP requests using threads.

import requests
import threading


def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")


urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org"
]
threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
