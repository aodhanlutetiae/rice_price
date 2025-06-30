import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# url="https://www.amazon.co.jp/%E9%AD%9A%E6%B2%BC%E7%94%A3%E3%82%B3%E3%82%B7%E3%83%92%E3%82%AB%E3%83%AA-%E3%80%90%E5%8F%97%E6%B3%A8%E7%B2%BE%E7%B1%B3%E3%80%91%E3%80%9030%E5%B9%B4%E7%94%A3%E6%96%B0%E7%B1%B3%E3%80%91%E5%8E%B3%E9%81%B8%E9%AD%9A%E6%B2%BC%E7%94%A3%E3%82%B3%E3%82%B7%E3%83%92%E3%82%AB%E3%83%AA%E3%80%90%E7%B2%BE%E7%B1%B3%E3%80%915kg/dp/B01JKTZWAO/ref=sr_1_58?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=2HAHJVZYPQAWZ&dib=eyJ2IjoiMSJ9.QX4PCuE9h17p0iD6hR_LrxFahxInwE494j_Eh1Ejr4B7ZAHKg-Y4MD81dhc8oy76cKF6lFze0fL7ZsmNEhO6xAOZwO3lSS-VIA5Udg44HaamfbKWAyV505fUUSl-r7mR1eBSaAqfbguDyyuWG-Rj9HXYjF_F9kjUg_JfecmbJSRWH9bJ33QHZoxRXLa_GfMOtN-2Op1eVrggAMo0uq4HEWnPA865PevbpUaMXXzMZ5HnNRZGVe3BSzc1pT5i8ZMdJhrHOWAovEJ2ZSfS_znesUgYKyUJoLgWuXMHAvCnpRc.mnd0ggJAhGUTaP0UeZh4l24BmqUgtnSrMCnwuYkTDWU&dib_tag=se&keywords=%E7%B2%BE%E7%B1%B35%E3%82%AD%E3%83%AD&qid=1750344347&sprefix=%E7%B2%BE%E7%B1%B3%2B5%E3%82%AD%E3%83%AD%2Caps%2C369&sr=8-58&th=1"
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}
# res=requests.get(url, headers=header)

# print(res.text[:500])

# soup=BeautifulSoup(res.text, "html.parser")
# brand=soup.find("span", class_="a-size-large product-title-word-break").text.strip()
# price=soup.find("span", class_="a-price-whole").text

time=datetime.now()
formatted = time.strftime("%Y-%m-%d %H:%M:%S")

with open(test.csv, 'a') as f:
    f.write(formatted)

#export to CSV
# filename="amazon_rice_price.csv"
# with open(filename, mode='a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow([brand, price, time])
