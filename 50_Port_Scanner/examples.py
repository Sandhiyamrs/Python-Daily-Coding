from file1_port_scanner import scan_ports

open_ports = scan_ports("127.0.0.1", start=20, end=100)

print("Open Ports:")
for port in open_ports:
    print(f"Port {port} is open")
