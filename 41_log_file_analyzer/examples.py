from file1_log_file_analyzer import analyze_logs

summary = analyze_logs("application.log")

print("==== LOG SUMMARY ====")
print("Errors     :", summary.get("errors", 0))
print("Warnings   :", summary.get("warnings", 0))
print("Info Logs  :", summary.get("info", 0))
print("Top IPs    :", summary.get("top_ips", []))
