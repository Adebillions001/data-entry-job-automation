#import all the modules needed for the project to run.
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import os

#Write all the constants that will be used for the project.
SF_RENTING_FORM = os.environ.get("MY_FORM")
ZILLOW_WEBSITE = "https://appbrewery.github.io/Zillow-Clone/"


#TODO 1: Scrape the website data using Beautiful Soup
request = requests.get(ZILLOW_WEBSITE)

soup = BeautifulSoup(request.text, "html.parser")
# print(soup.prettify())

cards = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")


link_cards = soup.find_all("a", class_="property-card-link")
href = [card["href"] for card in link_cards]

price_cards = soup.find_all("div", class_="StyledPropertyCardDataArea-fDSTNn")
price = [card.text.replace("\n", "").replace("+/mo", "") for card in price_cards]

edited_price = []
for p in price:
    if "/mo" in p:
        tupple = p.split("/")
        # print(tupple[0])
        edited_price.append(tupple[0])
    elif "+ 1bd" in p:
        replaced = p.split("+")
        edited_price.append(replaced[0])
    elif "+ 1 bd" in p:
        replace = p.split("+")
        edited_price.append(replace[0])
    else:
        edited_price.append(p)


address = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
address_text = [a.text.strip(" ").lstrip("\n").rstrip("\n").replace("  ", "") for a in address]


#TODO 2: Fill in the google form using Selenium.

#initialize the chrome browser.
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(SF_RENTING_FORM)
driver.implicitly_wait(20)

#Comb through the data gotten from BeautifulSoup.
for house_address, price, link in zip(address_text, edited_price, href):

    all_input = driver.find_element(By.XPATH, "//div[@class='Qr7Oae'][1]")
    property_input = all_input.find_element(By.XPATH, ".//input[@class='whsOnd zHQkBf']")
    property_input.send_keys(str(house_address))

    price_input = driver.find_element(By.XPATH, "//div[@class='Qr7Oae'][2]")
    price_box = price_input.find_element(By.XPATH, ".//input[@class='whsOnd zHQkBf']")
    price_box.send_keys(price)

    link_to_property = driver.find_element(By.XPATH, "//div[@class='Qr7Oae'][3]")
    link_to_property_box = link_to_property.find_element(By.XPATH, ".//input[@class='whsOnd zHQkBf']")
    link_to_property_box.send_keys(link)

    submit_button = driver.find_element(By.XPATH, "//span[@class='l4V7wb Fxmcue']")
    submit_button.click()

    submit_another_response = driver.find_element(By.LINK_TEXT, "Submit another response")
    submit_another_response.click()

    

print(f"Submitted a total of len{edited_price} forms.")
