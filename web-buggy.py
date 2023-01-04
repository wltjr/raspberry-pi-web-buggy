#!/bin/bash
# Copyright 2020-2023 Florida State College at Jacksonville
# Author William L. Thomson Jr. <w@wltjr.com>
#
# Distributed under the terms of The GNU Public License v3.0 (GPLv3)

#Import flask
from flask import Flask, render_template, request, jsonify
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

# handle form submissions
@app.route('/action', methods=['POST'])
def submit():
	# get form data in json format
	data = jsonify(request.form).json

	# set variables from form elements
	action = data['action']
	speed_left = int(data['speed_left'])
	speed_right = int(data['speed_right'])

	# default to slowest speed
	speed = speed_left if speed_left < speed_right else speed_right

	# switch action form value
	if action == "Backward":
		robot.backward(speed)
	elif action == "Forward":
		robot.forward(speed)
	elif action == "Stop":
		robot.stop()

	return ("nothing")

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)

