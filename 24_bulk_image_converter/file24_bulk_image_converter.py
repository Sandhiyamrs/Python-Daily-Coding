from PIL import Image
import os

folder = input("Enter folder path with images: ")
target_format = input("Enter target format (e.g., PNG, JPG): ").upper()

for file in os.listdir(folder):
    if file.endswith(("png", "jpg", "jpeg")):
        img = Image.open(os.path.join(folder, file))
        base_name = os.path.splitext(file)[0]
        img.save(os.path.join(folder, f"{base_name}.{target_format.lower()}"))
        print(f"Converted {file} to {target_format}")
