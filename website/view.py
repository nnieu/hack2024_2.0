from flask import Blueprint, render_template
from os import path 

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return render_template("home.html")

@view.route('/chatbox')
def chatbox():
    return render_template("chatbox.html")

@view.route('/chat')
def chat():
    return render_template("chat.html")