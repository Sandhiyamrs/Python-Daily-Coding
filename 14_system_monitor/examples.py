from solution import get_system_stats

stats = get_system_stats()
print("CPU Usage:", stats["cpu"])
print("Memory Usage:", stats["memory"])
