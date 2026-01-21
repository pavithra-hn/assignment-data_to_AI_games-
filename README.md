# HeyGen Avatar Alert System

This repository contains a Proof of Concept (PoC) for replacing standard jQuery `alert()` popups with HeyGen AI Avatar videos.

## 📂 Repository Structure

### `jquery_demo/` (The Solution)
A lightweight, frontend-focused PoC that demonstrates the "Avatar Alert" flow:

1. **Button Click** (User Action)
2. **API Call** (Async request to HeyGen)
3. **jQuery Rendering** (Injects video into a custom modal)

**Key Features:**
- Replaces legacy `alert()` with a modern avatar modal.
- Uses `avatar_alert.js` to separate logic from UI.
- Demonstrates the exact flow requested: API Call -> jQuery Render.

## 🚀 How to Run
1. Navigate to the `jquery_demo` folder.
2. Open `index.html` in any web browser.
3. Click **"Show Avatar Alert"**.

## 📝 Implementation Details
See `jquery_demo/POC_EXPLANATION.md` for a deeper technical breakdown of the architecture.
