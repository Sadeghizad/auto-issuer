import os
import subprocess

# Path to the folder containing the .md issue files
issue_folder = "genius_issues"

# Loop through each .md file and create an issue using gh CLI
for filename in os.listdir(issue_folder):
    if filename.endswith(".md"):
        filepath = os.path.join(issue_folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                continue
            title = lines[0].strip("# \n")
            body = "".join(lines[1:]).strip()

            print(f"Creating issue: {title}")
            subprocess.run([
                "gh", "issue", "create",
                "--title", title,
                "--body", body,
                "--assignee", "@me"
            ])
