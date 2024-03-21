import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Ensure NLTK data is downloaded
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)


def clean_text(text):
    """Cleans the input text."""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+|@\S+|#\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9]+", " ", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(tokens)
