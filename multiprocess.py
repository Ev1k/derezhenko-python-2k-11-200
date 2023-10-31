import multiprocessing
import re

import bs4
import requests


def normalization(href, domain):
    parts = href.split("/")
    if "https:" in parts:
        return href
    return "https://" + domain + "/" + parts[-1]


def get_image_name(image_link):
    result1 = re.finditer("(http[s]{0,1}:)//([a-zA-Z\._\d-]+/)+([a-zA-Z\._\d-]+)", image_link)
    for itm in result1:
        image_name = itm.group(3)
    return image_name


def download_image(args):
    url_of_image, filename = args
    response = requests.get(url_of_image)
    with open("images/" + filename, "wb") as f:
        f.write(response.content)


site = "https://plusclub.net/stati/373-top-5-evropejskikh-stran-dlya-otdykha-vsej-semej/"
result = re.finditer("(http[s]{0,1}:)//([a-zA-Z\._\d]+)+/[a-zA-Z\._\d]+", site)
for item in result:
    protocol = item.group(1)
    domain = item.group(2)



if __name__ == "__main__":
    response = requests.get(site)
    tree = bs4.BeautifulSoup(response.content, 'html.parser')
    content = tree.select_one('div', {'class': 'entry-content'}).find_all('img')
    link_list = []
    for itm in content:
        link_list.append(normalization(itm['src'], domain))
    image_links = []
    for link in link_list:
        image_links.append(get_image_name(link))
    args_list = list(zip(link_list, image_links))
    with multiprocessing.Pool() as pool:
        print(list(pool.map(download_image, args_list)))