import sqlite3

# шаг 0
def get_data_by_sql(sql):
    """Возвращает информацию из базы данных по sql-запросу"""
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

        return result


# шаг 1
def get_movie(title):
    """Возвращает информацию о фильме по названию"""
    result = ""
    sql = f"""
                select title, country, release_year, listed_in as genre, description from netflix
                where title = '{title}'
                order by release_year desc limit 1
                """
    for i in get_data_by_sql(sql):
        result = dict(i)

    return result


# шаг 2
def get_movie_by_release_year(year_first, year_second):
    """Возвращает фильмы, выпущенные в указанный период времени"""
    result = []
    sql = f"""
                select title, release_year from netflix
                where release_year between {year_first} and {year_second}
                order by release_year desc limit 100
                """
    for i in get_data_by_sql(sql):
        result.append(dict(i))

    return result


# шаг 3
def get_movie_for_age(age):
    """Возвращает фильмы, соответсвующие категории возраста"""
    age_rating = {"children": ('G', 'G'), "family": ('G', 'PG', 'PG-13'), "adult": ('R', 'NC-17')}

    result = []

    sql = f"""
            select title, rating, description from netflix
            where rating in {age_rating.get(age)}
            """
    for i in get_data_by_sql(sql):
        result.append(dict(i))

    return result



# шаг 4
def get_movie_by_genre(genre):
    """Возвращает информацию о последних 10  фильмах по жанру"""
    result = []
    sql = f"""
                select title, description from netflix
                where listed_in like '%{genre}%'
                order by release_year desc limit 10
                """
    for i in get_data_by_sql(sql):
        result.append(dict(i))

    return result


# шаг 5
def get_actors(first_actor, second_actor):
    """Возвращает список актеров, играющих в паре с указанными больше 2 раз"""
    sql = f"""
                    select "cast" from netflix
                    where "cast" like '%{first_actor}%' and "cast" like '%{second_actor}%'
                    """

    names_dict = {}

    for i in get_data_by_sql(sql):
        result = dict(i)

        names = set(result.get('cast').split(", ")) - set([first_actor, second_actor])

        for name in names:
            names_dict[name.strip()] = names_dict.get(name.strip(), 0) + 1

    result = []
    for key, value in names_dict.items():
        if value >= 2:
            result.append(key)

    return result
# print(get_actors('Rose McIver', 'Ben Lamb'))
# шаг 6
def get_movies_by_criteria(type, release_year, genre):
    """Возвращает информацию о фильмах по указанным критериям"""
    result = []
    sql = f"""
            select title, description from netflix
            where type == "{type}"
            and release_year == {release_year}
            and listed_in == "{genre}"
                """
    for i in get_data_by_sql(sql):
        result.append(dict(i))

    return result
