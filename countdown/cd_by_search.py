from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
# https://simkl.in/posters/14/1433436642a68e8d88_m.jpg


"""
<a class="countdown-content-trending-item has-poster poster-loaded" data-hot-percentage="" data-instant="" data-poster="//simkl.in/posters/89/89453959724b96d61_m.jpg" href="/1239415/han-solostar-wars-story" style="--poster:url('//simkl.in/posters/89/89453959724b96d61_m.jpg');">
<countdown-content-trending-item-title>Han Solo/Star Wars Story</countdown-content-trending-item-title>
<countdown-content-trending-item-desc>ona 2018-2018</countdown-content-trending-item-desc>
<countdown-content-trending-item-countdown class="countdown no-countdown" data-time="0"></countdown-content-trending-item-countdown>
</a>
"""


def getCountdownItem(item):
    title = "Han Solo/Star Wars Story"
    episode = "ona 2018-2018"
    slug = "/1239415/han-solostar-wars-story"
    img_url = "https://simkl.in/posters/14/1433436642a68e8d88_m.jpg"
    try:
        title = item.find("countdown-content-trending-item-title").text
        episode = item.find("countdown-content-trending-item-desc").text

        img_url = item['data-poster']

        slug = item['href']

        if img_url:
            img_url = f"https:{img_url}"
        else:
            img_url = "https://simkl.in/posters/14/1433436642a68e8d88_m.jpg"
    except:
        print('something went wrong')

    return {"title": title, "img_url": img_url,  "episode": episode, "slug": slug}


def getCountdownBySearchQuery(query):
    url = "https://animecountdown.com"
    query = query.replace(" ", "%")

    url = f"{url}/search?q={query}"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    page = urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')

    countdown_content_trending_items = soup.find(
        'countdown-content-trending-items')
    print(countdown_content_trending_items)

    countdown_content_trending_items = countdown_content_trending_items.find_all(
        'a', {'class': 'countdown-content-trending-item'})

    cd_list = []
    for countdown_item in countdown_content_trending_items:
        # print(countdown_item)
        cd_list.append(getCountdownItem(countdown_item))

    return {'searchList': cd_list}
