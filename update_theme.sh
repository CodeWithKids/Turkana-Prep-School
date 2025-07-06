#!/bin/bash

# List of HTML files to update
FILES=(
    "team.html"
    "events.html"
    "gallery.html"
    "blog.html"
    "contact.html"
    "detail.html"
    "404.html"
)

# Update each file
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        # Add theme colors CSS link
        sed -i '' '/<link href="css/style.css" rel="stylesheet">/a \
    <!-- Theme Colors -->\
    <link href="css/theme-colors.css" rel="stylesheet">' "$file"
        
        # Update navbar brand
        sed -i '' 's/<a href="" class="navbar-brand font-weight-bold text-secondary" style="font-size: 50px;">\s*<i class="flaticon-043-teddy-bear"><\/i>\s*<span class="text-primary">[^<]*<\/span>/<a href="index.html" class="navbar-brand font-weight-bold" style="font-size: 50px;">\
                <i class="flaticon-043-teddy-bear text-gold"><\/i>\
                <span class="text-primary">Turkana Prep<\/span>/g' "$file"
        
        # Update join school button
        sed -i '' 's/<a href="" class="btn btn-primary px-4">Join School<\/a>/<a href="contact.html" class="btn btn-primary px-4">Join School<\/a>/g' "$file"
        
        # Update join class button if it exists
        sed -i '' 's/<a href="" class="btn btn-primary px-4">Join Class<\/a>/<a href="contact.html" class="btn btn-primary px-4">Join Class<\/a>/g' "$file"
        
        echo "Updated $file"
    else
        echo "Skipping $file (not found)"
    fi
done
