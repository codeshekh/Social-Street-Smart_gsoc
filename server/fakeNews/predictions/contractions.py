
import re

contraction_mapping = {
    "don't": "do not",
    "can't": "cannot",
    "i'm": "i am",
    "you're": "you are",
    "isn't": "is not",
    "it's": "it is",
    "they're": "they are",
    "we're": "we are",
    "won't": "will not",
    "wouldn't": "would not",
    "couldn't": "could not",
    "haven't": "have not",
    "hasn't": "has not",
    "i've": "i have",
}

def expand_contractions(text):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in contraction_mapping.keys()) + r')\b')
    return pattern.sub(lambda x: contraction_mapping[x.group(0)], text)
