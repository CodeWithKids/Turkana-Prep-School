import os

def update_seo_meta():
    # The meta tags to add/update
    meta_tags = '''    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="Turkana Preparatory School offers a nurturing and creative learning environment for young children. Discover our unique approach to early childhood education." name="description">
    <meta content="Turkana Preparatory School, Lodwar Coding, kindergarten in Turkana, preschool, early education, child care, Lodwar, coding School, international school in turkana, STEM, Kids coding in Turkana, Turkana, preparatory school" name="keywords">
'''
    
    # Get all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find and replace the meta tags section
            viewport_start = content.find('<meta content="width=device-width')
            if viewport_start == -1:
                print(f"⚠️ Couldn't find viewport meta tag in {file}")
                continue
                
            # Find the end of the meta tags section
            viewport_end = content.find('>', viewport_start) + 1
            description_start = content.find('<meta content="Free HTML Templates" name="description">')
            
            if description_start != -1:
                # If old description exists, replace it along with viewport
                description_end = content.find('>', description_start) + 1
                new_content = content[:viewport_start] + meta_tags + content[description_end:]
            else:
                # If only viewport exists, insert after it
                new_content = content[:viewport_end] + '\n' + meta_tags[meta_tags.find('\n')+1:] + content[viewport_end:]
            
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
