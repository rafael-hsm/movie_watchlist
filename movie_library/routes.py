from flask import Blueprint, current_app, render_template, session, redirect, request, url_for

from movie_library.forms import MovieForm
from movie_library.models import Movie

from dataclasses import asdict

import uuid


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    movie_data = current_app.db.movie_collection.find({})
    movies_data_list = list(movie_data)
    
    for item in movies_data_list:
        print(item)
    
    movies = [Movie(**movie) for movie in movies_data_list]
    return render_template(
        "index.html",
        title="Movies Watchlist",
        movies_data=movies
    )


@pages.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()
    
    if form.validate_on_submit():
        movie = Movie(
            _id= uuid.uuid4().hex,
            title= form.title.data,
            director= form.director.data,
            year= form.year.data
        )
        
        current_app.db.movie_collection.insert_one(asdict(movie))
        
        return redirect(url_for('.index'))
    
    return render_template(
        'new_movie.html',
        title='Movies Watchlist - Add Movie',
        form=form
    )
    

@pages.get('/toogle-theme')
def toggle_theme():
    current_theme = session.get('theme')
    if current_theme == 'dark':
        session['theme'] = 'light'
    else:
        session['theme'] = 'dark'
    
    return redirect(request.args.get('current_page'))
        