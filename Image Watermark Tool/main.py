import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

root = tk.Tk()
root.title("Watermark App")
root.geometry("400x300")

def add_watermark():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if not file_path:
        return

    image = Image.open(file_path).convert("RGBA")
    print(f"Image size: {image.size}")  # Check image dimensions
    
    watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark_layer)
    
    watermark_text = "mywebsite.com"
    font_size = 50
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        print("Font not found, using default")
        font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    print(f"Text size: {text_width}x{text_height}")  # Check text dimensions
    
    position = (image.width - text_width - 10, image.height - text_height - 10)
    print(f"Watermark position: {position}")  # Check position
    
    draw.text(position, watermark_text, font=font, fill=(0, 0, 0, 255))  # Use black, opaque
    
    watermarked_image = Image.alpha_composite(image, watermark_layer)
    watermarked_image = watermarked_image.convert("RGB")
    
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    if save_path:
        watermarked_image.save(save_path)
        print("Image saved successfully!")

upload_button = tk.Button(root, text="Upload Image & Add Watermark", command=add_watermark)
upload_button.pack(pady=20)

root.mainloop()