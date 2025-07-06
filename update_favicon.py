from PIL import Image
import os

def create_favicon():
    try:
        # Convert logo.jpeg to favicon.ico
        logo_path = 'img/logo.jpeg'
        output_path = 'favicon.ico'
        
        # Open the image
        img = Image.open(logo_path)
        
        # Create a square image by cropping to the smallest dimension
        width, height = img.size
        size = min(width, height)
        left = (width - size) / 2
        top = (height - size) / 2
        right = (width + size) / 2
        bottom = (height + size) / 2
        
        # Crop and resize to standard favicon size (16x16, 32x32, 64x64)
        img = img.crop((left, top, right, bottom))
        img = img.resize((64, 64), Image.Resampling.LANCZOS)
        
        # Save as .ico
        img.save(output_path, format='ICO', sizes=[(16, 16), (32, 32), (64, 64)])
        print(f"✅ Created favicon.ico from {logo_path}")
        return True
    except Exception as e:
        print(f"❌ Error creating favicon: {str(e)}")
        return False

def update_html_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    favicon_link = '    <link rel="icon" type="image/x-icon" href="favicon.ico">\n'
    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.readlines()
            
            # Find the head section and insert favicon link
            head_end = next(i for i, line in enumerate(content) if '</head>' in line)
            
            # Check if favicon already exists
            if not any('favicon' in line for line in content):
                content.insert(head_end, favicon_link)
                with open(file, 'w', encoding='utf-8') as f:
                    f.writelines(content)
                print(f"✅ Updated {file} with favicon link")
            else:
                print(f"ℹ️ {file} already has a favicon link")
                
        except Exception as e:
            print(f"❌ Error updating {file}: {str(e)}")

def main():
    print("🔄 Setting up favicon...")
    if create_favicon():
        update_html_files()
    print("\n✅ Favicon setup complete!")

if __name__ == "__main__":
    main()
