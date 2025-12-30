from file1_log_file_analyzer import analyze_logs

result = analyze_logs("server.log")

print("Total Errors:", result["errors"])
print("Total Warnings:", result["warnings"])
print("Top IPs:", result["top_ips"])
