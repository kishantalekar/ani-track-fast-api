from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
# https://simkl.in/posters/14/1433436642a68e8d88_m.jpg


"""
<a class="countdown-content-trending-item has-poster poster-loaded" data-hot-percentage="0" data-instant="" data-poster="//simkl.in/posters/14/1471469974b7e44777_m.jpg" href="/2080726/dog-signal" style="--poster:url('//simkl.in/posters/14/1471469974b7e44777_m.jpg');--hot:'0'">
<countdown-content-trending-item-title>Dog Signal</countdown-content-trending-item-title>
<countdown-content-trending-item-desc>Episode 16</countdown-content-trending-item-desc>
<countdown-content-trending-item-countdown class="countdown" data-time="493099"></countdown-content-trending-item-countdown>
</a>
"""


def getCountdownItem(item):

    title = item.find("countdown-content-trending-item-title").text
    episode = item.find("countdown-content-trending-item-desc").text
    countdown = item.find(
        "countdown-content-trending-item-countdown")['data-time']

    img_url = item['data-poster']

    slug = item['href']

    if img_url:
        img_url = f"https:{img_url}"
    else:
        img_url = "https://simkl.in/posters/14/1433436642a68e8d88_m.jpg"

    return {"title": title, "img_url": img_url, "countdown": countdown, "episode": episode, "slug": slug}


def getCountDown(genre="trending"):
    url = "https://animecountdown.com"
    url = f"{url}/{genre}"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    page = urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')

    countdown_content_trending_items = soup.find(
        'countdown-content-trending-items')
    # print(countdown_content_trending_items)

    countdown_content_trending_items = countdown_content_trending_items.find_all(
        'a', {'class': 'countdown-content-trending-item'})

    cd_list = []
    for countdown_item in countdown_content_trending_items:
        # print(countdown_item)
        cd_list.append(getCountdownItem(countdown_item))

    return {'cdlist': cd_list}
