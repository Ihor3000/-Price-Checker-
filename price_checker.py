import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    url = "https://www.amazon.com/dp/B0DP3G4GVQ"
    driver.get(url)


    price_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
    )
    price = price_element.text.strip()


    title_element = driver.find_element(By.ID, "productTitle")
    title = title_element.text.strip()


    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    print(f"✅ Назва товару: {title}")
    print(f"💰 Поточна ціна: {price}")
    print(f"📅 Оновлено: {timestamp}")


    with open("/Users/igordanylenko/Desktop/Програмування/WEB-SCRAPING/nine/price.csv", mode="a", newline="\n", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, title, price])

except Exception as e:
    print(f"❌ Помилка: {e}")

finally:
    driver.quit()