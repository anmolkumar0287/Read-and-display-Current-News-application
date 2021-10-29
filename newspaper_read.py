
# Akhbaar padhke sunaao
import requests
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    time.sleep(2)
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=8bba43f5890a4dc6b9055fe0e760fda9"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        print(article['url'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")
