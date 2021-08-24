import flask
from flask import Flask, request
import urllib.request
import json
import urllib3
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import bs4 as bs
app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def recommend():
    print("Recommend Meet")
    model = pickle.load(open('../nlp_model.pkl','rb'))
    vectorizer = pickle.load(open('../transform.pkl','rb'))
    if(request.method == 'POST'):
        inputs = request.form.get("youtube")
        print(inputs)
        list_inputs = inputs.split(" ")
        list_inputs = [x.lower() for x in list_inputs]
        list_inputs = [x for x in list_inputs if x not in stopwords.words('english')]
        list_inputs = np.array(list_inputs)
        search_vector = vectorizer.transform(list_inputs)
        pred = model.predict(search_vector)
        print("Pred = ", pred)
        search_url = 'https://www.youtube.com/results?search_query='+inputs+'&sp=CAMSAhAB'
        search_url = search_url.replace(' ','+')
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
        headers = { 'User-Agent' : user_agent }
        http = urllib3.PoolManager()
        req = http.request("GET",search_url,headers = headers)
        html = req.data.decode('utf-8')
        soup = bs.BeautifulSoup(html,'lxml')
        #print(soup.prettify())
        myA = soup.find_all("a", {"id": "yt-simple-endpoint style-scope ytd-video-renderer"})
        print(myA)
    return flask.render_template('index.html', token="Hello Flask+React")
if __name__ == '__main__':
    app.run(debug=True)

