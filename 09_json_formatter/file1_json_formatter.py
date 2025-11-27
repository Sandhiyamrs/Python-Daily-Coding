import json

def format_json(input_path, output_path):
    with open(input_path, "r") as f:
        data = json.load(f)

    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

    print("JSON formatted and saved!")
