# -*- coding: utf-8 -*-
from random import shuffle

from flask import Flask, jsonify, request, render_template, redirect, url_for

from graphene import Graphene
from graphene.processor import Processor

# app = Flask(__name__, static_url_path='/lector_vector/static')
app = Flask(__name__, static_folder='static', static_url_path='')
graphene_ = Graphene()
proc_ = Processor()

@app.route('/')
def index():
    return "Hello World!"