import bs4
import requests

response = requests.get("https://yandex.ru/pogoda/")
tree = bs4.BeautifulSoup(response.text, 'html.parser')
print(response.status_code)
print(tree)

print("текущая погода: ", tree.select_one('.fact__temp-wrap').text.strip().strip())
# print(tree.select_one('.link__feelings.fact__feelings').text.strip())

week = tree.find('.forecast-briefly__days').findAll('.forecast-briefly__day')
for day in week:
      date = day.find('.forecast-briefly__date').text.strip()
      temperature = day.find('.forecast-briefly__temp-day').text.strip()
      print(date, ": ", temperature)