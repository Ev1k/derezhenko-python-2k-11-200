import bs4
import requests

response = requests.get("https://yandex.ru/pogoda/")
tree = bs4.BeautifulSoup(response.text, 'html.parser')
print("текущая погода: ", tree.find('.fact__temp-wrap').text.strip())
# print(tree.select_one('.link__feelings.fact__feelings').text.strip())

week = tree.find('.forecast-briefly__days').findAll('.forecast-briefly__day')
for day in week:
      date = day.find('.forecast-briefly__date').text.strip()
      temperature = day.find('.forecast-briefly__temp-day').text.strip()
      print(date, ": ", temperature)