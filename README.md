
# 🔍 Alibaba Product Scraper with Selenium & BeautifulSoup

A Python-based web scraper that automates searching for products on Alibaba.com, extracts key product information such as name, price, minimum order, image URL, and product link, and saves the data into CSV and Excel formats.

---

## 🚀 Features

- 🔍 Automates product search on Alibaba.com
- 📦 Extracts product name, price, minimum order, image URL, and product link
- 📊 Saves the data into CSV and Excel (.xlsx) files

---

## ⚙️ How It Works

- The user inputs the desired product name.
- Selenium automates the search process on Alibaba.
- BeautifulSoup parses the HTML to extract product details.
- Pandas saves the extracted data into CSV and Excel files.

---

## 🧰 Technologies

- **Python 3**
- **Selenium** for browser automation
- **BeautifulSoup** for HTML parsing
- **Pandas** for data manipulation and file export
- **WebDriver Manager** for managing the Chrome WebDriver

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CelmarPA/Python_Scraper_Products
cd python_scraper_alibaba
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install selenium beautifulsoup4 pandas openpyxl webdriver-manager
```

### 3. Run the Script

```bash
python scraper.py
```

Follow the on-screen prompt to enter the product name you want to search.

---

## 📂 Project Structure

```
Python_Scraper_Products/
├── README.md                    # Project documentation
└── python_scraper_alibaba/
    ├── requirements.txt         # Python dependencies
    ├── scraper.py               # Main scraper script
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Celmar Pereira**

- [GitHub](https://github.com/CelmarPA)
- [LinkedIn](https://linkedin.com/in/celmar-pereira-de-andrade-039830181)
- [Portfolio](https://yourportfolio.com)

---

## 💬 Feedback

Contributions, suggestions, and feedback are always welcome. Feel free to open issues or submit pull requests!
