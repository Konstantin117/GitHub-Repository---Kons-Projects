

import requests
from bs4 import BeautifulSoup

page_url = 'https://www.amazon.com/Artillery-Sidewinder-Pre-Assembled-300x300x400-Ultra-Quiet/dp/B084ZH4313/ref=sr_1_4?dchild=1&keywords=3d+printers&qid=1586898151&sr=8-4'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

amazon_page = requests.get(page_url, headers=headers)


def price_check():

    soup = BeautifulSoup(amazon_page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text
    price = soup.find(id="priceblock_ourprice").get_text
    converted_price = price[0:3]

    print(converted_price)

    if(converted_price < 599):
            send_mail()

        print(original_price)
        print(title.strip())


def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('emial_address', 'ter-reewr-wert-e')

        subject = '3D printer price drop!!'
        body = 'Check out the new price drop on this accessory :)'
        msg = f"subject {subject}\n\n{body}"
        server.sendmail(
            'random@email.com',
            'email_Address',
            msg
        )

        print("The price change email has been updated and sent out!!")
        server.quit()







