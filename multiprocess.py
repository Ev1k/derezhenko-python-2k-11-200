import multiprocessing
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


def get_image_name(image_link):
    result1 = re.finditer("(http[s]{0,1}:)//([a-zA-Z\._\d-]+/)+([a-zA-Z\._\d-]+)", image_link)
    for itm in result1:
        image_name = itm.group(3)
    return image_name


def download_image(args):
    url, filename = args
    response = requests.get(url)
    with open("images/" + filename, "wb") as f:
        f.write(response.content)


site = "https://plusclub.net/stati/373-top-5-evropejskikh-stran-dlya-otdykha-vsej-semej/"
result = re.finditer("(http[s]{0,1}:)//([a-zA-Z\._\d]+)+/[a-zA-Z\._\d]+", site)
for item in result:
    protocol = item.group(1)
    domen = item.group(2)
    print(domen, protocol)

response = requests.get(site)
tree = bs4.BeautifulSoup(response.content, 'html.parser')
content = tree.select_one('div', {'class': 'entry-content'}).find_all('img')


if __name__ == "__main__":
    link_list = []
    for itm in content:
        link_list.append(normalization(itm['src'], domen))
    image_links = []
    for link in link_list:
        image_links.append(get_image_name(link))
    args_list = list(zip(link_list, image_links))
    with multiprocessing.Pool() as pool:
        print(list(pool.map(download_image, args_list)))