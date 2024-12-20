from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to IDM Chrome extension
idm_extension_path = r"C:\Program Files (x86)\Internet Download Manager\IDMGCExt.crx"

# Configure ChromeDriver
options = webdriver.ChromeOptions()
options.add_extension(idm_extension_path)  # Add IDM extension
options.add_argument("--disable-blink-features=AutomationControlled")  # Optional: Make Selenium less detectable

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Read download links from a text file
with open("links.txt", "r") as file:
    links = [line.strip() for line in file.readlines()]

# Iterate over the links
for index, link in enumerate(links, start=1):
    print(f"Processing link {index}/{len(links)}: {link}")
    try:
        # Open the link
        driver.get(link)
        time.sleep(1)  # Wait for the page to load

        # Click the DOWNLOAD button (first click may open ads)
        try:
            download_button = driver.find_element(By.XPATH, '//button[text()="DOWNLOAD"]')  # Adjust as needed
            download_button.click()
            time.sleep(1)  # Handle ads or new tab
        except Exception as e:
            print(f"Error clicking button: {e}")
            continue

        # If required, click again for the actual download
        try:
            download_button = driver.find_element(By.XPATH, '//button[text()="DOWNLOAD"]')  # Adjust as needed
            download_button.click()
            time.sleep(3)  # Wait for the IDM extension to handle the download
        except Exception as e:
            print(f"Error clicking second button: {e}")
            continue

    except Exception as e:
        print(f"Error processing link {link}: {e}")
        continue

# Close the browser
driver.quit()
print("All links processed.")
