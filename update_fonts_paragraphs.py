import os
import re

def update_fonts_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Update Google Fonts link to use only Montserrat with appropriate weights
        new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
        
        # Replace the existing Google Fonts link
        content = re.sub(
            r'<link[^>]*?href=["\']https://fonts\.googleapis\.com/css2[^"\']*?["\'][^>]*>',
            new_font_link,
            content
        )
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Updated fonts in {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error updating {file_path}: {str(e)}")
        return False

def main():
    # Get all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Update each HTML file
    for file in html_files:
        update_fonts_in_file(file)
    
    print("\n🎨 Fonts updated to Montserrat for all text!")

if __name__ == "__main__":
    main()
