import os
import re

def update_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Add theme colors CSS link if not present
        if 'theme-colors.css' not in content:
            content = content.replace(
                '<link href="css/style.css" rel="stylesheet">',
                '<link href="css/style.css" rel="stylesheet">\n    <!-- Theme Colors -->\n    <link href="css/theme-colors.css" rel="stylesheet">'
            )
        
        # Update navbar brand
        content = re.sub(
            r'<a\s+href=["\']{0,1}[^"\'>]*["\']{0,1}\s+class=["\']navbar-brand[^"\']*["\']',
            '<a href="index.html" class="navbar-brand font-weight-bold" style="font-size: 50px;"',
            content
        )
        
        # Update navbar logo and title
        content = re.sub(
            r'<i class="flaticon-043-teddy-bear[^<]*</i>\s*<span class="[^"]*">[^<]*</span>',
            '<i class="flaticon-043-teddy-bear text-gold"></i>\n                <span class="text-white">Turkana Prep</span>',
            content
        )
        
        # Update join buttons
        content = content.replace(
            '<a href="" class="btn btn-primary',
            '<a href="contact.html" class="btn btn-primary'
        )
        
        # Update footer background
        content = content.replace(
            '<footer class="bg-dark',
            '<footer class="bg-dark bg-teal'
        )
        
        # Update primary buttons
        content = content.replace(
            'class="btn btn-primary"',
            'class="btn btn-primary btn-gold"'
        )
        
        # Update section titles
        content = content.replace(
            'class="section-title"',
            'class="section-title text-teal"'
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
    
    print("\n🎨 Theme update complete!")

if __name__ == "__main__":
    main()
