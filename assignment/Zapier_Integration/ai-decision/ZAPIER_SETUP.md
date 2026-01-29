# ⚡ Master Guide: Zapier Setup

This guide assumes your server and ngrok are already running (which they are!).

**Your AI Link**: `YOUR_NGROK_URL` + `/decide`

---

## 🟢 Step 1: The Trigger
1.  Log in to Zapier and click **+ Create Zap**.
2.  Click the first block (**Trigger**).
3.  Search for **Webhooks by Zapier**.
4.  Event: **Catch Hook**.
5.  Click **Continue** (Skip "Child Key").
6.  **Copy the Webhook URL** provided by Zapier.
    *   *Action*: Open a new browser tab, paste that URL, add `?text=schedule%20meeting` at the end, and hit Enter. This sends a test signal.
7.  Go back to Zapier and click **Test Trigger**.
    *   It should find the "Request". Click **Continue with selected record**.

---

## 🔵 Step 2: The Brain (AI)
1.  Click the second block (**Action**).
2.  Search for **Webhooks by Zapier**.
3.  Event: **POST**. click **Continue**.
4.  **Configure**:
    *   **URL**: `YOUR_NGROK_URL` + `/decide`
    *   **Payload Type**: `Json`
    *   **Data**:
        *   (Left Box): `text`
        *   (Right Box): Click and select **1. Catch Hook** -> **Text**.
    *   **Unflatten**: `Yes`.
5.  Click **Continue** -> **Test Step**.
    *   ✅ Success if you see: `decision: calendar` (or email/ignore).

---

## 🟣 Step 3: The Paths (Logic)
*Note: If you are on a Free Zapier plan, "Paths" might be locked. Use "Filter" instead or ask me for the free workaround.*

1.  Click **+ Add a Step**.
2.  Search for **Paths**.
3.  **Path A** (Rename to "Calendar"):
    *   **Rules**: Only continue if...
    *   **2. POST** -> **Decision** ... (Text) Exactly Matches ... `calendar`.
    *   **Action**: Google Calendar -> Quick Add Event -> Use the text from Step 1.
4.  **Path B** (Rename to "Email"):
    *   **Rules**: Only continue if...
    *   **2. POST** -> **Decision** ... (Text) Exactly Matches ... `email`.
    *   **Action**: Gmail -> Send Email -> Use the text from Step 1.

---
