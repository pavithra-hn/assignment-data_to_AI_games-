import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def take_screenshots():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=800,600")
    options.add_argument("--allow-file-access-from-files") # Crucial for local CSV reading

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Chrome setup failed: {e}")
        # Fallback to Edge could be added here but keeping simple for now
        return

    base_dir = os.path.abspath("jquery")
    output_dir = os.path.join(base_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)

    # Dictionary to define custom interactions if needed
    # Key: file number, Value: function(driver)
    interactions = {
        1: lambda d: d.find_element(By.ID, "btn").click(),
        2: lambda d: d.find_element(By.ID, "showBtn").click(),
        # 3 Toggle: default is visible, clicking hides it. Initial state is better? Or maybe show it is there.
        # 4 Fade: clicking hides it. Initial state better.
        # 5 SlideUp: clicking hides it. Initial state better.
        6: lambda d: d.find_element(By.ID, "addClassBtn").click(), # Adds highlight
        7: lambda d: d.find_element(By.ID, "removeClassBtn").click(), # Removes highlight. Initial has it. Both fine.
        8: lambda d: d.find_element(By.ID, "textBtn").click(),
        9: lambda d: d.find_element(By.ID, "htmlBtn").click(),
        10: lambda d: d.find_element(By.ID, "appendBtn").click(),
        # 11 Keyup: Needs input typing.
        11: lambda d: d.find_element(By.ID, "inputBox").send_keys("Hello jQuery"),
        # 12-15 depend on CSV. Just wait.
    }

    for i in range(1, 16):
        filename = f"p{i}.html"
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            print(f"Skipping {filename}, not found.")
            continue
            
        print(f"Processing {filename}...")
        try:
            driver.get(f"file:///{file_path}")
            time.sleep(1) # Wait for load/CSV
            
            if i in interactions:
                try:
                    interactions[i](driver)
                    time.sleep(0.5) # Wait for animation/update
                except Exception as e:
                    print(f"Interaction failed for {filename}: {e}")

            out_path = os.path.join(output_dir, f"code_{i}_output.png")
            driver.save_screenshot(out_path)
            print(f"Saved {out_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    driver.quit()

if __name__ == "__main__":
    take_screenshots()
