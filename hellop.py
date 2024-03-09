import os

# HTML template for a post
post_template = '''
<div class="post">
    <a href="{post_link}">
        <img class="thumbnail" src="{thumbnail_src}" alt="{thumbnail_alt}">
        <h2 class="title">{post_title}</h2>
    </a>
</div>
'''

# Function to insert a new post into index2.html at the specified location
def insert_new_post(post_title, thumbnail_src, post_link):
    # Load index2.html
    with open("index2.html", "r") as index_file:
        index_content = index_file.read()

    # Find the location to insert the new post
    insertion_index = index_content.find("<!-- Add more posts as needed -->")
    if insertion_index == -1:
        print("Error: Could not find insertion point in index2.html")
        return

    # Construct the new post HTML
    new_post = post_template.format(post_title=post_title, thumbnail_src=thumbnail_src, thumbnail_alt="", post_link=post_link)

    # Insert the new post into index_content
    index_content = index_content[:insertion_index] + new_post + index_content[insertion_index:]

    # Write updated content back to index2.html
    with open("index2.html", "w") as index_file:
        index_file.write(index_content)

# Function to create a new post.html page with the given content
def create_post_html(post_number, post_title, post_image, post_text):
    # Create post{number}.html file
    post_filename = f"post{post_number}.html"
    with open(post_filename, "w") as post_file:
        post_file.write(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{post_title}</title>
        <style>
        .container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .post {{
            text-align: center;
        }}
        img {{
            max-width: 50%;
            height: auto;
        }}
        </style>
    </head>
    <body>
        <div class="container">
        <div class="post">
            <img src="{post_image}" alt="{post_title}">
            <p>{post_text}</p>
        </div>
        </div>
    </body>
    </html>
    ''')
    return post_filename

# Function to find the next available post number
def find_next_post_number():
    i = 1
    while os.path.exists(f"post{i}.html"):
        i += 1
    return i

# Take inputs from the user
post_title = input("Enter the post title: ").strip()
thumbnail_src = input("Enter the thumbnail source URL: ").strip()
post_image = input("Enter the post image URL: ").strip()
post_text = input("Enter the post text: ").strip()

# Find the next available post number
next_post_number = find_next_post_number()

# Generate post_link
post_link = f"post{next_post_number}.html"

# Insert new post into index2.html
insert_new_post(post_title, thumbnail_src, post_link)

# Create post{number}.html page
created_post_filename = create_post_html(next_post_number, post_title, post_image, post_text)
print(f"Created new post: {created_post_filename}")
