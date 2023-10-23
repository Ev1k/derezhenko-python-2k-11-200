import asyncio

import aiohttp
import bs4


def normalization(href, domain):
    parts = href.split("/")
    if "https:" in parts:
        return href
    return "https://" + domain + "/" + parts[-1]


def get_list(content):
    link_list = []
    for itm in content:
        link_list.append(normalization(itm['src'], 'plusclub.net'))
    return link_list


async def download_image(session, url):
    async with session.get(url) as response:
        filename = "images/" + url.split("/")[-1]
        with open(filename, "wb") as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)


async def main():
    url = 'https://plusclub.net/stati/373-top-5-evropejskikh-stran-dlya-otdykha-vsej-semej/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            tree = bs4.BeautifulSoup(html, 'html.parser')
            content = tree.select_one('div', {'class': 'entry-content'}).find_all('img')
            link_list = get_list(content)
            tasks = []
            for url in link_list:
                tasks.append(asyncio.ensure_future(download_image(session, url)))
            await asyncio.gather(*tasks)


asyncio.run(main())
