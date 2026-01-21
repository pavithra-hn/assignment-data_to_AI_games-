# Heygen API Documentation & Avatar-Based Alert Replacement
**Prepared by:** Pavithra H N  
**Date:** 21 January 2026

## HeyGen API Overview
HeyGen provides AI-driven avatar video and audio services via REST and streaming APIs. Developers can programmatically generate realistic talking-avatar videos from text or audio, choose from many avatars/voices, and even stream interactive avatars in real time[1][2]. With HeyGen, you can build dynamic experiences such as virtual assistants or training demos where a digital avatar speaks your content. 

A Quick Start guide explains that the HeyGen API lets you “build videos programmatically with AI avatars and voices, translate them… or even power real-time streaming avatars”[3]. All API calls require an API key (found in HeyGen settings) sent as `X-API-KEY` header[4][5].

## Key Features

### Avatar Video Generation (Static)
Convert text into fully rendered avatar videos. HeyGen supports many photorealistic avatars and human-like voices. For example, the **Create Avatar Video (V2)** endpoint takes your text (up to ~5,000 characters) and chosen avatar/voice, and returns a downloadable MP4[1][6].

### Real-Time Interactive Avatars
Beyond batch video, HeyGen offers a **Streaming API** for live avatars. This uses WebRTC to display a talking avatar in real time. You can send text via WebSockets and the avatar will speak it immediately[7][2]. Key features include real-time streaming, text-to-speech integration, event-driven updates (avatar start/stop talking), and session management[7].

### Text-to-Speech Integration
In both modes, avatars synchronize lip movements with speech. You can adjust voice settings (speed, pitch, emotion) and support 100+ languages. For streaming avatars, you literally “send text commands” to make them speak on-the-fly[7].

### Templates & Translation (Additional)
HeyGen also supports video templates (with placeholders for text/voice), video translation, and photo-to-avatar video. (See HeyGen docs for template APIs and multi-language features.)

## Getting Started

1. **Obtain an API Key**: Sign up for a HeyGen account and get an API token under Settings > API. Include this key in each request (`X-API-KEY: <your-key>`)[4][5]. Keep it secure (do not expose in client-side code).
2. **Experiment in Docs**: HeyGen provides an interactive API explorer and a Postman collection. You can try endpoints (such as Create Video or Streaming calls) right in the documentation by supplying your API key[8].
3. **Choose Avatars/Voices**: Use the **List Avatars (V2)** and **List Voices (V2)** endpoints to see available digital characters and voice models. Each avatar and voice has an ID to use in video requests.
4. **Consult Examples**: HeyGen docs include step-by-step guides (e.g. Create Avatar Videos (V2)) that walk through the process of selecting an avatar, posting the create-video request, and polling for completion[9][6].

## Core Capabilities

- **Avatar Video (Batch) API**: Send a POST to `/v1/videos/avatar` (or similar) with parameters like `avatar_id`, `voice_id`, and your script text. The service returns a `video_id`. You then poll `/v1/videos/avatar/{video_id}` until status is completed, and retrieve the video URL. Limits: text ≤5000 chars, free-tier max 720p[6]. (Generated URLs expire after ~7 days[10].)
- **Streaming (Interactive) API**: First create a streaming session token (POST `/v1/streaming.create_token`[11]), then start a session (POST `/v1/streaming.new`) to get a `session_id` and websocket URL. After calling POST `/v1/streaming.start`, your app connects (e.g. via HeyGen’s SDK or LiveKit) to receive the avatar video stream. To make the avatar speak, send text tasks (POST `/v1/streaming.task`) – the avatar will vocalize the text in real time[12]. The session can later be closed (`/streaming.close`).
- **Speech & Lip Sync**: Whether batch or streaming, HeyGen avatars lip-sync to the audio. In streaming mode, the SDK “allows them to speak, respond to commands… in real-time” and even emits events when the avatar starts/stops talking[7].
- **Advanced**: HeyGen also offers customizable background, transparent avatars (WebM), photo-to-avatar (generate videos from still images), and template-based personalization.

## Example Use Cases
- **Virtual Assistants & Training Simulations**: Embed a talking avatar in a web app or kiosk that guides users, answers questions, or provides walkthroughs. HeyGen’s low-latency streaming makes this feasible[2].
- **Marketing & Communications**: Generate explainer or announcement videos with a digital spokesperson reading dynamic content.
- **Multilingual Content**: Use the Video Translate API to dub or subtitle videos in other languages.
- **In-App Notifications**: Instead of a boring alert box, have an on-screen avatar read out important messages or instructions in context (our primary scenario).
- **Accessible Content**: Use avatar narration to deliver content instead of plain text.

## High-Level Workflow

