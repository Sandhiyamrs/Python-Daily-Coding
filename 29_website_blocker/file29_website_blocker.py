import time
from datetime import datetime

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
blocked_websites = ["www.facebook.com", "www.youtube.com"]
redirect = "127.0.0.1"

start_hour = 9
end_hour = 17

while True:
    now = datetime.now()
    if start_hour <= now.hour < end_hour:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in blocked_websites:
                if website not in content:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()
    time.sleep(30)
