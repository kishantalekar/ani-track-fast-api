from fastapi import FastAPI
from trendingList import getTrending
from featuredList import getFeatured
from searchResult import getSearchResult
from genreList import get_genre
from categoryList import get_categories
from getAnimeById import getAnimeById
from getScheduleList import getSchedules

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
