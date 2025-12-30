import socket
import threading
from queue import Queue
from datetime import datetime

# Common port services
COMMON_PORTS = {
    21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
    53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP',
    443: 'HTTPS', 445: 'SMB', 3306: 'MySQL', 3389: 'RDP',
    5432: 'PostgreSQL', 5900: 'VNC', 8080: 'HTTP-Proxy',
    27017: 'MongoDB', 6379: 'Redis'
}

class PortScanner:
    def __init__(self, target, timeout=1, threads=100):
        self.target = target
        self.timeout = timeout
        self.threads = threads
        self.open_ports = []
        self.queue = Queue()
        self.lock = threading.Lock()
    
    def resolve_host(self):
        """Resolve hostname to IP."""
        try:
            return socket.gethostbyname(self.target)
        except socket.gaierror:
            return None
    
    def scan_port(self, port):
        """Scan a single port."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            sock.close()
            
            if result == 0:
                service = COMMON_PORTS.get(port, 'Unknown')
                with self.lock:
                    self.open_ports.append((port, service))
                    print(f"[+] Port {port} is OPEN - {service}")
        
        except Exception:
            pass
    
    def worker(self):
        """Worker thread to process port queue."""
        while True:
            port = self.queue.get()
            if port is None:
                break
            self.scan_port(port)
            self.queue.task_done()
    
    def scan(self, start_port=1, end_port=1024):
        """Scan ports in range."""
        print(f"\n[*] Scanning {self.target} ({self.resolve_host()})")
        print(f"[*] Port range: {start_port}-{end_port}")
        print(f"[*] Threads: {self.threads}")
        print(f"[*] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Start worker threads
        threads_list = []
        for _ in range(self.threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads_list.append(t)
        
        # Add ports to queue
        for port in range(start_port, end_port + 1):
            self.queue.put(port)
        
        # Wait for completion
        self.queue.join()
        
        # Stop workers
        for _ in range(self.threads):
            self.queue.put(None)
        
        for t in threads_list:
            t.join()
        
        return self.open_ports

def main():
    print("=== Port Scanner ===\n")
    
    target = input("Enter target host (IP or domain): ").strip()
    
    scanner = PortScanner(target)
    
    # Resolve hostname
    ip = scanner.resolve_host()
    if not ip:
        print("\n✗ Error: Unable to resolve hostname!")
        return
    
    print("\nScan Options:")
    print("1. Common Ports (Quick Scan)")
    print("2. Well-Known Ports (1-1024)")
    print("3. All Ports (1-65535)")
    print("4. Custom Range")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == '1':
        # Scan only common ports
        for port in COMMON_PORTS.keys():
            scanner.queue.put(port)
        scanner.scan(1, 1)  # Dummy call to setup
    
    elif choice == '2':
        open_ports = scanner.scan(1, 1024)
    
    elif choice == '3':
        print("\n⚠ Warning: Full port scan may take several minutes!")
        confirm = input("Continue? (y/n): ").lower()
        if confirm == 'y':
            open_ports = scanner.scan(1, 65535)
    
    elif choice == '4':
        start = int(input("Enter start port: ").strip())
        end = int(input("Enter end port: ").strip())
        open_ports = scanner.scan(start, end)
    
    else:
        print("\n✗ Invalid choice!")
        return
    
    # Results summary
    print(f"\n{'='*50}")
    print(f"[*] Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[*] Total open ports found: {len(scanner.open_ports)}")
    
    if scanner.open_ports:
        print(f"\n{'Port':<10} {'Service':<20}")
        print("-" * 30)
        for port, service in sorted(scanner.open_ports):
            print(f"{port:<10} {service:<20}")
    
    # Save results
    save = input("\n\nSave results to file? (y/n): ").lower()
    if save == 'y':
        filename = f"scan_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Port Scan Results\n")
            f.write(f"Target: {target} ({ip})\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"{'Port':<10} {'Service':<20}\n")
            f.write("-" * 30 + "\n")
            for port, service in sorted(scanner.open_ports):
                f.write(f"{port:<10} {service:<20}\n")
        
        print(f"✓ Results saved to {filename}")

if __name__ == "__main__":
    main()
