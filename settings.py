import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

# twitter api credentials
TWITTER_KEY = os.environ.get("TWITTER_KEY")
TWITTER_SECRET = os.environ.get("TWITTER_SECRET")