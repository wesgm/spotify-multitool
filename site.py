from flask import Flask
import gettracks as gt
import getartists as ga
top_tracks = gt.get_top_tracks()
top_artists = ga.get_top_artists()
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
	return "<h1>Home Page</h1>"
@app.route("/about")
def about():
	return "<h1>About:</h1>\n<p>Eventually: a flask app that tells you your top artists and tracks in a pretty way. I also plan on adding a way for users to input csv data of their spotify listening history and do some data analysis on it.</p>"
if __name__ == '__main__':
	app.run(debug=True)