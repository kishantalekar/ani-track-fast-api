from bs4 import BeautifulSoup
import requests


def getSpotlight():
    try:

        url = "https://aniwatch.to/home"
        response = requests.get(url)

        spotlight = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            deslide_wrap = soup.find('div', {'class': "deslide-wrap"})

            swiper_slides = deslide_wrap.find_all(
                'div', {'class': 'swiper-slide'})
            try:
                for swiper_slide in swiper_slides:
                    img = swiper_slide.find(
                        'img', {'class': 'film-poster-img'})
                    img = img['data-src']

                    name = swiper_slide.find(
                        'div', {'class': 'dynamic-name'}).text.strip()

                    spotlight_number = swiper_slide.find(
                        'div', {'class': 'desi-sub-text'}).text.strip()
                    url = swiper_slide.find('div', {'class': 'desi-buttons'})
                    url = url.find(
                        'a', {'class': 'btn-secondary'})['href']

                    spotlight.append({
                        "img": img,
                        "name": name,
                        "spotlight_number": spotlight_number,
                        "url": url
                    })
            except Exception as e:
                print("error")
                print(e)
            finally:
                return spotlight

        else:
            return spotlight
    except Exception as e:
        print("failed to request ", e)
