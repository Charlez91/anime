from Anime import  app
from flask import render_template
from Anime.models import *
from Anime.anime_request import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	season_anime = get_season_anime()
	return render_template('index.html', season_anime=season_anime)