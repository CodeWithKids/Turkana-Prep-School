import os

def update_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Add theme colors CSS link after style.css
        if 'theme-colors.css' not in content:
            content = content.replace(
                '<link href="css/style.css" rel="stylesheet">',
                '<link href="css/style.css" rel="stylesheet">\n    <!-- Theme Colors -->\n    <link href="css/theme-colors.css" rel="stylesheet">'
            )
        
        # Update navbar brand
        content = content.replace(
            '<a href="" class="navbar-brand font-weight-bold text-secondary" style="font-size: 50px;">\n                <i class="flaticon-043-teddy-bear"></i>\n                <span class="text-primary">KidKinder</span>',
            '<a href="index.html" class="navbar-brand font-weight-bold" style="font-size: 50px;">\n                <i class="flaticon-043-teddy-bear text-gold"></i>\n                <span class="text-primary">Turkana Prep</span>'
        )
        
        # Update join school/class buttons
        content = content.replace(
            '<a href="" class="btn btn-primary px-4">Join School</a>',
            '<a href="contact.html" class="btn btn-primary px-4">Join School</a>'
        )
        content = content.replace(
            '<a href="" class="btn btn-primary px-4">Join Class</a>',
            '<a href="contact.html" class="btn btn-primary px-4">Join Class</a>'
        )
        
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Updated {file_path}")
        return True
    except Exception as e:
        print(f"Error updating {file_path}: {str(e)}")
        return False

def main():
    html_files = [
        "team.html",
        "events.html",
        "gallery.html",
        "blog.html",
        "contact.html",
        "detail.html",
        "404.html"
    ]
    
    for file in html_files:
        if os.path.exists(file):
            update_file(file)
        else:
            print(f"Skipping {file} (not found)")

if __name__ == "__main__":
    main()
