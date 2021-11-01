import unittest
import analyze1 as analyze
import json
import os

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

class TestSum(unittest.TestCase):
    def test_get_all_tweets(self):
        with open('twitter_timeline.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(analyze.get_all_tweets("Youtube"), data, "error")

    def test_analyze_text_entities(self):
        with open('analyze_text_entities.json', 'r') as f:
            data = json.load(f)
        file = open('tweet.json', 'r')
        text = file['text']
        self.assertEqual(analyze.analyze_text_entities(text), data, "error")


if __name__ == "__main__":
    unittest.main()

    