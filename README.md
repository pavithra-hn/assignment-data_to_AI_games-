# HeyGen Avatar Alert with Auto-Synced Subtitles

AI-powered avatar video player with time-synchronized subtitles featuring a gaming-style UI.

---

## ✨ Features

- ✅ AI avatar video with audio
- ✅ **Auto-synced JSON subtitles** - Time-based captions that sync perfectly
- ✅ **Typing animation** - AI mentor feel (30ms/char)
- ✅ Gaming-style Sci-Fi UI (neon borders, animations)
- ✅ Audio visualizer indicator
- ✅ Professional subtitle styling with speaker identification

---

## 📦 Installation

### 1. Install Python Dependencies (for subtitle generation)
```bash
pip install -r requirements.txt
```

### 2. Install FFmpeg (required for Whisper)
```bash
# Windows
winget install ffmpeg

# macOS
brew install ffmpeg

# Linux
apt install ffmpeg
```

---

## 🚀 Quick Start

### 1. Start Local Server
```bash
cd jquery_demo
python -m http.server 8083
```

### 2. Open in Browser
```
http://localhost:8083/index.html
```

### 3. Click "Start Lesson"
Watch the video with auto-synced subtitles below!

---

## 📁 Project Structure

```
HeyGen_Manager_Task/
├── README.md
├── requirements.txt        # Python dependencies (Whisper)
├── .gitignore
└── jquery_demo/
    ├── index.html          # Main HTML with gaming UI
    ├── avatar_alert.js     # JavaScript with subtitle sync engine
    ├── real.mp4            # Video file
    ├── real.json           # Time-synced subtitle data (Whisper generated)
    └── screenshots/        # UI screenshots
```

---

## 🎬 How Subtitles Work

### Architecture:
```
[Video] → [JSON Subtitles] → [Time-Sync Engine] → [Typing Animation] → [UI Display]
```

### Subtitle Format (`real.json`):
```json
[
  { "start": 0.0, "end": 2.5, "text": "Hello! Welcome to your learning session." },
  { "start": 2.5, "end": 5.0, "text": "Great job! You have successfully completed" },
  { "start": 5.0, "end": 7.5, "text": "the Python basics module." }
]
```

### Sync Mechanism:
- Video's `timeupdate` event fires continuously
- JavaScript finds subtitle matching current video time
- Displays text with typing animation effect
- Auto-updates as video plays

---

## 📝 Adding Your Own Video

### Step 1: Add video file
```
jquery_demo/my_video.mp4
```

### Step 2: Create subtitle JSON (same name)
```
jquery_demo/my_video.json
```

### Step 3: Update video URL
In `avatar_alert.js` line 8:
```javascript
const VIDEO_URL = "my_video.mp4";
```

### Step 4: Refresh browser
Subtitles will auto-load and sync!

---

## 🤖 Auto-Generate Subtitles

### Using Whisper (Recommended):
```bash
pip install openai-whisper
whisper your_video.mp4 --model small --output_format json
```

### Using AssemblyAI:
```python
import assemblyai as aai
transcript = aai.Transcriber().transcribe("video.mp4")
# Returns JSON with timestamps
```

### Using YouTube:
1. Upload video (private)
2. Auto-generate captions
3. Download as JSON
4. Place in `jquery_demo/`

---

## 🎨 Customization

### Change Typing Speed
In `avatar_alert.js` around line 170:
```javascript
const speed = 30; // milliseconds per character (lower = faster)
```

### Modify UI Colors
In `index.html` CSS section:
```css
.speaker-name {
    color: #00ff88;  /* Change accent color */
}
```

---

## 🛠 Technologies

- **HTML5** - Structure and video player
- **jQuery** - DOM manipulation
- **JavaScript** - Subtitle sync engine
- **CSS3** - Gaming-style UI and animations
- **JSON** - Subtitle data format

---

## ⚙️ How It Works (Technical)

### 1. Video loads and plays
```javascript
renderAvatarVideo(videoUrl);
```

### 2. Subtitle JSON auto-loads
```javascript
const subtitleUrl = videoUrl.replace(/\.\w+$/, '.json');
fetch(subtitleUrl).then(data => subtitles = data);
```

### 3. Time-sync engine runs
```javascript
video.addEventListener('timeupdate', () => {
  const current = subtitles.find(
    s => currentTime >= s.start && currentTime <= s.end
  );
  if (current) displayWithAnimation(current.text);
});
```

### 4. Typing animation displays text
```javascript
function typeText(text) {
  let i = 0;
  setInterval(() => element.text += text[i++], 30);
}
```

---

## 📸 Screenshots

### Initial UI
![Initial](jquery_demo/screenshots/01_initial_ui.png)

### Video with Subtitles
![Avatar](jquery_demo/screenshots/02_avatar_modal.png)

---

## ✅ Verified Working

- ✓ Video loads and plays correctly
- ✓ Subtitles auto-load from JSON
- ✓ Perfect time synchronization
- ✓ Typing animation effect (AI feel)
- ✓ Clean gaming-style UI
- ✓ No console errors
- ✓ Works with any video + JSON pair

---

## 🎯 Key Benefits

- **Scalable** - Works with any number of videos
- **Maintainable** - JSON is easy to edit
- **Automated** - Can auto-generate from speech-to-text
- **Professional** - Smooth animations and modern UI
- **Portable** - Standard JSON format

---

