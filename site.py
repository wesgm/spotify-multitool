from flask import Flask, render_template
import gettracks as gt
import getartists as ga
top_tracks = gt.get_top_tracks()
top_artists = ga.get_top_artists()
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', top_tracks = top_tracks, top_artists= top_artists)
@app.route("/about")
def about():
	return render_template('about.html')
#@app.route("/authorize")
#def authorize():


if __name__ == '__main__':
	app.run(debug=True) 