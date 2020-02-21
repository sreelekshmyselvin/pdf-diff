#-*- coding: utf-8 -*-
"""
Created on 21/02/20 11:58 PM
@author : Sreelekshmy Selvin

"""
from flask import Flask,request,jsonify
import pdfDiffAPI as up

app = Flask(__name__)


@app.route('/upload',methods=['POST'])
def main():
    resp = up.upload()
    return resp

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
