import os

def update_html_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Copy logo.jpeg to favicon.ico
    if os.path.exists('img/logo.jpeg'):
        with open('img/logo.jpeg', 'rb') as src:
            with open('favicon.ico', 'wb') as dst:
                dst.write(src.read())
        print("✅ Created favicon.ico from logo.jpeg")
    
    # Add favicon link to all HTML files
    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if favicon already exists
            if 'favicon' not in content:
                # Insert after <head>
                new_content = content.replace(
                    '<head>',
                    '<head>\n    <link rel="icon" type="image/x-icon" href="favicon.ico">',
                    1  # Only replace first occurrence
                )
                if new_content != content:
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ Updated {file} with favicon link")
                else:
                    print(f"ℹ️ Couldn't find <head> in {file} to add favicon")
            else:
                print(f"ℹ️ {file} already has a favicon link")
                
        except Exception as e:
            print(f"❌ Error updating {file}: {str(e)}")

if __name__ == "__main__":
    print("🔄 Setting up favicon...")
    update_html_files()
    print("\n✅ Favicon setup complete!")
