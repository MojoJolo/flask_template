# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, jsonify, request, url_for, session
from app import app
import json
import arrow


@app.route("/")
def index():
    return "Hello Brodie!"
