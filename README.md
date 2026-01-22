# HeyGen Avatar Alert

**AI Avatar speaks text to replace standard UI alerts.**

---

## What This Does

- Uses HeyGen API to generate an AI avatar video
- Avatar speaks alert messages instead of text popups
- Gaming-style UI with visual effects

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Browser | Chrome / Edge / Firefox |
| Web Server | Optional (for testing locally) |
| HeyGen API Key | See below |

---

## How to Get HeyGen API Key

1. **Log In**: Sign in to your [HeyGen account](https://app.heygen.com/)
2. **Access Settings**: Click your profile icon (bottom-left corner)
3. **Navigate to API Section**:
   - Select **Settings** → **Subscriptions & API**
   - Select **HeyGen API** from sidebar
4. **Generate Token**: Click to view or generate a new API key
5. **Copy and Secure**: Save the token immediately

### Important Notes

| Note | Details |
|------|---------|
| Default Access | Free Trial includes 10 credits/month |
| Header Format | `X-API-KEY: YOUR_API_TOKEN` |
| API Credits | Separate from web-based credits |
| Streaming API | Use `create_token` endpoint for session tokens |

---

## Steps to Run

```bash
# 1. Clone the repo
git clone <repo-url>
cd HeyGen_Manager_Task

# 2. Navigate to demo folder
cd jquery_demo

# 3. Start local server
python -m http.server 8083

# 4. Open in browser
# http://127.0.0.1:8083/
```

---

## Output

### Initial UI
![Initial](jquery_demo/screenshots/01_initial_ui.png)

### Avatar Speaking
![Avatar](jquery_demo/screenshots/02_avatar_modal.png)

---

## Features

- ✅ Avatar video with audio
- ✅ Gaming-style UI (neon borders, animations)
- ✅ Typing animation for subtitles
- ✅ Audio visualizer indicator

---

## Project Structure

```
HeyGen_Manager_Task/
├── README.md
├── .gitignore
└── jquery_demo/
    ├── index.html          # Main HTML file with UI
    ├── avatar_alert.js     # jQuery & JavaScript logic
    ├── real.mp4           # Avatar video file
    └── screenshots/       # UI screenshots
```

## Technologies Used

- **HTML5**: Structure and markup
- **jQuery**: DOM manipulation and event handling
- **JavaScript**: HeyGen Avatar integration logic
- **CSS3**: Styling, animations, and gaming-style effects

