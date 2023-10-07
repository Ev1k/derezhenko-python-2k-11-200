import requests
import bs4
import re

ip = input()
response = requests.get(f"http://ip-api.com/json/{ip}")
tree = bs4.BeautifulSoup(response.text, 'html.parser')
result = re.finditer(r"(message|\"country\":\"([a-zA-Z-]+)\")", str(tree), )

for item in result:
    if str(item.group(1)) == "message":
        print("Такого IP не существует")
        break
    print(item.group(2))