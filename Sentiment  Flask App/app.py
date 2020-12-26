
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import numpy as np
import unicodedata
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
model = tf.keras.models.load_model('model.h5')

app = Flask(__name__)

@app.route('/')


def get_news():


    #Loading Tokenizer
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    #Sentiment Prediction
    def predict_sentiment(txt):
        news = [txt]
        news = tokenizer.texts_to_sequences(news)
        news = pad_sequences(news,maxlen = 400, padding = 'post', truncating = 'post')
        score = model.predict(news)
        if (np.argmax(score,axis = 1) == np.array([1])):
            sentiment = "Positive"
        else:
            sentiment = "Negative"
        return sentiment


    #Himalayan times

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get('http://thehimalayantimes.com/category/nepal/', headers=headers)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    himTimes= []
    for h4_tag in soup.find_all('h4'):
        a_tag = h4_tag.find('a')
        title = a_tag.attrs['title']
        url = a_tag.attrs['href']
        result = requests.get(url, headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        text=[data.get_text() for data in soup.find_all("p") ]
        news_txt = "".join(text[2:4])
        news_sum = unicodedata.normalize("NFKD", news_txt)
        classify_news = title + "." + news_sum
        sentiment = predict_sentiment(classify_news)
        news=[title]
        news.append(url)
        news.append(news_sum)
        news.append(sentiment)
        himTimes.append(news)


    #Kathmandu Post

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get('https://kathmandupost.com/politics', headers=headers)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    kPost = []
    for a_tag in soup.find_all('a'):
        if a_tag.find('h3'):
            h3_tag = a_tag.find('h3').get_text()
            url = 'https://kathmandupost.com' + a_tag.attrs['href']
            result = requests.get(url, headers=headers)
            src = result.content
            soup = BeautifulSoup(src, 'lxml')
            text=[data.get_text() for data in soup.find_all("p") ]
            news_txt = "".join(text[:2])
            news_sum = unicodedata.normalize("NFKD", news_txt)
            classify_news = h3_tag + "." + news_sum
            sentiment = predict_sentiment(classify_news)
            news=[h3_tag]
            news.append(url)
            news.append(news_sum)
            news.append(sentiment)
            kPost.append(news)
    

    #republica nepal

    result = requests.get("https://myrepublica.nagariknetwork.com/category/politics")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    myRepublica = []
    for a_tag in soup.find_all('a'):
        if a_tag.find('h2'):
            h2_tag = a_tag.find('h2').get_text(strip=True)
            url = 'https://myrepublica.nagariknetwork.com' + a_tag.attrs['href']
            result = requests.get(url, headers=headers)
            src = result.content
            soup = BeautifulSoup(src, 'lxml')
            text=[data.get_text(strip=True) for data in soup.find_all("p") ]
            news_txt = "".join(text[3:5])
            news_sum = unicodedata.normalize("NFKD", news_txt)
            classify_news = h2_tag + "." + news_sum
            sentiment = predict_sentiment(classify_news)
            news=[h2_tag]
            news.append(url)
            news.append(news_sum)
            news.append(sentiment)
            myRepublica.append(news)

    tableheadings = ("News", "Sentiment")
    return render_template('index.html',himTimes = himTimes, kPost = kPost, myRepublica = myRepublica, tableheadings = tableheadings)

#export FLASK_ENV=development
#flask run