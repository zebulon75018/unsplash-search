# 🖼️ unsplash-search — Claude Code Skill

A Claude Code skill that searches for images on [Unsplash](https://unsplash.com) using their official API. Claude can fetch the best match or propose several options, then use the results to build HTML pages, galleries, or any visual content — all from a simple natural language prompt.

---

## ✨ Features

- 🔍 Search Unsplash images by natural language description
- 📦 Returns structured JSON with URLs, photographer info, dimensions, and more
- 🖼️ Supports fetching 1 image or multiple options at once
- 🐍 Zero dependencies — uses Python standard library only
- ⚡ Plugs directly into Claude Code's skill system

---

## 📋 Requirements

- [Claude Code](https://claude.ai/code) installed and configured
- Python 3.8+
- An [Unsplash Developer account](https://unsplash.com/developers) with an **Access Key**

---

## 📁 Skill Structure

```
unsplash-search/
├── SKILL.md                  # Skill definition (read by Claude Code)
└── scripts/
    └── unsplash_search.py    # Python script called by Claude
```

---

## 🚀 Installation

### 1. Clone or download this skill

```bash
# Clone the repo
git clone https://github.com/your-username/unsplash-search-skill.git

# Or just create the folders manually
mkdir -p ~/.claude/skills/unsplash-search/scripts
```

### 2. Copy the skill files

```bash
cp unsplash-search/SKILL.md ~/.claude/skills/unsplash-search/SKILL.md
cp unsplash-search/scripts/unsplash_search.py ~/.claude/skills/unsplash-search/scripts/unsplash_search.py

# Make the script executable
chmod +x ~/.claude/skills/unsplash-search/scripts/unsplash_search.py
```

### 3. Set your Unsplash API key

Add this line to your `~/.bashrc`, `~/.zshrc`, or equivalent shell config:

```bash
export UNSPLASH_ACCESS_KEY="your_access_key_here"
```

Then reload your shell:

```bash
source ~/.bashrc
```

> **Where to get an API key?**  
> Go to [unsplash.com/developers](https://unsplash.com/developers) → New Application → copy the **Access Key**.

### 4. Register the skill in Claude Code

Open (or create) `~/.claude/settings.json` and add the skill path:

```json
{
  "skills": [
    "~/.claude/skills/unsplash-search"
  ]
}
```

---

## 🧪 Testing the script directly

You can test the Python script from the terminal before using it inside Claude Code:

```bash
# Fetch the single best match
python ~/.claude/skills/unsplash-search/scripts/unsplash_search.py "snowy mountains"

# Fetch 5 results
python ~/.claude/skills/unsplash-search/scripts/unsplash_search.py "parisian café" --count 5
```

### Example JSON output

```json
{
  "query": "snowy mountains",
  "total_available": 9821,
  "returned": 1,
  "results": [
    {
      "id": "abc123",
      "description": "A breathtaking view of snow-capped peaks",
      "width": 5472,
      "height": 3648,
      "color": "#a8c0d6",
      "url_thumb": "https://images.unsplash.com/photo-...?w=200",
      "url_regular": "https://images.unsplash.com/photo-...?w=1080",
      "url_full": "https://images.unsplash.com/photo-...",
      "download_url": "https://unsplash.com/photos/abc123/download",
      "page_url": "https://unsplash.com/photos/abc123",
      "photographer": "Jane Doe",
      "photographer_url": "https://unsplash.com/@janedoe",
      "likes": 342
    }
  ]
}
```

---

## 💬 Claude Code — Prompt Examples

Once the skill is installed, use natural language inside Claude Code:

### Generate a single-image HTML page

```
Search for an image of "autumn forest" on Unsplash and create an HTML page
that displays it fullscreen with the photographer's name at the bottom.
```

### Build a gallery from multiple results

```
Find 6 images of "rainy city streets" on Unsplash and generate an index.html
gallery with a dark minimal style and a caption under each photo.
```

### Embed an image into an existing HTML template

```
Search for a "minimalist desk setup" image on Unsplash, take the first result,
and insert it as the hero background of this HTML: [paste your HTML here]
```

### Let Claude pick the best option

```
Use the unsplash-search skill to find 5 photos of "Japanese cherry blossom",
pick the one with the most likes, and build a full-page HTML with it.
```

---

## 🔧 Script Reference

```
usage: unsplash_search.py [-h] [--count COUNT] query

positional arguments:
  query          Image description to search for (e.g. "dog in the snow")

options:
  -h, --help     show this help message and exit
  --count COUNT  Number of images to return (default: 1, max: 30)
```

### Environment variable

| Variable | Required | Description |
|---|---|---|
| `UNSPLASH_ACCESS_KEY` | ✅ Yes | Your Unsplash API Access Key |

---

## ⚠️ Unsplash API Guidelines

This skill is intended for **testing and development** purposes (Demo plan on Unsplash).

- Demo plan allows **50 requests/hour**
- Images must credit the photographer (name + link to their profile)
- For production use, you must apply for **Production access** on the Unsplash Developer portal
- When displaying a photo, Unsplash recommends triggering the `download_url` endpoint to log the download — you can ask Claude to do this in your prompt

More info: [unsplash.com/documentation](https://unsplash.com/documentation)

---

## 📄 License

MIT — free to use, modify, and distribute.

---

## 🙏 Credits

Built as a Claude Code skill example.  
Photos provided by [Unsplash](https://unsplash.com) and their amazing photographer community.
