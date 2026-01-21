/**
 * Avatar Alert Proof of Concept
 * 
 * Flow:
 * 1. User Trigger -> 2. Call API -> 3. Render Response via jQuery
 */

// Configuration
// This is the specific HeyGen Video ID we generated (Female Voice "Allison")
// In a real production app, this would be dynamic or cached.
const MOCK_VIDEO_URL = "https://resource.heygen.ai/video/32dda5d3ddd046662a3be639d44995329/1280x720.mp4";
// Note: If the above URL expires (HeyGen temporary URLs expire), use a placeholder for demo:
// const MOCK_VIDEO_URL = "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4";


// --- MAIN ENTRY POINT ---
function showAvatarAlert(message) {
    console.log("1. Avatar Alert Triggered with message:", message);

    // UI: Show loading state via jQuery
    $("#status-msg")
        .text("Connecting to HeyGen API...")
        .css("color", "#2563eb")
        .show();

    // --- STEP 1: API CALL (Async) ---
    // We call the API wrapper function with the text we want spoken.
    callHeyGenAPI(message)
        .then(function (videoUrl) {

            // --- STEP 2: RENDER RESPONSE (jQuery) ---
            console.log("3. API Response Received. Rendering video...");
            $("#status-msg").hide(); // Hide status

            renderAvatarVideo(videoUrl);

        })
        .catch(function (error) {
            console.error("API Call Failed:", error);
            $("#status-msg").text("Error: " + error).css("color", "red");
            alert("Fallback: " + message); // Graceful degradation
        });
}


// --- API LAYER ---
/**
 * callHeyGenAPI
 * Simulates (or performs) the asynchronous request to HeyGen.
 * Returns a Promise that resolves to the Video URL.
 */
function callHeyGenAPI(textInput) {
    console.log("2. Calling API with text:", textInput);

    return new Promise((resolve, reject) => {

        // SIMULATION OF API DELAY
        // In a real app, $.ajax or fetch would go here.
        // Example:
        // $.post('/api/generate-video', { text: textInput }, (data) => resolve(data.url));

        setTimeout(() => {
            // MOCK RESPONSE
            // We return a valid video URL simulating a successful generation.
            if (textInput) {
                // Return our pre-generated video for the demo
                resolve(MOCK_VIDEO_URL);
            } else {
                reject("No text provided");
            }
        }, 1500); // 1.5 second delay to show "Connecting..." state
    });
}


// --- VIEW LAYER (jQuery) ---
/**
 * renderAvatarVideo
 * Uses jQuery to construct the HTML and display the modal.
 */
function renderAvatarVideo(url) {
    // 1. Construct Video HTML dynamically
    const videoHtml = `
        <video autoplay controls width="100%" style="display:block;">
            <source src="${url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    `;

    // 2. Inject into DOM
    $("#video-container").html(videoHtml);

    // 3. Show Modal (Fade In)
    $("#avatar-modal").fadeIn(300);

    // 4. Show RPG Text Box
    $("#subtitle-box").fadeIn(300);
    $("#subtitle-text").text("Mission Update: Payment successful. Proceed.");
}


// --- UTILITIES ---
// Modal Close Logic
$(document).ready(function () {
    $(".close-btn, #avatar-modal").click(function (e) {
        if (e.target !== this && !$(e.target).hasClass("close-btn")) return;

        $("#avatar-modal").fadeOut(200);
        setTimeout(() => $("#video-container").empty(), 200); // Clear video source
    });
});
