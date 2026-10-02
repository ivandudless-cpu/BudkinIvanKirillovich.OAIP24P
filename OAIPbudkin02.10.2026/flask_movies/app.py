from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre" : "Фантастика",
        "description" : "Кино о будущем"
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre" : "Фантастика",
        "description" : "Кино про легендарного агента Нео"
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 9.9,
        "genre" : "Комедия",
        "description" : "Лучший фильм всех времён и народов!"
    },
    {
        "id": 4,
        "title": "Соник в Кино",
        "year": 2020,
        "rating": 8.4,
        "genre" : "Боевик",
        "description" : "Фильм по игровселеной про синего дикобраза"
    },
    {
        "id": 5,
        "title": "Девушки и танки: Фильм",
        "year": 2015,
        "rating": 8.9,
        "genre" : "Экшн",
        "description" : "Аниме-фильм по одноименному аниме-сериалу о танковых баталиях и милых девушках :3"
    }
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie.html", movie=movie)

    return "Фильм не найден", 404

if __name__ == "__main__":
    app.run(debug=True)
