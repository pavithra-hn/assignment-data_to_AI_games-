# Avatar Alert Proof of Concept (PoC)

This PoC demonstrates how to replace the standard browser `alert()` with a modern **Avatar Video Alert** using jQuery and the HeyGen API.

## Technical Approach

The implementation follows a strict **Event → API Call → Render** flow, making it easy to integrate into existing jQuery-based applications.

### 1. Replacement of Alert
Instead of calling `alert("Message")` which blocks the browser, we call `showAvatarAlert("Message")`. This function initiates an asynchronous process that doesn't freeze the UI.

### 2. The API Call Logic
We introduced a specific function `callHeyGenAPI(text)`:
- It accepts the alert text as input.
- It performs an **asynchronous request** (simulated in this demo, but replaced by `$.ajax` or `fetch` in production).
- It handles the "Loading" state, providing visual feedback to the user while the video is generated.
- It returns a **Video URL** once the API responds successfully.

### 3. jQuery Rendering
Once the API returns the URL, we use jQuery to update the UI:
- **Injection**: We dynamically create a `<video>` tag with the returned URL and inject it into the DOM: `$("#container").html(videoTag)`.
- **Display**: We use `$("#modal").fadeIn()` to smoothly show the result.

## Feasibility & API Limit
- **Free Validation**: This flow works with HeyGen's Video Generation API (even on free tiers).
- **Latency**: Generation takes time (30s+), so for instant alerts, we recommend using "Instant Avatars" (Streaming) or pre-caching common messages.
- **Mocking**: In this demo, the API call is mocked with a `setTimeout` to demonstrate the UI handling without hitting API rate limits or wait times.
