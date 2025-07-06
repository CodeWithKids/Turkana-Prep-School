import os

def update_seo_meta():
    # The meta tags to add/update
    meta_description = '''    <meta content="Turkana Preparatory School offers a nurturing and creative learning environment for young children. Discover our unique approach to early childhood education." name="description">
    <meta content="Turkana Preparatory School, Lodwar Coding, kindergarten in Turkana, preschool, early education, child care, Lodwar, coding School, international school in turkana, STEM, Kids coding in Turkana, Turkana, preparatory school" name="keywords">
'''
    
    # Get all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if meta tags already exist
            if 'name="description"' in content and 'name="keywords"' in content:
                print(f"ℹ️ {file} already has SEO meta tags")
                continue
                
            # Find the head section
            head_start = content.find('<head>')
            if head_start == -1:
                print(f"⚠️ Couldn't find <head> in {file}")
                continue
                
            # Insert after <head>
            head_end = head_start + len('<head>')
            new_content = content[:head_end] + '\n' + meta_description + content[head_end:]
            
            # Write the updated content back to the file
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"✅ Updated SEO meta tags in {file}")
            
        except Exception as e:
            print(f"❌ Error updating {file}: {str(e)}")

if __name__ == "__main__":
    print("🔄 Updating SEO meta tags...")
    update_seo_meta()
    print("\n✅ SEO meta tags update complete!")
