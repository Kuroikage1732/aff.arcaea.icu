#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# (c)2021 .direwolf <kururinmiracle@outlook.com>
# Licensed under the MIT License.

from flask import Flask, render_template
from flask_pjax import PJAX


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["PJAX_BASE_TEMPLATE"] = "templates/pjax.html"

    @app.route('/')
    def root():
        return render_template('index.html')

    @app.route('/arc-cutter')
    def arc_cutter():
        return render_template('arc-cutter.html')
    
    @app.route('/arc-rain')
    def arc_rain():
        return render_template('arc-rain.html')

    @app.route('/arc-crease-line')
    def arc_crease_line():
        return render_template('arc-crease-line.html')
    
    @app.route('/timing-easing')
    def timing_easing():
        return render_template('timing-easing.html')

    @app.route('/timing-glitch')
    def timing_glitch():
        return render_template('timing-glitch.html')

    pjax = PJAX()
    pjax.init_app(app)

    return app