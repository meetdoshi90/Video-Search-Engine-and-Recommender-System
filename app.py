from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def mainpage():
    
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    
    search_params = {
        'key' : 'AIzaSyAUDcKdlgEXzTBxi1A9L0W7c7N0U4E5Sws',
        'q' : 'learn Ml',
        'part': 'snippet'

    }
    r=requests.get(search_url, params=search_params)
    print(r.text)


    return render_template('index.html')
    

@app.route("/analysispage")
def analysis():
    return render_template('')   


if __name__ == "__main__":
    app.run(debug=True)