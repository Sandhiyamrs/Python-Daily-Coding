from collections import Counter

def analyze_log(file_path):
    levels = Counter()
    errors = []

    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("INFO"):
                levels["INFO"] += 1
            elif line.startswith("WARNING"):
                levels["WARNING"] += 1
            elif line.startswith("ERROR"):
                levels["ERROR"] += 1
                errors.append(line.strip())

    print("Log Summary:")
    for level, count in levels.items():
        print(f"{level}: {count}")

    if errors:
        common_error = Counter(errors).most_common(1)[0][0]
        print("\nMost Frequent Error:")
        print(common_error)

# Example usage
# analyze_log("log.txt")
