from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os

class WatermarkTool:
    def __init__(self):
        self.positions = {
            '1': 'top-left',
            '2': 'top-right',
            '3': 'center',
            '4': 'bottom-left',
            '5': 'bottom-right'
        }
    
    def calculate_position(self, base_size, watermark_size, position):
        """Calculate watermark position."""
        base_w, base_h = base_size
        wm_w, wm_h = watermark_size
        margin = 10
        
        positions = {
            'top-left': (margin, margin),
            'top-right': (base_w - wm_w - margin, margin),
            'center': ((base_w - wm_w) // 2, (base_h - wm_h) // 2),
            'bottom-left': (margin, base_h - wm_h - margin),
            'bottom-right': (base_w - wm_w - margin, base_h - wm_h - margin)
        }
        
        return positions.get(position, (margin, margin))
    
    def add_text_watermark(self, image_path, text, position='bottom-right', 
                          opacity=128, font_size=36, output_path=None):
        """Add text watermark to image."""
        try:
            # Open image
            image = Image.open(image_path).convert('RGBA')
            
            # Create transparent layer
            txt_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt_layer)
            
            # Try to use a font, fallback to default
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            
            # Get text size
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Calculate position
            pos = self.calculate_position(image.size, (text_width, text_height), position)
            
            # Draw text
            draw.text(pos, text, fill=(255, 255, 255, opacity), font=font)
            
            # Combine images
            watermarked = Image.alpha_composite(image, txt_layer)
            watermarked = watermarked.convert('RGB')
            
            # Save
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_watermarked{ext}"
            
            watermarked.save(output_path)
            return output_path
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def add_image_watermark(self, image_path, watermark_path, position='bottom-right',
                           opacity=128, scale=0.2, output_path=None):
        """Add image watermark."""
        try:
            # Open images
            base_image = Image.open(image_path).convert('RGBA')
            watermark = Image.open(watermark_path).convert('RGBA')
            
            # Scale watermark
            wm_width = int(base_image.size[0] * scale)
            wm_height = int(watermark.size[1] * (wm_width / watermark.size[0]))
            watermark = watermark.resize((wm_width, wm_height), Image.Resampling.LANCZOS)
            
            # Adjust opacity
            alpha = watermark.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(opacity / 255)
            watermark.putalpha(alpha)
            
            # Calculate position
            pos = self.calculate_position(base_image.size, watermark.size, position)
            
            # Create transparent layer
            transparent = Image.new('RGBA', base_image.size, (0, 0, 0, 0))
            transparent.paste(watermark, pos)
            
            # Combine
            watermarked = Image.alpha_composite(base_image, transparent)
            watermarked = watermarked.convert('RGB')
            
            # Save
            if output_path is None:
                name, ext = os.path.splitext(image_path)
                output_path = f"{name}_watermarked{ext}"
            
            watermarked.save(output_path)
            return output_path
        
        except Exception as e:
            print(f"Error: {e}")
            return None

def main():
    print("=== Image Watermark Tool ===\n")
    
    tool = WatermarkTool()
    
    image_path = input("Enter image path: ").strip()
    
    if not os.path.exists(image_path):
        print("Error: Image not found!")
        return
    
    print("\nWatermark Type:")
    print("1. Text Watermark")
    print("2. Image Watermark")
    
    wm_type = input("\nEnter choice (1-2): ").strip()
    
    print("\nPosition:")
    print("1. Top-Left")
    print("2. Top-Right")
    print("3. Center")
    print("4. Bottom-Left")
    print("5. Bottom-Right")
    
    pos_choice = input("\nEnter position (1-5): ").strip()
    position = tool.positions.get(pos_choice, 'bottom-right')
    
    opacity = int(input("Enter opacity (0-255, default 128): ").strip() or "128")
    
    if wm_type == '1':
        text = input("Enter watermark text: ").strip()
        font_size = int(input("Enter font size (default 36): ").strip() or "36")
        
        output = tool.add_text_watermark(image_path, text, position, opacity, font_size)
    
    elif wm_type == '2':
        watermark_path = input("Enter watermark image path: ").strip()
        
        if not os.path.exists(watermark_path):
            print("Error: Watermark image not found!")
            return
        
        scale = float(input("Enter watermark scale (0.1-1.0, default 0.2): ").strip() or "0.2")
        
        output = tool.add_image_watermark(image_path, watermark_path, position, opacity, scale)
    
    else:
        print("Invalid choice!")
        return
    
    if output:
        print(f"\n✓ Watermarked image saved: {output}")
    else:
        print("\n✗ Failed to add watermark!")

if __name__ == "__main__":
    main()
