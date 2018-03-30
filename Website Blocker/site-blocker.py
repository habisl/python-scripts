import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # One reason to put 'r' is to separate the directory \\.\\ can be used instead.
redirect = "127.0.0.1" # In order to redirect to local DNS when u want to visit those website
website_list = ["www.facebook.com", "facebook.com"]

while True:
    # It calculates the time between 8-16 in current day
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
   
