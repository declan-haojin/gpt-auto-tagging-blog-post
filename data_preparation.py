import os
import glob
import frontmatter
import re
import csv
import openai
import pandas as pd


# import tiktoken

# def num_tokens_from_string(string: str, encoding_name: str) -> int:
#     """Returns the number of tokens in a text string."""
#     encoding = tiktoken.get_encoding(encoding_name)
#     num_tokens = len(encoding.encode(string))
#     return num_tokens

# num_tokens_from_string("tiktoken is great!", "cl100k_base")



openai.api_key = "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"

folder_path = "/Users/haojin/Code/blog.haojin.li/source/_posts"
csv_file_path = "data.csv"

# Use glob to find all Markdown files in the folder and its subfolders
md_files = glob.glob(os.path.join(folder_path, '**/*.md'), recursive=True)

# Output the data to a CSV file
with open(csv_file_path, "w", newline="") as f:
    # Create a csv.writer object
    writer = csv.writer(f)

    # Iterate through each Markdown file and print its filename
    for file_path in md_files:
        with open(file_path, "r") as f:
            content = f.read()
        with open(file_path, "r") as f:
            post = frontmatter.load(f)
        # Split the content into front matter and body
        front_matter, body = content.split("---\n", 2)[1:]
        # Remove all images from the content
        image_pattern = re.compile(r"!\[.*?\]\(.*?\)")
        body = image_pattern.sub("", body)
        body = body.replace("<!--more-->", "") # Remove the "more" tag from the content
        body = re.sub(r'<\/?[^>]+>', '', body) # Remove HTML tags
        body = re.sub(r'^\s*[\r\n]', '', body, flags=re.MULTILINE) # Remove empty lines
        # Get the title
        title = post['title']
        text = title + body

        print(title + "...", end="")

        # Let GPT-3 generate the tags
        prompt = f'Generate top 10 English single-word blog tags separated by comma for this post: "${text}"'
        try:
            res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        except Exception as e:
            print("Failed!")
            continue
        res = res.choices[0].message['content']
        tags = res.split(", ")

        for tag in tags:
            writer.writerow([title, tag])
        print("Success!")


