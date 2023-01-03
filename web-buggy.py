#!/bin/bash
# Copyright 2020-2023 Florida State College at Jacksonville
# Author William L. Thomson Jr.
#        w@wltjr.com
#
# Distributed under the terms of The GNU Public License v3.0 (GPLv3)

#Import flask
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

#Import time
import time

#Import the Robot file PYC
import Robot

#Create the trim variables
LEFT_TRIM    = 0
RIGHT_TRIM   = 0

#Create a instance with the trim values
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

@app.route('/')
def index():
	return render_template('index.html');

@app.route('/move_backward')
def move_backward():
	robot.backward(100)
	return ("nothing")

@app.route('/move_forward')
def move_forward():
	robot.forward(100)
	return ("nothing")

@app.route('/stop')
def stop():
	robot.stop()
	return ("nothing")

@app.route('/turn_left')
def turn_left():
	robot.left(100, 3)
	return ("nothing")

@app.route('/turn_right')
def turn_right():
	robot.right(100, 3)
	return ("nothing")

@app.route('/json')
def json():
    return render_template('json.html')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)

