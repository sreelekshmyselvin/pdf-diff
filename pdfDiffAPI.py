# -*- coding: utf-8 -*-
"""
Created on 21/02/20 11:45 PM
@author : Sreelekshmy Selvin

"""
from flask import request, jsonify
from werkzeug.utils import secure_filename
import pdfdifferencefinder as differencefinder

ALLOWED_EXTENSIONS = {'pdf'}


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file1' not in request.files or 'file2' not in request.files:
			finalstatus = 'No file part'
			return jsonify(finalstatus)
		file1 = request.files['file1']
		file2 = request.files['file2']
		if file1.filename == '' or file2.filename == '':
			finalstatus = 'Two files needed for comparison'
			return jsonify(finalstatus)
		if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
			filename1 = secure_filename(file1.filename)
			filename2 = secure_filename(file2.filename)
			try:
				finalstatus = differencefinder.processPDF(filename1, filename2)
				return jsonify(finalstatus)
			except Exception as e:
				finalstatus = "Something went wrong"
				return jsonify(finalstatus)
