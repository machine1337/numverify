import base64
import re
import platform
import os

print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install requests -q -q -q")
        import requests
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

elif platform.system().startswith("Windows"):
    try:
        import requests
    except ImportError:
        os.system("python -m pip install requests -q -q -q")
        import requests
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *

colorama.deinit()
banner = Center.XCenter(r"""********************************************************************
*        ___   _              __     __   _____ _  __     __        *
*       / / \ | |_   _ _ __ __\ \   / /__|___ /(_)/ _|_   \ \       *
*      | ||  \| | | | | '_ ` _ \ \ / / _ \ |_ \| | |_| | | | |      *
*     < < | |\  | |_| | | | | | \ V /  __/___) | |  _| |_| |> >     *
*      | ||_| \_|\__,_|_| |_| |_|\_/ \___|____/|_|_|  \__, | |      *
*       \_\                                           |___/_/       *
*                                                                   *
*           OSINT TOOL TO FIND MOBILE INFO, LOCATION AND VALIDITY   *
*                                                                   *
*                    Coded By: Machine1337                          *
*********************************************************************
          Note: Enter Number with country code but without +
                          (9123456789098)
""")
def is_valid_mobile_number(mobile_number):
    pattern = re.compile(r"(?:(?:\+|00)91)?[6-9]\d{9}")
    return pattern.match(mobile_number) is not None

def check_number():
    try:
        os_name = "cls" if platform.system() == "Windows" else "clear" if platform.system() == "Linux" else "Unknown"
        os.system(os_name)
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        mobile_number = input(Fore.GREEN + '\n[+] Enter Mobile Number: ')
        if is_valid_mobile_number(mobile_number):
            message = base64.b64decode(
                'aHR0cHM6Ly9hcGkuYXBpbGF5ZXIuY29tL251bWJlcl92ZXJpZmljYXRpb24vdmFsaWRhdGU/bnVtYmVyPQ=='.encode(
                    'ascii')).decode('ascii')
            url = f"{message}{mobile_number}"
            hello = base64.b64decode('dGdDckRFOVF0QVF4Q1lvNnk4dHprMUdtQTJKbzBYZmI='.encode('ascii')).decode('ascii')
            payload = {}
            headers = {
                "apikey": f"{hello}"
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            if status_code == 200:
                response_json = response.json()
                country_code = response_json["country_code"]
                number = response_json["number"]
                country_name = response_json["country_name"]
                country_prefix = response_json["country_prefix"]
                international_format = response_json["international_format"]
                line_type = response_json["line_type"]
                local_format = response_json["local_format"]
                valid = response_json["valid"]
                location = response_json["location"]
                print(
                    f"Country code: {country_code}\nNumber: {number}\nCountry name: {country_name}\nCountry prefix: {country_prefix}\nInternational format: {international_format}\nLine type: {line_type}\nLocal format: {local_format}\nLocation: {location}\nValid: {valid}")
            else:
                print(Fore.RED + f"Error: {status_code}")
        else:
            print(Fore.RED + '[*] Invalid Mobile Number....')
    except KeyboardInterrupt:
        print(Fore.RED+'\n[*] You Pressed The Wrong Button....')
check_number()
#coded by: machine1337
