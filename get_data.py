from github import Github
import mistune
import pandas as pd
import re
repository = github.get_repo("rweekly/rweekly.org")
contents = repository.get_contents("_posts")
# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub personal access token
# You can generate a token here: https://github.com/settings/tokens
token = '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'

# Create a Github instance with your token
github = Github(token)

def get_posts():
    data = []
    # Markdown parser
    markdown_parser = mistune.Markdown()
    text_list = []
    link_list = []
    line_list = []
    text_list_all = []
    content_list = []
    # Loop through the contents to extract and read Markdown files
    for content in contents:
        if content.type == "file" and content.name.endswith(".md"):
            # Read the content of the Markdown file
            file_content = content.decoded_content.decode('utf-8')
            lines = file_content.split('\n')

            # Extract and store text and link information from each line
            for line in lines:
                matches = re.search(r'\[([^]]+)\]\(([^)]+)\)', line)
                if matches:
                    text, link = matches.group(1, 2)
                    text_list.append(text)
                    link_list.append(link)
                    line_list.append(line)
                    content_list.append(content.name)
                else:
                    text_list_all.append(line)
                    #link_list.append(None)

