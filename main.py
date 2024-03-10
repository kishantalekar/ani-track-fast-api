from fastapi import FastAPI


from aniwatch.trendingList import getTrending
from aniwatch.featuredList import getFeatured
from aniwatch.genreList import get_genre
from aniwatch.getAnimeById import getAnimeById
from aniwatch.searchResult import getSearchResult
from getScheduleList import getSchedules
from aniwatch.getSpotlightList import getSpotlight
from aniwatch.categoryList import get_categories

from countdown.countdown_by_genre import getCountDown
from countdown.cd_by_search import getCountdownBySearchQuery


# to start the server run the following command
# uvicorn main:app --reload

app = FastAPI()


@app.get('/')
def getRoot():
    return {"for more info go to your yourserverurl/docs"}


@app.get('/trending')
def get_trending():
    return {"trending_data": getTrending()}


@app.get('/featured')
def get_featured():
    return getFeatured()


@app.get('/search/{query}')
def search(query: str):
    return getSearchResult(query)


@app.get('/genre/{genre}')
def get_genre_data(genre: str):
    return get_genre(genre)


@app.get('/categories/{category}')
def get_category_data(category: str):
    return get_categories(category)


@app.get('/anime/{query}')
def get_anime_by_id(query: str):
    return getAnimeById(query)


@app.get('/schedules')
def get_schedules():
    return getSchedules()


@app.get('/spotlight')
def get_spotlight():
    return getSpotlight()


@app.get('/countdown/{query}')
def get_countdown_genre(query: str):
    return getCountDown(query)


@app.get("/countdown/search/{query}")
def get_countdown_search(query: str):
    return getCountdownBySearchQuery(query)
