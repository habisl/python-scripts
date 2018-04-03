import time
from datetime import datetime as dt

temp_hosts = "hosts"
redirect = "127.0.0.1" # In order to redirect to the local DNS when u want to visit those website
website_list = ["www.facebook.com", "facebook.com"]

while True:
    # It calculates the time between 8-16 in current day
    if dt(dt.now().year, dt.now().month, dt.now().day, 18) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 0):
        print("This is work hours")
        with open(temp_hosts, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:  # To check if website is in the hosts file
                    pass
                else:
                    # It will add the sites even its not in the hosts file.
                    file.write("\n" + redirect + " " + website + "\n")
    else:
        with open(temp_hosts, 'r+') as file:
            content = file.readlines()  # Reads all the lines in the hosts file
            """
            To check agains other lines in the file 
            if any items that listed in website_list  
            """
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() # to remove repeated lines in the file to overcome 'for' loop iteration
        print("This is fun hour")

    time.sleep(5)

