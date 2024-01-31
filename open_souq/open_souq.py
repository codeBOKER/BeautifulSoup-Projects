"""
This code collect products from opensooq website as following.
    discrptiongit 
    price -- place 
    the link
"""
import requests
from bs4 import BeautifulSoup
for num_page in range(10):
    url = f"https://ye.opensooq.com/ar/find?PostSearch[categoryId]=5565&PostSearch[term]=%D8%A7%D9%8A%D9%81%D9%88%D9%86={num_page}"
    reaslut = requests.get(url)
    soup = BeautifulSoup(reaslut.content, "lxml")
    
    parts = soup.find_all(class_="flex flexNoWrap p-16 blackColor radius-8 grayHoverBg ripple boxShadow2 relative")

    for part in parts:
        #_____discrption______
        discrption = part.find(class_="font-20 breakWord overflowHidden").text
        re_discrption = discrption.replace("\n", " ")
        #_____price_____
        price = part.find(class_="postPrice ms-auto bold alignSelfCenter font-19")
        try:
            re_price = price.get_text()
        except AttributeError:
            re_price ="he did not put the price"
        #_____place______
        place = part.find(class_="bold")
        re_place = place.get_text()
        #_____link_________
        link = part.get("href")
        re_link = f"http:/{link}"

        print(re_discrption)
        print("\n" + re_price + "in" + re_place)
        print("click here to take a view")
        print(re_link)
        print("______________--------_________")

#codeBOKAR