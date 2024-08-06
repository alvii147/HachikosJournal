import requests
from hachikosjournal.config import HUGGINGFACE_API_URL, HUGGINGFACE_API_KEY


TWITTER_ROBERT_BASE_SENTIMENT_LATEST_MODEL = 'cardiffnlp/twitter-roberta-base-sentiment-latest'

def analyze_sentiment(text: str) -> tuple[float, float, float]:
    response = requests.post(
        f'{HUGGINGFACE_API_URL}/models/{TWITTER_ROBERT_BASE_SENTIMENT_LATEST_MODEL}',
        headers={
            'Authorization': f'Bearer {HUGGINGFACE_API_KEY}',
        },
        json={
            'inputs': text,
        },
    )
    response.raise_for_status()

    labels = {
        str(l['label']): float(l['score'])
        for l in response.json()[0]
    }

    positive, negative, neutral = labels['positive'], labels['negative'], labels['neutral']

    return positive, negative, neutral
