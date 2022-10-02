import json

from flask import Flask

from utils import get_movie, get_movie_by_release_year, get_movie_for_age, get_movie_by_genre

app = Flask(__name__)


@app.route("/movie/<title>")
def get_movie_page(title):
    """Страница с краткой информацией о фильме по названию"""
    return app.response_class(
        json.dumps(get_movie(title), ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )


@app.route("/movie/<year_first>/to/<year_second>")
def get_movie_by_release_year_page(year_first, year_second):
    """Страница с фильмами указанного периода времени"""
    return app.response_class(
        json.dumps(get_movie_by_release_year(year_first, year_second), ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )


@app.route("/rating/<age>")
def get_movie_for_age_page(age):
    """Страница фильмов по возрастному рейтингу"""
    return app.response_class(
        json.dumps(get_movie_for_age(age), ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )

@app.route("/genre/<genre>")
def get_movie_by_genre_page(genre):
    """Страница с последними 10  фильмами по указанному жанру"""
    return app.response_class(
        json.dumps(get_movie_by_genre(genre), ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )


if __name__ == '__main__':
    app.run()
