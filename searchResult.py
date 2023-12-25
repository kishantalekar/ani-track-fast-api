from bs4 import BeautifulSoup
import requests


def getSearchResult(query: str):

    url = f"https://aniwatch.to/search?keyword={query}"

    response = requests.get(url)
    search_film_result = []
    if response.status_code == 200:
        print(response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')

        film_list_wrap = soup.find('div', {'class': 'film_list-wrap'})

        flw_items = film_list_wrap.find_all('div', {'class': 'flw-item'})

        for flw_item in flw_items:
            try:
                anime_name = flw_item.find(
                    'a', {'class': 'dynamic-name'}).text.strip()

                url = flw_item.find(
                    'a', {'class': 'dynamic-name'})['href'].strip()
                url = url.split('?')[0]

                image_source = flw_item.find(
                    'img', {'class': 'film-poster-img'})['data-src'].strip()

                type = flw_item.find(
                    'span', {'class': 'fdi-item'}).text.strip()

                search_film_result.append({
                    "anime_name": anime_name,
                    "url": url,
                    "image_source": image_source,
                    "type": type,
                })

            except Exception as e:
                print(f"Error processing an item: {e}")

        return search_film_result
    else:
        return []

    # debugging
    # for flw_item in search_film_result:
    #     print(f"\nanime name :{flw_item['anime_name']}")
    #     print(f"\nurl :{flw_item['url']}")
    #     print(f"\nimage_source :{flw_item['image_source']}")
    #     print(f"\ntype :{flw_item['type']}\n")
