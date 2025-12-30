import markdown
import os

def convert_markdown_to_html(md_file, output_file=None):
    """Convert markdown file to HTML."""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        # Create full HTML document
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted from Markdown</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            line-height: 1.6;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Determine output filename
        if output_file is None:
            output_file = os.path.splitext(md_file)[0] + '.html'
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        return output_file
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    print("=== Markdown to HTML Converter ===\n")
    
    md_file = input("Enter markdown file path: ").strip()
    
    if not os.path.exists(md_file):
        print("Error: File not found!")
        return
    
    output_file = input("Enter output HTML file path (or press Enter for auto): ").strip()
    
    if not output_file:
        output_file = None
    
    result = convert_markdown_to_html(md_file, output_file)
    
    if result:
        print(f"\n✓ Successfully converted to: {result}")
    else:
        print("\n✗ Conversion failed!")

if __name__ == "__main__":
    main()
