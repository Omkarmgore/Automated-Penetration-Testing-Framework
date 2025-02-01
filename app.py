import nmap
import logging
import json
import os
import subprocess
import socket
import threading
import bcrypt
from datetime import datetime
from getpass import getpass
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

# Initialize rich console
console = Console()

# Configure logging
logging.basicConfig(
    filename='pentest_framework.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)
logger = logging.getLogger()

# Configuration management
class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()
        
    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Config file not found")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON in config file")
            raise

    def get(self, key, default=None):
        return self.config.get(key, default)

# Initialize configuration
try:
    config = ConfigManager().config
except:
    console.print("[bold red]Error loading configuration![/bold red]")
    exit(1)

# Authentication System
class Authenticator:
    def __init__(self):
        self.users = self.load_users()
        
    def load_users(self):
        try:
            with open('users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def authenticate(self):
        console.print("\n[bold cyan]Authentication Required[/bold cyan]")
        username = input("Username: ")
        password = getpass("Password: ")
        
        if username in self.users and bcrypt.checkpw(password.encode(), self.users[username].encode()):
            logger.info(f"User {username} authenticated successfully")
            return username
        logger.warning(f"Failed authentication attempt for {username}")
        return None

# Advanced Scanner Classes
class AdvancedNetworkScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.lock = threading.Lock()
        
    def threaded_scan(self, network_range, options, max_threads=4):
        try:
            hosts = self.nm.listscan(network_range)
            chunk_size = len(hosts) // max_threads or 1
            threads = []
            
            with Progress() as progress:
                task = progress.add_task("[cyan]Scanning...", total=len(hosts))
                
                for i in range(0, len(hosts), chunk_size):
                    chunk = hosts[i:i+chunk_size]
                    t = threading.Thread(
                        target=self._scan_chunk,
                        args=(chunk, options, progress, task)
                    )
                    threads.append(t)
                    t.start()
                
                for t in threads:
                    t.join()
            
            return self.nm.all_hosts()
        except nmap.PortScannerError as e:
            logger.error(f"Nmap error: {e}")
            return []

    def _scan_chunk(self, hosts, options, progress, task):
        for host in hosts:
            try:
                self.nm.scan(hosts=host, arguments=options)
                with self.lock:
                    progress.update(task, advance=1)
            except Exception as e:
                logger.error(f"Error scanning {host}: {e}")

class VulnerabilityScanner:
    @staticmethod
    def run_nikto(target):
        try:
            result = subprocess.run(
                ['nikto', '-h', target],
                capture_output=True,
                text=True,
                timeout=600
            )
            return result.stdout
        except Exception as e:
            logger.error(f"Nikto error: {e}")
            return None

    @staticmethod
    def run_nmap_vuln_scripts(target):
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='--script vuln')
            return nm[target]
        except Exception as e:
            logger.error(f"Nmap vuln scan error: {e}")
            return None

# Reporting System
class ReportGenerator:
    @staticmethod
    def generate_html_report(report_data, report_type):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/{report_type}_report_{timestamp}.html"
        
        try:
            os.makedirs('reports', exist_ok=True)
            with open(filename, 'w') as f:
                f.write("<html><body>")
                f.write(f"<h1>{report_type.capitalize()} Report</h1>")
                f.write(f"<p>Generated at: {timestamp}</p>")
                
                if report_type == "network":
                    for host in report_data['hosts']:
                        f.write(f"<h2>Host: {host['ip']}</h2>")
                        f.write("<h3>Open Ports:</h3><ul>")
                        for port in host['ports']:
                            f.write(f"<li>{port['port']} ({port['service']}) - {port['state']}</li>")
                        f.write("</ul>")
                
                f.write("</body></html>")
            return filename
        except Exception as e:
            logger.error(f"Error generating HTML report: {e}")
            return None

