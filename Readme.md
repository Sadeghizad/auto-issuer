# 🐍 GitHub Bulk Issue Importer (via GPT & gh CLI)

This script lets you **automatically create GitHub issues** from a folder of Markdown files — generated manually or using ChatGPT.

It uses the [GitHub CLI](https://cli.github.com/) to create each issue and assign it to you.

---

## ⚙️ Setup

### ✅ Requirements
- Python 3.x
- [GitHub CLI (`gh`)](https://cli.github.com/) installed & authenticated

```bash
gh auth login
```

---

## 📁 Folder Structure

Make sure you have this setup in your project directory:

```
Genius-clone/
├── genius_issues/                   # Folder containing .md issue files
│   ├── comment_section.md
│   ├── album_discovery_for_users.md
│   └── ...
├── github_bulk_issue_import.py     # This script
```

Each `.md` file must have:

- The **first line** as issue title (starts with `#`)
- The **rest** as the issue body

---

## 🚀 Usage

In the root of your repo (where the script and folder are placed), run:

```bash
python github_bulk_issue_import.py
```

It will:
- Loop through all `.md` files in `genius_issues/`
- Use the first line as the issue title
- Create the issue using:
```bash
gh issue create --title "..." --body "..." --assignee @me
```

---

## 💡 Recommended: Generating `.md` issues with ChatGPT

You can use ChatGPT to generate `.md` issue files automatically (like [this example](https://github.com/your-repo/issues)).

Simply:
- Ask GPT to format each issue in its own `.md` file
- Save them in the `genius_issues/` folder

---

## 🥪 Optional Features You Can Add
- Add labels: `--label "bug,ui,enhancement"`
- Set milestone: `--milestone "MVP"`
- Add to project board: `--project "UI Refactor"`

---

## 🧠 Credits

Script powered by `gh` CLI + GPT-powered planning.  
Developed for use with the **Genius Clone JavaFX project**.

