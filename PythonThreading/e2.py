# Write a Python program to download multiple files concurrently using threads.

import threading
import urllib.request


def download_file(url, filename):
    print(f"\nDownloading {filename} from {url}...")
    urllib.request.urlretrieve(url, filename)
    print(f"\n{filename} downloaded successfully.")


files_to_download = [
    {"url": "https://en.wikipedia.org/wiki/British_logistics_in_the_Normandy_campaign",
        "filename": "i:\wfile1"},
    {"url": "https://en.wikipedia.org/wiki/Graph_(abstract_data_type)",
     "filename": "i:\Graph_abstract_data_type"},
    {"url": "https://example.com/", "filename": "i:\example"}
]

threads = []

for file_info in files_to_download:
    thread = threading.Thread(
        target=download_file,
        args=(file_info["url"], file_info["filename"])
    )
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
