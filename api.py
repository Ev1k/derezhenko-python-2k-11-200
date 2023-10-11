import requests

ip = input()
response = requests.post(f"http://ip-api.com/json/{ip}?fields=country")
if not (response.json().__contains__("country")):
    print("Такого IP не существует")
else:
    print(response.json()["country"])
