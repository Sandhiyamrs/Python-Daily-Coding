def analyze_log(file_path):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(file_path, "r") as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1

    print("Log Analysis Report")
    for k, v in counts.items():
        print(f"{k}: {v}")

# Example usage
# analyze_log("system.log")
