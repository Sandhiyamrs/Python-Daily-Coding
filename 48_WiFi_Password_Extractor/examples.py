from file1_wifi_password_extractor import get_saved_wifi_passwords

networks = get_saved_wifi_passwords()

for ssid, password in networks.items():
    print(f"SSID: {ssid} | Password: {password}")
