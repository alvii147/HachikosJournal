import os
from google.cloud import language_v1

def getSentiment(text):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"MyFirstProject-da5d6b04be74.json"
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    return sentiment.score, sentiment.magnitude

if __name__ == "__main__":
    score, mag = getSentiment("This is so annoying! I hate this! Why am I always suffering?!")
    print(score, mag)