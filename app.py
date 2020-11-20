from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'usafa1993'
# toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/story')
def display_story():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adj = request.args['adj']
    plural = request.args['plural']
    # return render_template("story.html", place=place, noun=noun, verb=verb, adj=adj, plural=plural)
    return render_template("story.html", place=place, noun=noun, verb=verb, adj=adj, plural=plural)

    # num = randint(1, 10)
    # return render_template("story.html", lucky_num=num)
