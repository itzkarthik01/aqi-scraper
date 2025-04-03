import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL of AQI website
url = "https://www.aqi.in/"
csv_file = "E:/Dw/aqi_data.csv"

try:
    while True:  # Infinite loop to run every 60 seconds
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Locate AQI value
        aqi_element = driver.find_element(By.XPATH, "//span[@title]")
        aqi_value = aqi_element.text.strip()
        
        # Get timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append data to CSV
        with open(csv_file, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, aqi_value])

        print(f"✅ Data saved: {timestamp}, AQI: {aqi_value}")

        # Wait for 60 seconds before next fetch
        time.sleep(60)

except KeyboardInterrupt:
    print("⏹️ Script stopped manually.")

finally:
    driver.quit()
