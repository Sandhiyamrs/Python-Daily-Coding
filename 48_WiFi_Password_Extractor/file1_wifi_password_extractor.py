import subprocess
import platform
import re

def get_wifi_profiles():
    """Get list of saved WiFi profiles."""
    if platform.system() != 'Windows':
        print("This script only works on Windows!")
        return []
    
    try:
        # Get list of profiles
        profiles_data = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles'],
            stderr=subprocess.STDOUT
        ).decode('utf-8', errors='ignore')
        
        # Extract profile names
        profile_names = re.findall(r'All User Profile\s+:\s+(.+)', profiles_data)
        
        return [name.strip() for name in profile_names]
    
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve WiFi profiles. Run as administrator!")
        return []

def get_wifi_password(profile_name):
    """Get password for a specific WiFi profile."""
    try:
        profile_info = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'],
            stderr=subprocess.STDOUT
        ).decode('utf-8', errors='ignore')
        
        # Extract password
        password_match = re.search(r'Key Content\s+:\s+(.+)', profile_info)
        
        if password_match:
            return password_match.group(1).strip()
        else:
            return None
    
    except subprocess.CalledProcessError:
        return None

def main():
    print("=== WiFi Password Extractor ===\n")
    
    if platform.system() != 'Windows':
        print("Error: This script only works on Windows!")
        return
    
    print("Retrieving WiFi profiles...\n")
    
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("No WiFi profiles found or insufficient permissions!")
        return
    
    wifi_data = []
    
    print(f"Found {len(profiles)} WiFi profile(s):\n")
    
    for profile in profiles:
        password = get_wifi_password(profile)
        
        if password:
            print(f"Profile: {profile}")
            print(f"Password: {password}\n")
            wifi_data.append(f"Profile: {profile}\nPassword: {password}\n")
        else:
            print(f"Profile: {profile}")
            print(f"Password: [No password or open network]\n")
            wifi_data.append(f"Profile: {profile}\nPassword: [No password]\n")
    
    # Option to save to file
    save = input("Save to file? (y/n): ").lower()
    
    if save == 'y':
        filename = "wifi_passwords.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=== Saved WiFi Passwords ===\n\n")
            f.writelines(wifi_data)
        
        print(f"\n✓ Saved to {filename}")

if __name__ == "__main__":
    main()
