import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "http://books.toscrape.com/"

# Request 
response = requests.get(url)

# HTML parse 
soup = BeautifulSoup(response.text, "html.parser")

# Books find 
books = soup.find_all("article", class_="product_pod")

data = []

# Data extract 
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    
    clean_price = ''.join(ch for ch in price if ch.isdigit() or ch == '.')
    price_value = float(clean_price)

    # INR convert (approx)
    price_inr = round(price_value * 100, 2)

    data.append([title, f"₹{price_inr}"])


with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Title", "Price (INR)"])
    writer.writerows(data)

print(f"✅ Done! {len(data)} books saved in books_data.csv")