# Enhanced UI Components
class PentestUI:
    @staticmethod
    def display_menu():
        console.print("\n[bold magenta]Advanced PenTest Framework[/bold magenta]")
        console.print("1. Advanced Network Scan")
        console.print("2. Targeted Vulnerability Scan")
        console.print("3. Web Application Scan")
        console.print("4. Brute Force Attack")
        console.print("5. View Reports")
        console.print("6. Exit")

    @staticmethod
    def display_scan_types():
        table = Table(title="Available Scan Types")
        table.add_column("ID", style="cyan")
        table.add_column("Scan Type", style="magenta")
        table.add_column("Description")
        
        scan_types = [
            ("1", "SYN Scan", "Stealthy TCP SYN scan"),
            ("2", "UDP Scan", "UDP port scanning"),
            ("3", "Full Scan", "Aggressive scan with OS and service detection"),
            ("4", "Vulnerability Scan", "Nmap vulnerability scripts")
        ]
        
        for st in scan_types:
            table.add_row(*st)
            
        console.print(table)

# Main Application
class PentestFramework:
    def __init__(self):
        self.auth = Authenticator()
        self.scanner = AdvancedNetworkScanner()
        self.ui = PentestUI()
        self.reports = []
        
    def run(self):
        user = self.auth.authenticate()
        if not user:
            console.print("[bold red]Authentication failed![/bold red]")
            return
            
        console.print(f"\n[bold green]Welcome {user}![/bold green]")
        
        while True:
            self.ui.display_menu()
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                self.network_scan_workflow()
            elif choice == "2":
                self.vulnerability_scan_workflow()
            elif choice == "5":
                self.view_reports()
            elif choice == "6":
                console.print("[bold yellow]Exiting...[/bold yellow]")
                break
            else:
                console.print("[bold red]Invalid choice![/bold red]")

    def network_scan_workflow(self):
        self.ui.display_scan_types()
        scan_type = input("Select scan type: ")
        target = input("Enter target (IP/CIDR): ")
        
        options = {
            '1': '-sS',
            '2': '-sU',
            '3': '-A -T4',
            '4': '--script vuln'
        }.get(scan_type, '-sS')
        
        with console.status("[bold green]Scanning network...[/bold green]"):
            results = self.scanner.threaded_scan(target, options)
            report = self.process_scan_results(results)
            self.reports.append(report)
            console.print("[bold green]Scan completed![/bold green]")

    def process_scan_results(self, results):
        report = {'hosts': []}
        for host in results:
            host_info = self.scanner.nm[host]
            ports = []
            
            for proto in host_info.all_protocols():
                for port in host_info[proto].keys():
                    service = host_info[proto][port].get('name', 'unknown')
                    state = host_info[proto][port]['state']
                    ports.append({
                        'port': port,
                        'service': service,
                        'state': state
                    })
            
            report['hosts'].append({
                'ip': host,
                'ports': ports
            })
        
        ReportGenerator.generate_html_report(report, "network")
        return report

    def vulnerability_scan_workflow(self):
        target = input("Enter target IP/hostname: ")
        console.print("\n[bold]Vulnerability Scan Options:[/bold]")
        console.print("1. Web Application Scan (Nikto)")
        console.print("2. Network Vulnerability Scan (Nmap)")
        choice = input("Select scan type: ")
        
        with console.status("[bold green]Running vulnerability scan...[/bold green]"):
            if choice == "1":
                results = VulnerabilityScanner.run_nikto(target)
            elif choice == "2":
                results = VulnerabilityScanner.run_nmap_vuln_scripts(target)
            else:
                console.print("[bold red]Invalid choice![/bold red]")
                return
            
            self.reports.append(results)
            console.print(results)

    def view_reports(self):
        report_files = [f for f in os.listdir('reports') if f.endswith('.html')]
        if not report_files:
            console.print("[bold yellow]No reports found![/bold yellow]")
            return
            
        table = Table(title="Available Reports")
        table.add_column("ID", style="cyan")
        table.add_column("Report Name")
        
        for idx, file in enumerate(report_files, 1):
            table.add_row(str(idx), file)
            
        console.print(table)
        choice = input("Select report to view (or 'q' to quit): ")
        
        if choice != 'q' and choice.isdigit():
            os.system(f"open reports/{report_files[int(choice)-1]}")

if __name__ == "__main__":
    try:
        framework = PentestFramework()
        framework.run()
    except KeyboardInterrupt:
        console.print("\n[bold red]Operation cancelled by user![/bold red]")
    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
        console.print(f"[bold red]Critical error: {str(e)}[/bold red]")
