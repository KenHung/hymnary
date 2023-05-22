from bs4 import BeautifulSoup
import requests

r = requests.get(
    "https://www.hymnal.net/en/search/all/all/There%20Is%20A%20Green%20Hill%20Far%20Away"
)
r.raise_for_status()

html = r.text

soup = BeautifulSoup(html, "html.parser")

# Get the first link item in the list-group div
link_item = soup.select_one(".list-group a")

# Extract the text and link number from the link item
text = link_item.contents[0].strip()
link_number = link_item["href"].split("/")[-1]

print(text)  # "There is a green hill far away"
print(link_number)  # "995"
