# HeyGen Avatar Alert System

This repository contains two implementations for replacing standard jQuery `alert()` popups with HeyGen AI Avatar videos.

## 📂 Repository Structure

### 1. `jquery_demo/` (Recommended Proof of Concept)
A lightweight, frontend-focused PoC that demonstrates the "Avatar Alert" flow:
- **Button Click** → **API Call** → **jQuery Rendering**
- Replaces `alert()` with a custom modal.
- Uses `avatar_alert.js` to manage the logic.
- **Usage:** Simply open `index.html` in a browser.

### 2. `python_implementation/` (Full Backend)
A complete Flask-based implementation that handles:
- API Key security (using `.env`).
- Proxying requests to HeyGen to avoid CORS.
- Advanced video generation handling.
- **Usage:** Run `python app.py` and navigate to `http://localhost:5000`.

## 🚀 Key Features
- **Video Generation:** Uses HeyGen's API to generate videos from text.
- **jQuery Integration:** Renders the resulting video in a seamless modal.
- **Female Voice/Avatar:** tailored to use specific female avatars and voices (e.g., Allison).

## ⚠️ Setup
1. Clone the repository.
2. For the Python version, create a `.env` file inside `python_implementation/` with:
   ```
   HEYGEN_API_KEY=your_key_here
   ```
3. For the jQuery demo, you can test `index.html` directly (Note: API calls are mocked in the JS for demo purposes due to browser CORS).
