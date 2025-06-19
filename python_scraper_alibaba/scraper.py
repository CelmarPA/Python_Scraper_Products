# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


# Ask the user to input the product they want to search
product = input("Enter the product name: ").strip().lower()

# Selenium browser configuration
options = Options()
options.add_argument("--start-maximized")  # Start the browser maximized
# options.add_argument("--headless")  # Optional: run without opening the browser window

# Initialize the Chrome browser using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the Alibaba website
url = "https://www.alibaba.com"
driver.get(url)

# Wait for the page to load (adjust if needed)
driver.implicitly_wait(5.0)

# Locate the search bar using XPath
search_bar = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[3]/div/div/div[1]/div[1]/input')

# Input the product name and submit the search
search_bar.send_keys(product)
search_bar.send_keys(Keys.ENTER)

# Wait for search results to load
driver.implicitly_wait(3.0)

# Get the HTML source of the loaded page
html = driver.page_source

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Select all product containers (change the selector if needed)
products = soup.select('div[class*="offer"]')

# Create an empty list to store product data
products_list = []

# Loop through each product container to extract data
for product in products:
    # Extract the product name
    name_tag = product.select_one("h2.search-card-e-title > a > span")
    name = name_tag.get_text(strip=True) if name_tag else "N/A"

    # Extract the product price
    price_tag = product.select_one("div.search-card-e-price-main")
    price = price_tag.get_text(strip=True) if price_tag else "N/A"
    # Clean encoding issues like non-breaking spaces and extra characters
    price = price.replace('\xa0', ' ').replace('Â', '').strip()

    # Extract the image URL
    img_tag = product.select_one("img.search-card-e-slider__img")
    img_url = img_tag["src"] if img_tag else "N/A"
    # Complete the URL if it starts with '//'
    img_url = "https:" + img_url if img_url.startswith("//") else img_url

    # Extract the product link
    link_tag = product.select_one("a.search-card-e-slider__link")
    product_link = link_tag["href"] if link_tag else "N/A"

    # Extract the minimum order quantity
    info_sale_tag = product.select_one("div.search-card-m-sale-features__item")
    minimum_order = info_sale_tag.get_text(strip=True) if info_sale_tag else "N/A"

    # Create a dictionary with the extracted data
    product_dict = {
        "name": name,
        "price": price,
        "minimum_order": minimum_order,
        "img_url": img_url,
        "product_link": product_link
    }

    # Append the dictionary to the list
    products_list.append(product_dict)

# Wait a moment (optional)
driver.implicitly_wait(3.0)

# Close the browser
driver.quit()

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(products_list)

# Save to CSV
df.to_csv('products_list_alibaba.csv', index=False, encoding='utf-8')
print("CSV file created successfully: products_list_alibaba.csv")

# Save to Excel
df.to_excel('products_list_alibaba.xlsx', index=False, engine='openpyxl')
print("Excel file created successfully: products_list_alibaba.xlsx")
