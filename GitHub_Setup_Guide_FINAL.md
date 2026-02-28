# GitHub Setup Guide

Complete step-by-step instructions to get your Federal Grant Compliance Framework online.

## Step 1: Create GitHub Account

If you don't have a GitHub account yet:

1. Go to **github.com**
2. Click **"Sign up"**
3. Enter email: damoah.dao@gmail.com
4. Create password
5. Username: damoahdao-cyber (already taken if you have an account)
6. Verify your email

**If you already have an account:** Just sign in at github.com

## Step 2: Create New Repository

1. Click the **"+"** icon (top right corner)
2. Select **"New repository"**
3. Fill in these exact details:
   - **Owner:** damoahdao-cyber
   - **Repository name:** `federal-grant-compliance-framework`
   - **Description:** "Open-source framework for nonprofit federal grant compliance - helping organizations manage $1.2 trillion in annual federal funding"
   - **Public:** ✅ Check this (required for open source)
   - **Add a README file:** ✅ Check this (you'll replace it)
   - **Add .gitignore:** None
   - **Choose a license:** None (we have custom license)
4. Click **"Create repository"**

You now have an empty repository at:
`https://github.com/damoahdao-cyber/federal-grant-compliance-framework`

## Step 3: Upload Core Files

### Replace the Auto-Generated README

1. On your repository page, click on **"README.md"**
2. Click the **trash can icon** (🗑️) to delete it
3. Scroll down, commit the deletion
4. Now click **"Add file"** → **"Upload files"**
5. Drag and drop **README_FINAL.md** from your computer
6. **IMPORTANT:** Rename it before uploading:
   - When you drag it, GitHub shows the filename
   - Click "rename" and change to just **README.md** (remove the _FINAL part)
7. Add commit message: "Add framework README"
8. Click **"Commit changes"**

### Upload Other Core Files

1. Click **"Add file"** → **"Upload files"**
2. Drag these files:
   - CONTRIBUTING_FINAL.md → rename to **CONTRIBUTING.md**
   - CODE_OF_CONDUCT_FINAL.md → rename to **CODE_OF_CONDUCT.md**
   - LICENSE_FINAL → rename to **LICENSE** (no extension)
3. Commit message: "Add contributing guidelines and license"
4. Click **"Commit changes"**

## Step 4: Create Folder Structure

GitHub doesn't allow empty folders, so we create folders by adding files into them.

### Create Research Folder

1. Click **"Add file"** → **"Create new file"**
2. In the name field, type: `research/README.md`
   - The `research/` part creates the folder
3. Add this content:
```markdown
# Research Foundation

This folder contains the theoretical and empirical foundation for the Federal Grant Compliance Framework.

## Published Research

- [Federal Grant Compliance Framework: An Open-Source Knowledge Commons Approach](FGCF_journal_article.md) - Full research article with methodology, theoretical framework, and evaluation design.

## Related Publications

*Additional publications will be listed here as they become available.*
```
4. Commit the file

### Upload Research Article

1. Click into the `research/` folder
2. Click **"Add file"** → **"Upload files"**
3. Upload **FGCF_journal_article.md**
4. Commit

### Create Framework Folder

1. From the main repository page, click **"Add file"** → **"Create new file"**
2. Type: `framework/README.md`
3. Add this content:
```markdown
# Framework Components

The Federal Grant Compliance Framework is organized into 7 domains addressing documented compliance challenges.

## Status

- ✅ Domain 1: Financial Management & Reporting (COMPLETE)
- 🔄 Domain 2: Compliance Policies & Procedures (IN DEVELOPMENT)
- 🔄 Domain 3: Eligibility Verification & Program Management (IN DEVELOPMENT)
- 🔄 Domain 4: Reporting & Performance Management (IN DEVELOPMENT)
- 🔄 Domain 5: Subrecipient Monitoring (IN DEVELOPMENT)
- 🔄 Domain 6: Audit Readiness & Internal Controls (IN DEVELOPMENT)
- 🔄 Domain 7: Training & Capacity Building (IN DEVELOPMENT)

## Using the Framework

Each domain folder contains:
- Comprehensive guide document
- Templates and tools
- Implementation instructions
- Examples and case studies

Start with Domain 1 if you're new to the framework.
```
4. Commit

### Create Other Folders

Repeat the process above for:

**Templates folder:**
```
File: templates/README.md
Content: 
# Templates & Tools

Excel spreadsheets, Word templates, and other practical tools.

Organized by framework domain.
```

**Implementation folder:**
```
File: implementation/README.md
Content:
# Implementation Guide

Step-by-step guidance for adopting the framework in your organization.

*Coming soon*
```

**Docs folder:**
```
File: docs/README.md
Content:
# Documentation

Additional documentation including FAQ, glossary, and quick-reference guides.

*Coming soon*
```

## Step 5: Add Topics (Tags)

1. From your main repository page, find **"About"** section (right side)
2. Click the **⚙️ gear icon**
3. Add these topics (type and press Enter after each):
   - `nonprofit`
   - `federal-grants`
   - `compliance`
   - `grants-management`
   - `open-source`
   - `knowledge-commons`
4. Click **"Save changes"**

## Step 6: Create Placeholder Files

### CHANGELOG.md

1. Create file: **CHANGELOG.md** (in root)
2. Content:
```markdown
# Changelog

All notable changes to the Federal Grant Compliance Framework will be documented here.

## [0.1.0-alpha] - 2026-02-XX

### Added
- Initial framework structure
- Domain 1: Financial Management & Reporting (complete)
- Research foundation and theoretical framework
- Core documentation (README, CONTRIBUTING, CODE_OF_CONDUCT, LICENSE)

### In Development
- Domains 2-7 guides and templates
- Implementation guide
- Training materials
```

### CONTRIBUTORS.md

1. Create file: **CONTRIBUTORS.md** (in root)
2. Content:
```markdown
# Contributors

Thank you to everyone who has contributed to the Federal Grant Compliance Framework!

## Project Lead

- **David Amoah Oduro** - Gulf of Maine Research Institute - Framework development, research design

## Contributors

*Contributors will be listed here as the project grows.*

---

Want to be listed here? See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved!
```

## Step 7: Your Repository is Live!

Your repository is now at:
**https://github.com/damoahdao-cyber/federal-grant-compliance-framework**

### What You Have:
```
federal-grant-compliance-framework/
├── README.md                    ✅
├── CONTRIBUTING.md              ✅
├── CODE_OF_CONDUCT.md           ✅
├── LICENSE                      ✅
├── CHANGELOG.md                 ✅
├── CONTRIBUTORS.md              ✅
├── research/
│   ├── README.md                ✅
│   └── FGCF_journal_article.md  ✅
├── framework/
│   └── README.md                ✅
├── templates/
│   └── README.md                ✅
├── implementation/
│   └── README.md                ✅
└── docs/
    └── README.md                ✅
```

## Step 8: Enable Discussions (Optional)

This creates a forum where people can ask questions.

1. Go to **Settings** (top tab)
2. Scroll to **"Features"** section
3. Check ✅ **"Discussions"**
4. A "Discussions" tab appears on your repository

## Step 9: Share Your Repository!

Post on LinkedIn:
```
Excited to announce I've published an open-source Federal Grant Compliance 
Framework based on implementation science research! 

Built to help nonprofits manage compliance with the $1.2 trillion in annual 
federal grants. Everything is free under Creative Commons license.

Framework: https://github.com/damoahdao-cyber/federal-grant-compliance-framework
Research Article: [add link to your research folder]

Looking for nonprofits interested in pilot testing. DM me if interested!

#nonprofit #grants #opensource #compliance #research
```

## Next Steps

1. **This week:** Upload Domain 1 materials as you create them
2. **This month:** Create 3-5 Excel templates
3. **Next month:** Recruit 2-3 pilot testers
4. **Ongoing:** Build out Domains 2-7

## Common Tasks

### Add a New File
1. Navigate to the folder
2. Click "Add file" → "Upload files" or "Create new file"
3. Add/upload, commit

### Edit a File
1. Click on the file
2. Click pencil icon (✏️) 
3. Make changes
4. Scroll down, commit

### Delete a File
1. Click on the file
2. Click trash icon (🗑️)
3. Commit the deletion

## Troubleshooting

**Q: I don't see README.md displaying on my main page**  
A: Refresh the page. GitHub auto-displays README.md.

**Q: How do I rename a file?**  
A: Click file → pencil icon → click filename at top to edit → save

**Q: Can I edit directly on GitHub?**  
A: Yes! Click any file, click pencil, edit, commit.

**Q: What if I make a mistake?**  
A: Click "History" on any file to see all versions. You can restore old versions.

## Need Help?

- **GitHub Docs:** https://docs.github.com
- **Markdown Guide:** https://www.markdownguide.org/basic-syntax/
- **Email David:** damoah.dao@gmail.com

---

**Your framework is now live and ready for the world!** 🎉
