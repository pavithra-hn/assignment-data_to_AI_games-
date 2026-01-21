/**
 * Avatar Alert - Gaming Edition
 * HeyGen Avatar Integration with Sci-Fi UI
 */

// Configuration
const VIDEO_URL = "real.mp4";

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

// --- RENDER VIDEO ---
function renderAvatarVideo(url, message) {
    const videoHtml = `
        <video id="avatar-video" autoplay controls width="100%">
            <source src="${url}" type="video/mp4">
        </video>
    `;

    $("#video-container").html(videoHtml);
    $("#avatar-modal").css("display", "flex").hide().fadeIn(300);
    $("#subtitle-box").fadeIn(200);

    // Typing effect
    $("#subtitle-text").text("");
    typeText(message, "#subtitle-text", 40);

    // Audio sync
    const video = document.getElementById('avatar-video');
    if (video) {
        video.addEventListener('play', () => $("#audio-viz").css("opacity", "1"));
        video.addEventListener('pause', () => $("#audio-viz").css("opacity", "0.3"));
        video.addEventListener('ended', () => {
            $("#audio-viz").css("opacity", "0.3");
            $(".cursor").css("animation", "none").css("opacity", "0");
        });
    }
}

// --- TYPING EFFECT ---
function typeText(text, selector, speed) {
    let i = 0;
    const $el = $(selector);

    (function type() {
        if (i < text.length) {
            $el.text($el.text() + text.charAt(i++));
            setTimeout(type, speed);
        }
    })();
}

// --- MODAL CONTROLS ---
$(document).ready(function () {
    $(".close-btn").click(closeModal);
    $("#avatar-modal").click(function (e) { if (e.target === this) closeModal(); });
    $(document).keydown(function (e) { if (e.key === "Escape") closeModal(); });
});

function closeModal() {
    const video = document.getElementById('avatar-video');
    if (video) video.pause();

    $("#avatar-modal").fadeOut(200, function () {
        $("#video-container").empty();
        $(".cursor").css("animation", "cursorBlink 0.7s infinite").css("opacity", "1");
    });
}
