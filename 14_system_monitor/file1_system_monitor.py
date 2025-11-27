import psutil

def system_monitor():
    print("CPU:", psutil.cpu_percent(), "%")
    print("RAM:", psutil.virtual_memory().percent, "%")
    print("Disk:", psutil.disk_usage('/').percent, "%")
