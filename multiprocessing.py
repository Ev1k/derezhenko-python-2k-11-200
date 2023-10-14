import re
import bs4
import requests

def normalization(href, domen):
    regex = "//(([a-zA-Z\._\d]+)/)+[a-zA-Z\._\d]+"
    if re.match(f"{regex}",href):
        return "https:" + href
    elif domen not in href:
        return "https://" + domen + href
    else:
        return href


site = "https://plusclub.net/stati/373-top-5-evropejskikh-stran-dlya-otdykha-vsej-semej/"
result = re.finditer("(http[s]{0,1}:)//([a-zA-Z\._\d]+)+/[a-zA-Z\._\d]+", site)
for item in result:
    protocol = item.group(1)
    domen = item.group(2)
    print(domen, protocol)


response = requests.get(site)
tree = bs4.BeautifulSoup(response.content, 'html.parser')
content = tree.select_one('div', {'class': 'entry-content'}).find_all('img')
link_list = []
for itm in content:
    link_list.append(normalization(itm['src'], domen))
    print(normalization(itm['src'], domen), itm['src'])