1. **Configure and Authenticate**: Store your HeyGen API key (e.g. in environment variables). All API requests must include this key (e.g. `X-API-KEY` header)[5].
2. **Select Avatars/Voices**: Call GET `/v1/avatars` and GET `/v1/voices` to pick a character and voice ID.
3. **Generate Content**:
   - **Static Video**: Make a POST to `/v1/videos/avatar` with your text (≤5000 chars) and chosen avatar/voice. Receive a `video_id`, poll its status, and download the MP4 when ready[6].
   - **Interactive Stream**: Call POST `/v1/streaming.create_token` to get a session token, then POST `/v1/streaming.new` to start a session. Use POST `/v1/streaming.start` to begin the stream. On the client side, connect to the provided WebSocket/LiveKit URL. Send messages with POST `/v1/streaming.task`[12].
4. **Post-Processing**: For batch videos, you may want to store or cache them[10]. For streaming, manage session lifecycle.

## Example Code (Python)
Below is a simplified outline of using the streaming API in Python (using requests):

```python
import requests

api_key = "YOUR_HEYGEN_API_KEY"
headers = {"X-API-KEY": api_key}

# 1. Create a streaming session token
token_res = requests.post("https://api.heygen.com/v1/streaming.create_token", headers=headers)
session_token = token_res.json()["access_token"]

# 2. Start a new avatar session (choose an avatar)
session_res = requests.post(
    "https://api.heygen.com/v1/streaming.new",
    headers={"Authorization": f"Bearer {session_token}", "Content-Type": "application/json"},
    json={"avatar_id": "YOUR_AVATAR_ID", "version": "v2"}
)
session_id = session_res.json()["data"]["session_id"]

# 3. Initiate the session connection
requests.post(
    "https://api.heygen.com/v1/streaming.start",
    headers={"Authorization": f"Bearer {session_token}", "Content-Type": "application/json"},
    json={"session_id": session_id}
)

# 4. Send the message to speak (e.g. instead of alert)
task_res = requests.post(
    "https://api.heygen.com/v1/streaming.task",
    headers={"Authorization": f"Bearer {session_token}", "Content-Type": "application/json"},
    json={"session_id": session_id, "text": "Alert: operation completed!", "task_type": "REPEAT"}
)
```

## Limitations and Constraints
- **Latency (Batch vs Real-Time)**: Static video generation is not instantaneous. Only the Streaming API offers near-real-time speech.
- **Character Limit**: Avatar video text is capped (≈5000 chars)[6].
- **Quality and Resolution**: Free API tier caps output at 720p[6].
- **Session Expiry**: Streaming sessions have time limits. Download URLs expire after ~7 days[10].
- **Integration Complexity**: The real-time avatar feature uses WebSockets/LiveKit. Embedding the avatar video in an app requires additional client-side logic.
- **Costs and Quotas**: Heavy usage will require a paid subscription[15].

## Replacing jQuery Alert with Avatar Speech
**Support**: HeyGen does support speaking dynamic text via avatars. Its Streaming API lets you send any text as a “task” and the avatar will speak it[12][13].

**Approach**: Rather than using an alert, trigger the avatar flow:
1. **Prepare the Avatar Session**: Have a streaming session ready.
2. **Send the Alert Text**: Call POST `/v1/streaming.task` with the alert text.
3. **End-to-End Flow**: A video element connected to HeyGen’s LiveKit stream will play the avatar.

**Feasibility**: This setup is feasible but more involved than a simple alert. It requires embedding HeyGen’s video stream in your UI.

**Conclusion**: HeyGen’s Streaming Avatar API can replace a jQuery alert with a speaking avatar. This yields a richer UX, though at the cost of integrating real-time video.

## Sources
[1] [6] [9] [10] [Create Avatar Videos (V2)](https://docs.heygen.com/docs/create-video)  
[2] [16] [Streaming API Overview](https://docs.heygen.com/docs/streaming-api)  
[3] [4] [5] [8] [15] [Quick Start](https://docs.heygen.com/docs/quick-start)  
[7] [14] [Streaming Avatar SDK](https://docs.heygen.com/docs/streaming-avatar-sdk)  
[11] [Create Session Token](https://docs.heygen.com/reference/create-session-token)  
[12] [Send Task](https://docs.heygen.com/reference/send-task)  
[13] [Streaming Avatar SDK API Reference](https://docs.heygen.com/docs/streaming-avatar-sdk-reference)  
[17] [Real-time synthesis for text to speech avatar - Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech-avatar/real-time-synthesis-avatar)  
[18] [AI Avatar: Talking Heads Presenters | Speaking Portrait](https://www.d-id.com/speaking-portrait/)  
[19] [Create a Free AI Text to Speech Avatar | 230+ TTS Avatars](https://www.synthesia.io/tools/text-to-speech-avatar)
