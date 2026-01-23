/**
 * Avatar Alert - Gaming Edition
 * HeyGen Avatar Integration with Sci-Fi UI
 * With Auto-Synced JSON Subtitle System
 */

// Configuration
const VIDEO_URL = "real.mp4";

// Subtitle state
let subtitles = [];
let currentSubtitleIndex = -1;

// --- MAIN ENTRY POINT ---
function showAvatarAlert(message) {
    console.log("Transmission initiated:", message);

    // Show loading state
    $("#status-msg")
        .html('Establishing connection<span class="loading-bar"></span>')
        .show();

    // API Call
    callHeyGenAPI(message)
        .then(function (videoUrl) {
            $("#status-msg").hide();
            renderAvatarVideo(videoUrl, message);
        })
        .catch(function (error) {
            $("#status-msg").html("Connection failed: " + error).css("color", "#ff3c3c");
            alert(message);
        });
}

// --- API LAYER ---
function callHeyGenAPI(textInput) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            textInput ? resolve(VIDEO_URL) : reject("No input");
        }, 1200);
    });
}

// --- RENDER VIDEO WITH AUTO-SYNCED SUBTITLES ---
function renderAvatarVideo(url, message) {
    // Get subtitle JSON path (same name as video but .json extension)
    const subtitleUrl = url.replace(/\.\w+$/, '.json');

    const videoHtml = `
        <video id="avatar-video" autoplay controls width="100%">
            <source src="${url}" type="video/mp4">
        </video>
    `;

    $("#video-container").html(videoHtml);
    $("#avatar-modal").css("display", "flex").hide().fadeIn(300);
    $("#subtitle-box").fadeIn(200);

    // Initialize subtitle display
    $("#subtitle-text").text("Loading subtitles...");
    $(".cursor").hide();

    // Load subtitles from JSON
    loadSubtitles(subtitleUrl);

    // Setup video event handlers
    const video = document.getElementById('avatar-video');
    if (video) {
        // Wait for video to be ready
        video.addEventListener('loadedmetadata', function () {
            console.log('Video loaded successfully');
            $("#subtitle-text").text("Ready to play...");
        });

        // Core subtitle sync - fires continuously as video plays
        video.addEventListener('timeupdate', updateSubtitleDisplay);

        video.addEventListener('play', () => {
            $("#audio-viz").css("opacity", "1");
            console.log('Video playing');
        });

        video.addEventListener('pause', () => $("#audio-viz").css("opacity", "0.3"));

        video.addEventListener('ended', () => {
            $("#audio-viz").css("opacity", "0.3");
            $("#subtitle-text").text("Session complete.");
        });

        // Error handling
        video.addEventListener('error', function (e) {
            console.error('Video error:', video.error);
            $("#subtitle-text").text("Video loading error - check console");
        });
    }
}

// --- LOAD SUBTITLES FROM JSON ---
function loadSubtitles(subtitleUrl) {
    fetch(subtitleUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Subtitle file not found: ${subtitleUrl}`);
            }
            return response.json();
        })
        .then(data => {
            subtitles = data;
            console.log('Subtitles loaded:', subtitles.length, 'entries');
            $("#subtitle-text").text("Subtitles ready...");
        })
        .catch(error => {
            console.warn('Could not load subtitles:', error);
            subtitles = [];
            $("#subtitle-text").text("Playing without subtitles");
        });
}

// --- AUTO-SYNC SUBTITLE SYSTEM (Core Logic) ---
function updateSubtitleDisplay() {
    const video = document.getElementById('avatar-video');
    if (!video || subtitles.length === 0) return;

    const currentTime = video.currentTime;

    // Find the subtitle that matches current video time
    const currentSubtitle = subtitles.find(
        s => currentTime >= s.start && currentTime <= s.end
    );

    if (currentSubtitle) {
        // Find index to check if it's a new subtitle
        const newIndex = subtitles.indexOf(currentSubtitle);

        if (newIndex !== currentSubtitleIndex) {
            currentSubtitleIndex = newIndex;
            displaySubtitleWithAnimation(currentSubtitle.text);
        }
    } else {
        // No subtitle active at this time
        if (currentSubtitleIndex !== -1) {
            currentSubtitleIndex = -1;
            $("#subtitle-text").text("");
        }
    }
}

// --- DISPLAY SUBTITLE WITH TYPING ANIMATION (AI Feel) ---
function displaySubtitleWithAnimation(text) {
    const $subtitleText = $("#subtitle-text");

    // Quick fade out
    $subtitleText.fadeOut(100, function () {
        // Start typing animation
        $subtitleText.text("").show();
        typeText(text, $subtitleText);
    });
}

// --- TYPING ANIMATION (Makes it feel like AI is speaking live) ---
function typeText(text, $element) {
    let i = 0;
    const speed = 30; // milliseconds per character

    // Clear any existing typing interval
    if (window.typingInterval) {
        clearInterval(window.typingInterval);
    }

    window.typingInterval = setInterval(() => {
        if (i < text.length) {
            $element.text($element.text() + text[i]);
            i++;
        } else {
            clearInterval(window.typingInterval);
        }
    }, speed);
}

// --- MODAL CONTROLS ---
$(document).ready(function () {
    $(".close-btn").click(closeModal);
    $("#avatar-modal").click(function (e) { if (e.target === this) closeModal(); });
    $(document).keydown(function (e) { if (e.key === "Escape") closeModal(); });
});

function closeModal() {
    const video = document.getElementById('avatar-video');
    if (video) {
        video.removeEventListener('timeupdate', updateSubtitleDisplay);
        video.pause();
    }

    // Clear typing animation
    if (window.typingInterval) {
        clearInterval(window.typingInterval);
    }

    // Reset state
    subtitles = [];
    currentSubtitleIndex = -1;
    $(".cursor").show();

    $("#avatar-modal").fadeOut(200, function () {
        $("#video-container").empty();
    });
}
