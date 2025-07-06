import os

def update_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Add Font Awesome if not present
        if 'fontawesome' not in content.lower():
            content = content.replace(
                '</title>',
                '</title>\n    <!-- Font Awesome -->\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">'
            )
        
        # Add back to top script before closing body tag
        if 'back-to-top.js' not in content:
            content = content.replace(
                '</body>',
                '    <!-- Back to Top Button -->\n    <script src="js/back-to-top.js"></script>\n</body>'
            )
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Updated {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error updating {file_path}: {str(e)}")
        return False

def main():
    # Get all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Update each HTML file
    for file in html_files:
        update_file(file)
    
    print("\n🚀 Back to top button added to all pages!")

if __name__ == "__main__":
    main()
