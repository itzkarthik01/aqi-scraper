from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Set timeouts
driver.set_page_load_timeout(30)  # Max wait time for page load
driver.set_script_timeout(30)  # Max wait time for scripts

# URL of the AQI website
url = "https://www.binance.com/"  # Update with the correct AQI data source

try:
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    # Example: Scrape an element (update selector as needed)
    data_element = driver.find_element(By.XPATH, "//div[@class='your-element-class']")
    scraped_data = data_element.text

    # Save to CSV
    csv_file = "aqi_data.csv"
    df = pd.DataFrame({"AQI Data": [scraped_data]})
    df.to_csv(csv_file, mode="a", index=False, header=False)

    print("AQI data successfully scraped and saved!")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()
