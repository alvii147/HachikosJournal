import random
import nltk
from nltk.tokenize import sent_tokenize
from hachikosjournal.huggingface import analyze_sentiment


class Hachiko:
    COMPLIMENTS_DATA_FILE = 'data/compliments.txt'
    MOTIVATORS_DATA_FILE = 'data/motivators.txt'
    FILLERS_DATA_FILE = 'data/fillers.txt'

    def __init__(self):
        self._load_tokenizer()
        self._load_compliments()
        self._load_motivators()
        self._load_fillers()

    def talk(self, text: str) -> str:
        """
        Talk to Hachiko using full paragraph of text.
        """

        return self.chat(self._split_sentences(text)[-1])

    def chat(self, message: str) -> str:
        """
        Chat with Hachiko using message.
        """

        positive, negative, neutral = analyze_sentiment(message)
        response = (self._get_compliment, self._get_motivator, self._get_filler)[
            max(
                range(3),
                key=lambda i: (positive, negative, neutral)[i],
            )
        ]()

        return response

    def _load_tokenizer(self):
        """
        Download NLTK punkt sentence tokenizer.
        """

        nltk.download('punkt', quiet=True)

    def _load_compliments(self):
        """
        Load list of compliments.
        """

        with open(self.COMPLIMENTS_DATA_FILE, 'r') as f:
            self.COMPLIMENTS = [
                line.strip() for line in f.readlines()
                if len(line.strip()) > 0
            ]

    def _load_motivators(self):
        """
        Load list of motivators.
        """

        with open(self.MOTIVATORS_DATA_FILE, 'r') as f:
            self.MOTIVATORS = [
                line.strip() for line in f.readlines()
                if len(line.strip()) > 0
            ]

    def _load_fillers(self):
        """
        Load list of fillers.
        """

        with open(self.FILLERS_DATA_FILE, 'r') as f:
            self.FILLERS = [
                line.strip() for line in f.readlines()
                if len(line.strip()) > 0
            ]

    def _get_compliment(self) -> str:
        return random.choice(self.COMPLIMENTS)

    def _get_motivator(self) -> str:
        return random.choice(self.MOTIVATORS)

    def _get_filler(self) -> str:
        return random.choice(self.FILLERS)

    def _split_sentences(self, text: str) -> str:
        return sent_tokenize(text)
