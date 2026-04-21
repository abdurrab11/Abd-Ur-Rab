#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    ﷽
    بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
    
    ████████╗ ██████╗  ██████╗ ██╗     ███████╗    ████████╗██╗  ██╗███████╗
    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    ╚══██╔══╝██║  ██║██╔════╝
       ██║   ██║   ██║██║   ██║██║     ███████╗       ██║   ███████║█████╗  
       ██║   ██║   ██║██║   ██║██║     ╚════██║       ██║   ██╔══██║██╔══╝  
       ██║   ╚██████╔╝╚██████╔╝███████╗███████║       ██║   ██║  ██║███████╗
       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝
    
    A.R.T.H - Abd Ur Rab's Technological Hub
    The Greatest A1 First-Class Supreme Toolkit
    Version: 3.0 Divine Edition
    Author: Abd Ur Rab
"""

import os
import sys
import time
import socket
import platform
import subprocess
import threading
import json
import re
import math
from datetime import datetime
from collections import deque
import requests

# ═══════════════════════════════════════════════════════════════════
# DIVINE COLOR PALETTE - 256 Color Support for Termux
# ═══════════════════════════════════════════════════════════════════
class DivineColors:
    # Standard
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Extended 256 Colors
    ORANGE = '\033[38;5;208m'
    GOLD = '\033[38;5;220m'
    PINK = '\033[38;5;213m'
    LIME = '\033[38;5;154m'
    TEAL = '\033[38;5;51m'
    PURPLE = '\033[38;5;141m'
    CRIMSON = '\033[38;5;161m'
    EMERALD = '\033[38;5;46m'
    SKY = '\033[38;5;117m'
    SUNSET = '\033[38;5;203m'
    
    # Backgrounds
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_GOLD = '\033[48;5;220m'
    BG_PURPLE = '\033[48;5;141m'
    
    # Effects
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    STRIKE = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    
    # Reset
    END = '\033[0m'
    
    @staticmethod
    def gradient(text, start_color=51, end_color=213):
        """Apply 256-color gradient to text"""
        result = ""
        length = len(text)
        for i, char in enumerate(text):
            if char == ' ':
                result += char
                continue
            color = int(start_color + (end_color - start_color) * (i / length))
            result += f"\033[38;5;{color}m{char}"
        return result + '\033[0m'
    
    @staticmethod
    def rainbow(text):
        """Rainbow effect using 256 colors"""
        colors = [196, 208, 220, 154, 46, 51, 45, 27, 93, 201, 198]
        result = ""
        for i, char in enumerate(text):
            if char == ' ':
                result += char
                continue
            result += f"\033[38;5;{colors[i % len(colors)]}m{char}"
        return result + '\033[0m'

# ═══════════════════════════════════════════════════════════════════
# DIVINE TOOLKIT CLASS
# ═══════════════════════════════════════════════════════════════════
class ARTHDivineToolkit:
    def __init__(self):
        self.C = DivineColors()
        self.author = "Abd Ur Rab"
        self.version = "3.0 Divine Edition"
        self.running = True
        self.data_history = deque(maxlen=100)
        self.animation_chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        self.current_frame = 0
        
    def clear(self):
        os.system('clear' if os.name != 'nt' else 'cls')
        
    def get_terminal_width(self):
        try:
            return os.get_terminal_size().columns
        except:
            return 80
            
    def center_text(self, text, width=None, fill=' '):
        if width is None:
            width = self.get_terminal_width()
        return text.center(width, fill)
        
    def print_line(self, char="═", color=None):
        color = color or self.C.GOLD
        width = self.get_terminal_width()
        print(f"{color}{char * width}{self.C.END}")
        
    def animate_loading(self, text="Loading"):
        chars = "◐◓◑◒"
        for i in range(20):
            sys.stdout.write(f"\r{self.C.GOLD}{chars[i % 4]}{self.C.END} {self.C.CYAN}{text}...{self.C.END}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        
    # ═══════════════════════════════════════════════════════════════
    # DIVINE BISMILLAH & BANNER
    # ═══════════════════════════════════════════════════════════════
    def divine_bismillah(self):
        bismillah = """
        ﷽
        
        بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
        
        In the name of Allah, the Most Gracious, the Most Merciful
        """
        print(f"{self.C.GOLD}{self.C.BOLD}{self.C.ITALIC}{bismillah}{self.C.END}")
        
    def supreme_banner(self):
        self.clear()
        width = self.get_terminal_width()
        
        # Top sacred border
        print(f"{self.C.GOLD}{self.C.BOLD}╔{'═' * (width-2)}╗{self.C.END}")
        
        # Bismillah header
        bismillah_line = "  ﷽  بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ  ﷽  "
        padding = (width - len("  ﷽  بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ  ﷽  ")) // 2
        print(f"{self.C.GOLD}║{' ' * padding}{self.C.CYAN}{self.C.BOLD}{bismillah_line}{self.C.END}{self.C.GOLD}{' ' * (width - padding - len(bismillah_line) - 2)}║{self.C.END}")
        
        print(f"{self.C.GOLD}{self.C.BOLD}╠{'═' * (width-2)}╣{self.C.END}")
        
        # ASCII Art with gradient
        art_lines = [
            "    ████████╗ ██████╗  ██████╗ ██╗     ███████╗    ████████╗██╗  ██╗███████╗",
            "    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    ╚══██╔══╝██║  ██║██╔════╝",
            "       ██║   ██║   ██║██║   ██║██║     ███████╗       ██║   ███████║█████╗  ",
            "       ██║   ██║   ██║██║   ██║██║     ╚════██║       ██║   ██╔══██║██╔══╝  ",
            "       ██║   ╚██████╔╝╚██████╔╝███████╗███████║       ██║   ██║  ██║███████╗",
            "       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝"
        ]
        
        for line in art_lines:
            colored_line = self.C.gradient(line, 220, 51)
            padding = (width - 80) // 2
            print(f"{self.C.GOLD}║{' ' * max(0, padding)}{colored_line}{self.C.GOLD}{' ' * max(0, width - padding - 80 - 2)}║{self.C.END}")
            
        # Title
        title = "  A.R.T.H - ABD UR RAB'S TECHNOLOGICAL HUB  "
        subtitle = "  THE GREATEST A1 FIRST-CLASS SUPREME TOOLKIT  "
        
        print(f"{self.C.GOLD}║{' ' * ((width - len(title)) // 2)}{self.C.CRIMSON}{self.C.BOLD}{self.C.BLINK}{title}{self.C.END}{self.C.GOLD}{' ' * ((width - len(title)) // 2 - 1)}║{self.C.END}")
        print(f"{self.C.GOLD}║{' ' * ((width - len(subtitle)) // 2)}{self.C.PURPLE}{self.C.BOLD}{subtitle}{self.C.END}{self.C.GOLD}{' ' * ((width - len(subtitle)) // 2 - 1)}║{self.C.END}")
        
        # Author info
        print(f"{self.C.GOLD}╠{'═' * (width-2)}╣{self.C.END}")
        info = f"  Author: {self.author}  |  Version: {self.version}  |  Platform: {platform.system()}  "
        print(f"{self.C.GOLD}║{self.C.SKY}{info.center(width-2)}{self.C.GOLD}║{self.C.END}")
        print(f"{self.C.GOLD}╚{'═' * (width-2)}╝{self.C.END}")
        
    # ═══════════════════════════════════════════════════════════════
    # REAL-TIME CLOCK & STATUS BAR
    # ═══════════════════════════════════════════════════════════════
    def live_status_bar(self):
        while self.running:
            now = datetime.now()
            date_str = now.strftime("%A, %B %d, %Y")
            time_str = now.strftime("%H:%M:%S")
            hijri = self.get_hijri_date()
            
            status = f" ﷽  |  {date_str}  |  {self.C.GOLD}{time_str}{self.C.CYAN}  |  Hijri: {hijri}  |  {self.get_prayer_indicator()} "
            
            sys.stdout.write(f"\r{self.C.BG_PURPLE}{self.C.WHITE}{self.C.BOLD}{status.center(self.get_terminal_width())}{self.C.END}")
            sys.stdout.flush()
            time.sleep(1)
            
    def get_hijri_date(self):
        try:
            today = datetime.now()
            # Approximate Hijri calculation
            hijri_year = int((today.year - 622) * 1.03)
            hijri_month = ((today.month + 2) % 12) + 1
            hijri_day = today.day
            months = ["Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-thani", "Jumada al-awwal", 
                     "Jumada al-thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qi'dah", "Dhu al-Hijjah"]
            return f"{hijri_day} {months[hijri_month-1]} {hijri_year} AH"
        except:
            return "Unknown"
            
    def get_prayer_indicator(self):
        hour = datetime.now().hour
        prayers = {
            5: "☀️ Fajr",
            12: "☀️ Dhuhr", 
            15: "☀️ Asr",
            18: "🌅 Maghrib",
            20: "🌙 Isha"
        }
        for p_hour, name in sorted(prayers.items()):
            if hour <= p_hour:
                return name
        return "🌙 Isha"
        
    # ═══════════════════════════════════════════════════════════════
    # NETWORK INTELLIGENCE
    # ═══════════════════════════════════════════════════════════════
    def get_public_ip(self):
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            return response.json().get('ip', 'Unknown')
        except:
            return f"{self.C.RED}Offline{self.C.END}"
            
    def get_ip_details(self, ip):
        try:
            response = requests.get(f'https://ipapi.co/{ip}/json/', timeout=5)
            data = response.json()
            return {
                'ip': ip,
                'city': data.get('city', 'N/A'),
                'region': data.get('region', 'N/A'),
                'country': data.get('country_name', 'N/A'),
                'country_code': data.get('country_code', 'N/A'),
                'isp': data.get('org', 'N/A'),
                'asn': data.get('asn', 'N/A'),
                'timezone': data.get('timezone', 'N/A'),
                'latitude': data.get('latitude', 'N/A'),
                'longitude': data.get('longitude', 'N/A'),
                'currency': data.get('currency', 'N/A')
            }
        except:
            return None
            
    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
            
    def internet_speed_test(self):
        print(f"\n{self.C.GOLD}[⚡] INITIATING DIVINE SPEED TEST...{self.C.END}")
        self.animate_loading("Connecting to sacred servers")
        
        try:
            # Download speed test
            start_time = time.time()
            response = requests.get('https://speed.hetzner.de/10MB.bin', stream=True, timeout=30)
            total_length = int(response.headers.get('content-length', 0))
            
            downloaded = 0
            chunk_size = 1024
            for data in response.iter_content(chunk_size=chunk_size):
                downloaded += len(data)
                elapsed = time.time() - start_time
                if elapsed > 0:
                    speed = (downloaded / (1024*1024)) / elapsed
                    percent = (downloaded / total_length) * 100 if total_length > 0 else 0
                    sys.stdout.write(f"\r{self.C.CYAN}↓ Download: {self.C.GREEN}{speed:.2f} MB/s{self.C.CYAN} ({percent:.1f}%){self.C.END}")
                    sys.stdout.flush()
                    
            download_speed = (downloaded / (1024*1024)) / elapsed
            
            # Upload simulation (using httpbin)
            print(f"\n{self.C.CYAN}↑ Testing upload...{self.C.END}")
            upload_data = os.urandom(1024 * 1024)  # 1MB
            up_start = time.time()
            requests.post('https://httpbin.org/post', data=upload_data, timeout=30)
            upload_speed = 1 / (time.time() - up_start)
            
            # Ping test
            ping_times = []
            for _ in range(4):
                ping_start = time.time()
                requests.get('https://www.google.com', timeout=5)
                ping_times.append((time.time() - ping_start) * 1000)
            avg_ping = sum(ping_times) / len(ping_times)
            
            return {
                'download': download_speed,
                'upload': upload_speed,
                'ping': avg_ping
            }
        except Exception as e:
            print(f"{self.C.RED}[!] Speed test failed: {e}{self.C.END}")
            return None
            
    def display_speed_results(self, results):
        if not results:
            return
            
        print(f"\n{self.C.GOLD}{self.C.BOLD}╔{'═'*58}╗{self.C.END}")
        print(f"{self.C.GOLD}║{self.C.CENTER}  ⚡ INTERNET SPEED ANALYSIS  {self.C.GOLD}║{self.C.END}")
        print(f"{self.C.GOLD}╠{'═'*58}╣{self.C.END}")
        
        # Download bar
        dl_color = self.C.GREEN if results['download'] > 10 else self.C.YELLOW if results['download'] > 5 else self.C.RED
        dl_bar = "█" * int(min(results['download'], 50))
        print(f"{self.C.GOLD}║{self.C.END} {self.C.CYAN}↓ DOWNLOAD:{self.C.END} {dl_color}{results['download']:.2f} MB/s{self.C.END} {dl_bar}")
        
        # Upload bar
        ul_color = self.C.GREEN if results['upload'] > 5 else self.C.YELLOW if results['upload'] > 2 else self.C.RED
        ul_bar = "█" * int(min(results['upload'] * 5, 50))
        print(f"{self.C.GOLD}║{self.C.END} {self.C.CYAN}↑ UPLOAD:  {self.C.END} {ul_color}{results['upload']:.2f} MB/s{self.C.END} {ul_bar}")
        
        # Ping
        ping_color = self.C.GREEN if results['ping'] < 50 else self.C.YELLOW if results['ping'] < 100 else self.C.RED
        print(f"{self.C.GOLD}║{self.C.END} {self.C.CYAN}↔ PING:    {self.C.END} {ping_color}{results['ping']:.1f} ms{self.C.END}")
        
        print(f"{self.C.GOLD}╚{'═'*58}╝{self.C.END}")
        
    # ═══════════════════════════════════════════════════════════════
    # SYSTEM INTELLIGENCE MODULE
    # ═══════════════════════════════════════════════════════════════
    def system_intelligence(self):
        print(f"\n{self.C.EMERALD}{self.C.BOLD}[🔮] DIVINE SYSTEM INTELLIGENCE{self.C.END}")
        self.print_line("━", self.C.EMERALD)
        
        info = {
            "🖥️  Hostname": socket.gethostname(),
            "⚙️  Platform": f"{platform.system()} {platform.release()}",
            "🏗️  Architecture": platform.machine(),
            "🧠 Processor": platform.processor() or "Unknown",
            "🐍 Python": platform.python_version(),
            "📱 Termux": "✓ Installed" if 'TERMUX_VERSION' in os.environ else "✗ Not detected",
            "🔰 User": os.environ.get('USER', 'Unknown'),
            "🏠 Home": os.path.expanduser("~")
        }
        
        for key, value in info.items():
            print(f"  {self.C.GOLD}{key:<15}{self.C.END} {self.C.CYAN}➤{self.C.END} {self.C.WHITE}{self.C.BOLD}{value}{self.C.END}")
            
        # Memory info
        try:
            if platform.system() == "Linux":
                with open('/proc/meminfo', 'r') as f:
                    mem = f.read()
                    total = int(re.search(r'MemTotal:\s+(\d+)', mem).group(1)) / 1024
                    available = int(re.search(r'MemAvailable:\s+(\d+)', mem).group(1)) / 1024
                    used = total - available
                    percent = (used / total) * 100
                    
                    bar_color = self.C.GREEN if percent < 60 else self.C.YELLOW if percent < 80 else self.C.RED
                    bar = "█" * int(percent / 2) + "░" * (50 - int(percent / 2))
                    
                    print(f"\n  {self.C.GOLD}💾 Memory Usage:{self.C.END}")
                    print(f"  {bar_color}{bar}{self.C.END}")
                    print(f"  {self.C.CYAN}Used:{self.C.END} {self.C.WHITE}{used:.0f}MB{self.C.END} / {self.C.CYAN}Total:{self.C.END} {self.C.WHITE}{total:.0f}MB{self.C.END} ({self.C.RED}{percent:.1f}%{self.C.END})")
        except:
            pass
            
    # ═══════════════════════════════════════════════════════════════
    # NETWORK RECONNAISSANCE
    # ═══════════════════════════════════════════════════════════════
    def network_reconnaissance(self):
        print(f"\n{self.C.SKY}{self.C.BOLD}[🌐] CELESTIAL NETWORK RECONNAISSANCE{self.C.END}")
        self.print_line("━", self.C.SKY)
        
        local_ip = self.get_local_ip()
        public_ip = self.get_public_ip()
        
        print(f"  {self.C.GOLD}🌐 Local IP:{self.C.END}    {self.C.GREEN}{self.C.BOLD}{local_ip}{self.C.END}")
        print(f"  {self.C.GOLD}🌍 Public IP:{self.C.END}   {self.C.GREEN}{self.C.BOLD}{public_ip}{self.C.END}")
        
        if public_ip and 'Offline' not in public_ip:
            details = self.get_ip_details(public_ip)
            if details:
                print(f"\n  {self.C.PURPLE}{self.C.BOLD}📍 GEOLOCATION INTELLIGENCE:{self.C.END}")
                geo_data = [
                    ("🏙️  City", details['city']),
                    ("🗺️  Region", details['region']),
                    ("🇺🇳 Country", f"{details['country']} ({details['country_code']})"),
                    ("🏢 ISP/Org", details['isp']),
                    ("🔢 ASN", details['asn']),
                    ("🕐 Timezone", details['timezone']),
                    ("📍 Coordinates", f"{details['latitude']}, {details['longitude']}"),
                    ("💰 Currency", details['currency'])
                ]
                for key, value in geo_data:
                    print(f"    {self.C.YELLOW}{key:<15}{self.C.END} {self.C.CYAN}➤{self.C.END} {self.C.WHITE}{value}{self.C.END}")
                    
        # Network interfaces
        print(f"\n  {self.C.PURPLE}{self.C.BOLD}🔌 NETWORK INTERFACES:{self.C.END}")
        try:
            if platform.system() == "Linux":
                result = subprocess.check_output(['ip', 'addr'], universal_newlines=True)
                for line in result.split('\n'):
                    if 'inet ' in line and '127.0.0.1' not in line:
                        parts = line.strip().split()
                        if len(parts) >= 2:
                            ip = parts[1].split('/')[0]
                            iface = line.split()[-1] if 'scope' in line else 'unknown'
                            print(f"    {self.C.YELLOW}📡{self.C.END} {self.C.CYAN}{iface:<10}{self.C.END} {self.C.GREEN}{ip}{self.C.END}")
        except:
            pass
            
    # ═══════════════════════════════════════════════════════════════
    # PORT SCANNER - ADVANCED
    # ═══════════════════════════════════════════════════════════════
    def divine_port_scanner(self):
        target = input(f"\n{self.C.GOLD}[?] Enter target (IP/Domain): {self.C.END}").strip()
        if not target:
            return
            
        try:
            target_ip = socket.gethostbyname(target)
        except:
            print(f"{self.C.RED}[!] Could not resolve target{self.C.END}")
            return
            
        print(f"\n{self.C.CRIMSON}{self.C.BOLD}[⚔️] INITIATING DIVINE PORT SCAN{self.C.END}")
        print(f"{self.C.GOLD}Target:{self.C.END} {self.C.CYAN}{target} ({target_ip}){self.C.END}")
        
        # Common ports with services
        port_services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
            3389: "RDP", 5432: "PostgreSQL", 8080: "HTTP-Proxy", 8443: "HTTPS-Alt"
        }
        
        print(f"\n{self.C.GOLD}{self.C.BOLD}╔{'═'*60}╗{self.C.END}")
        print(f"{self.C.GOLD}║{self.C.END} {self.C.CYAN}{'PORT':<8}{'STATE':<10}{'SERVICE':<15}{'BANNER':<25}{self.C.GOLD}║{self.C.END}")
        print(f"{self.C.GOLD}╠{'═'*60}╣{self.C.END}")
        
        open_ports = []
        for port, service in port_services.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                banner = ""
                try:
                    sock.settimeout(2)
                    sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()[:20]
                except:
                    pass
                    
                print(f"{self.C.GOLD}║{self.C.END} {self.C.GREEN}{port:<8}{'OPEN':<10}{service:<15}{banner:<25}{self.C.GOLD}║{self.C.END}")
                open_ports.append(port)
            else:
                print(f"{self.C.GOLD}║{self.C.END} {self.C.DIM}{port:<8}{'CLOSED':<10}{service:<15}{self.C.END}{' '*25}{self.C.GOLD}║{self.C.END}")
            sock.close()
            
        print(f"{self.C.GOLD}╚{'═'*60}╝{self.C.END}")
        print(f"\n{self.C.YELLOW}[✓] Scan complete. {len(open_ports)} ports open.{self.C.END}")
        
    # ═══════════════════════════════════════════════════════════════
    # WIFI ANALYZER
    # ═══════════════════════════════════════════════════════════════
    def wifi_analyzer(self):
        print(f"\n{self.C.LIME}{self.C.BOLD}[📶] WIRELESS SPECTRUM ANALYSIS{self.C.END}")
        self.print_line("━", self.C.LIME)
        
        try:
            if 'TERMUX_VERSION' in os.environ:
                # Termux wifi scan
                result = subprocess.check_output(['termux-wifi-scaninfo'], universal_newlines=True)
                networks = json.loads(result)
                
                print(f"  {self.C.GOLD}{'SSID':<25}{'BSSID':<20}{'SIGNAL':<10}{'CHANNEL':<10}{self.C.END}")
                print(f"  {self.C.CYAN}{'─'*65}{self.C.END}")
                
                for net in networks:
                    ssid = net.get('ssid', 'Hidden')[:23]
                    bssid = net.get('bssid', 'N/A')
                    signal = net.get('rssi', 0)
                    channel = net.get('frequency', 'N/A')
                    
                    # Signal strength color
                    if signal > -50:
                        sig_color = self.C.GREEN
                    elif signal > -70:
                        sig_color = self.C.YELLOW
                    else:
                        sig_color = self.C.RED
                        
                    print(f"  {self.C.WHITE}{ssid:<25}{self.C.END}{self.C.CYAN}{bssid:<20}{self.C.END}{sig_color}{signal:<10}{self.C.END}{self.C.YELLOW}{channel:<10}{self.C.END}")
            else:
                # Linux wifi
                result = subprocess.check_output(['iwlist', 'scan'], universal_newlines=True, stderr=subprocess.DEVNULL)
                cells = re.findall(r'Cell \d+ - Address: ([\w:]+).*?ESSID:"([^"]*)".*?Signal level=(-?\d+)', result, re.DOTALL)
                
                for addr, ssid, signal in cells:
                    signal = int(signal)
                    sig_color = self.C.GREEN if signal > -50 else self.C.YELLOW if signal > -70 else self.C.RED
                    print(f"  {self.C.WHITE}{ssid:<25}{self.C.END} {self.C.CYAN}{addr}{self.C.END} {sig_color}{signal} dBm{self.C.END}")
                    
        except Exception as e:
            print(f"{self.C.RED}[!] WiFi scan unavailable: {e}{self.C.END}")
            
    # ═══════════════════════════════════════════════════════════════
    # DIVINE MENU
    # ═══════════════════════════════════════════════════════════════
    def divine_menu(self):
        width = self.get_terminal_width()
        menu_width = 70
        
        print(f"\n{self.C.GOLD}{self.C.BOLD}╔{'═'*menu_width}╗{self.C.END}")
        print(f"{self.C.GOLD}║{' '*((menu_width-30)//2)}{self.C.CYAN}{self.C.BOLD}⚡ DIVINE OPERATIONS CENTER ⚡{' '*((menu_width-30)//2)}{self.C.GOLD}║{self.C.END}")
        print(f"{self.C.GOLD}╠{'═'*menu_width}╣{self.C.END}")
        
        options = [
            ("[1]", "🖥️  System Intelligence", "[5]", "📶 WiFi Analyzer"),
            ("[2]", "🌐 Network Reconnaissance", "[6]", "🌡️  System Monitor"),
            ("[3]", "⚡ Internet Speed Test", "[7]", "📡 Packet Tracer"),
            ("[4]", "⚔️  Port Scanner", "[8]", "🔐 Security Audit"),
            ("[9]", "🧹 Clear Screen", "[0]", "🚪 Exit (Alhamdulillah)")
        ]
        
        for i in range(0, len(options), 2):
            left = f"  {self.C.GOLD}{self.C.BOLD}{options[i][0]}{self.C.END} {self.C.WHITE}{options[i][1]}{self.C.END}"
            right = f"  {self.C.GOLD}{self.C.BOLD}{options[i+1][0]}{self.C.END} {self.C.WHITE}{options[i+1][1]}{self.C.END}"
            padding = menu_width - len(f"  {options[i][0]} {options[i][1]}  {options[i+1][0]} {options[i+1][1]}") - 4
            print(f"{self.C.GOLD}║{left}{' '*padding}{right}{self.C.GOLD}║{self.C.END}")
            
        print(f"{self.C.GOLD}╚{'═'*menu_width}╝{self.C.END}")
        
    def system_monitor(self):
        print(f"\n{self.C.SUNSET}{self.C.BOLD}[🌡️] REAL-TIME SYSTEM MONITOR{self.C.END}")
        print(f"{self.C.YELLOW}(Press Ctrl+C to stop){self.C.END}\n")
        
        try:
            while True:
                # CPU usage
                if platform.system() == "Linux":
                    with open('/proc/loadavg', 'r') as f:
                        load = f.read().split()[:3]
                    print(f"\r{self.C.GOLD}CPU Load:{self.C.END} {self.C.CYAN}{load[0]}{self.C.END} {self.C.YELLOW}{load[1]}{self.C.END} {self.C.RED}{load[2]}{self.C.END} | ", end="")
                    
                    # Memory
                    with open('/proc/meminfo', 'r') as f:
                        mem = f.read()
                        total = int(re.search(r'MemTotal:\s+(\d+)', mem).group(1))
                        free = int(re.search(r'MemFree:\s+(\d+)', mem).group(1))
                        used = ((total - free) / total) * 100
                        
                    mem_bar = "█" * int(used / 5) + "░" * (20 - int(used / 5))
                    mem_color = self.C.GREEN if used < 60 else self.C.YELLOW if used < 80 else self.C.RED
                    print(f"{self.C.GOLD}RAM:{self.C.END} {mem_color}{mem_bar}{self.C.END} {self.C.WHITE}{used:.1f}%{self.C.END} | ", end="")
                    
                    # Uptime
                    with open('/proc/uptime', 'r') as f:
                        uptime = float(f.read().split()[0])
                        hours = int(uptime // 3600)
                        minutes = int((uptime % 3600) // 60)
                    print(f"{self.C.GOLD}Uptime:{self.C.END} {self.C.CYAN}{hours}h {minutes}m{self.C.END}", end="")
                    
                    sys.stdout.flush()
                    time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{self.C.GREEN}[✓] Monitor stopped{self.C.END}")
            
    def packet_tracer(self):
        print(f"\n{self.C.PINK}{self.C.BOLD}[📡] PACKET TRACE ROUTE{self.C.END}")
        target = input(f"{self.C.GOLD}[?] Enter target: {self.C.END}").strip()
        
        if not target:
            return
            
        print(f"\n{self.C.CYAN}Tracing route to {target}...{self.C.END}\n")
        try:
            if platform.system().lower() != 'windows':
                result = subprocess.check_output(['traceroute', '-m', '15', '-w', '2', target], 
                                               universal_newlines=True, stderr=subprocess.STDOUT)
            else:
                result = subprocess.check_output(['tracert', '-h', '15', '-w', '2000', target], 
                                               universal_newlines=True)
                                               
            for line in result.split('\n'):
                if line.strip():
                    if '*' in line:
                        print(f"  {self.C.RED}{line}{self.C.END}")
                    elif 'ms' in line:
                        print(f"  {self.C.GREEN}{line}{self.C.END}")
                    else:
                        print(f"  {self.C.CYAN}{line}{self.C.END}")
        except Exception as e:
            print(f"{self.C.RED}[!] Trace failed: {e}{self.C.END}")
            
    def security_audit(self):
        print(f"\n{self.C.CRIMSON}{self.C.BOLD}[🔐] DIVINE SECURITY AUDIT{self.C.END}")
        self.print_line("━", self.C.CRIMSON)
        
        checks = {
            "🔒 Root Access": "✓ YES" if os.geteuid() == 0 else "✗ NO (Good)",
            "🛡️  Firewall": "Check with: iptables -L",
            "🔑 SSH Service": "Active" if subprocess.call(['pgrep', 'sshd'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0 else "Inactive",
            "📝 Sudoers": "Configured" if os.path.exists('/etc/sudoers') else "N/A",
            "🦠 Termux": f"Version: {os.environ.get('TERMUX_VERSION', 'N/A')}"
        }
        
        for key, value in checks.items():
            color = self.C.GREEN if "YES" in value or "Active" in value or "Good" in value else self.C.YELLOW
            print(f"  {self.C.GOLD}{key:<15}{self.C.END} {self.C.CYAN}➤{self.C.END} {color}{value}{self.C.END}")
            
    # ═══════════════════════════════════════════════════════════════
    # MAIN EXECUTION
    # ═══════════════════════════════════════════════════════════════
    def run(self):
        self.supreme_banner()
        self.divine_bismillah()
        
        # Start live clock
        clock_thread = threading.Thread(target=self.live_status_bar, daemon=True)
        clock_thread.start()
        
        time.sleep(2)
        
        while True:
            print("\n")
            self.divine_menu()
            
            try:
                choice = input(f"\n{self.C.BG_GOLD}{self.C.BLACK}{self.C.BOLD} [AbdUrRab@ARTHA1]~# {self.C.END} ").strip()
            except EOFError:
                continue
                
            print("\n")
            
            if choice == '1':
                self.system_intelligence()
            elif choice == '2':
                self.network_reconnaissance()
            elif choice == '3':
                results = self.internet_speed_test()
                self.display_speed_results(results)
            elif choice == '4':
                self.divine_port_scanner()
            elif choice == '5':
                self.wifi_analyzer()
            elif choice == '6':
                self.system_monitor()
            elif choice == '7':
                self.packet_tracer()
            elif choice == '8':
                self.security_audit()
            elif choice == '9':
                self.clear()
                self.supreme_banner()
                self.divine_bismillah()
            elif choice == '0':
                print(f"{self.C.GOLD}{self.C.BOLD}")
                print("  ╔═══════════════════════════════════════════════════════╗")
                print("  ║  Alhamdulillah! All praise is due to Allah (SWT)     ║")
                print("  ║  Tool terminated successfully.                       ║")
                print("  ║  May Allah bless Abd Ur Rab and all righteous users. ║")
                print("  ╚═══════════════════════════════════════════════════════╝")
                print(f"{self.C.END}")
                self.running = False
                break
            else:
                print(f"{self.C.RED}[!] Invalid command. Please choose wisely.{self.C.END}")
                
            input(f"\n{self.C.YELLOW}[Press Enter to return to Divine Menu...]{self.C.END}")

if __name__ == "__main__":
    try:
        tool = ARTHDivineToolkit()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{self.C.GOLD}\n  ﷽  Interrupted by user. As-Salamu Alaykum.  ﷽{self.C.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{self.C.RED}[!] Divine Error: {e}{self.C.END}")
        sys.exit(1)
