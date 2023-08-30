from flask import Flask, render_template, redirect
from flask import request
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route("/")
def index():
    listings = {'_id':'615f3911a6d569a7cd86c945',
 'url': 'https://www.cnbc.com/2021/10/04/here-are-the-five-most-valuable-college-majors-.html',
 'img': 'https://image.cnbcfm.com/api/v1/image/106885838-1621509859148-gettyimages-1318999756-vcg111330726320.jpeg?v=1633354738&w=929&h=523',
 'title': 'Here are the 5 most valuable — and 5 least valuable — college majors'}
    return render_template("index.html",listings=listings)

@app.route("/slides")
def slides():
    return render_template("slides.html")

@app.route("/job_cat")
def jm():
    return render_template("jobs_by_category_mw.html")
    

@app.route("/job_market")
def jc():
    return render_template("job_market_map_visual_mw.html")
    

@app.route("/salary")
def sa():
    return render_template("as_charts.html")

@app.route("/employment_info")
def ei():
    return render_template("as_map.html")

# @app.route('/salary_prediction',methods=['GET', 'POST'])
# def sp():
#     if request.method == 'POST':
#         names = request.form.to_dict()
#         skill=skill_check(names)
#         input=[names["titles"],names["size"],names["ownership"],names["industry"],names["sector"],names["state"],names["age"]]
#         input=input+list(skill.values())
#         input=input+[names["titles"],names["seniority"]]
#         df=pd.DataFrame([input],columns=['Job Title', 'Size', 'Type of ownership', 'Industry', 'Sector', 'State',
#        'Age', 'Python', 'R', 'SQL', 'AWS', 'Excel', 'GCP', 'Azure', 'Spark',
#        'PyTorch', 'TensorFlow', 'Tableau', 'Keras', 'NoSQL', 'Scikit-Learn',
#        'Machine_Learning', 'Hadoop', 'Scala', 'Data_Brick', 'Job',
#        'Seniority'])
#         pred=salary_category( model.predict(df)[0])
#         return render_template('salary_prediction_sj.html',pred=pred)
#     else:
#         return render_template('salary_prediction_sj.html')


if __name__ == "__main__":
    app.run(debug=True)
