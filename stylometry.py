# A dictionary of all books and author so we don't need a different method for each
books = [
    # Arthur Conan Doyle
    {"author": "Conan Doyle", "title": "The Adventures of Sherlock Holmes",
     "url": "https://www.gutenberg.org/cache/epub/1661/pg1661.txt"},
    {"author": "Conan Doyle", "title": "The Memoirs of Sherlock Holmes",
     "url": "https://www.gutenberg.org/cache/epub/834/pg834.txt"},
    {"author": "Conan Doyle", "title": "The Return of Sherlock Holmes",
     "url": "https://www.gutenberg.org/cache/epub/108/pg108.txt"},

    # Charlotte Perkins Gilman
    {"author": "Gilman", "title": "The Yellow Wallpaper",
     "url": "https://www.gutenberg.org/cache/epub/1952/pg1952.txt"},
    {"author": "Gilman", "title": "Human Work",
     "url": "https://www.gutenberg.org/cache/epub/64098/pg64098.txt"},
    {"author": "Gilman", "title": "Herland",
     "url": "https://www.gutenberg.org/cache/epub/32/pg32.txt"},

    # Charlotte Brontë
    {"author": "Charlotte Bronte", "title": "Jane Eyre",
     "url": "https://www.gutenberg.org/cache/epub/1260/pg1260.txt"},
    {"author": "Charlotte Bronte", "title": "Shirley",
     "url": "https://www.gutenberg.org/cache/epub/30486/pg30486.txt"},

    # Anne Brontë
    {"author": "Anne Bronte", "title": "Agnes Grey",
     "url": "https://www.gutenberg.org/cache/epub/767/pg767.txt"},
    {"author": "Anne Bronte", "title": "The Tenant of Wildfell Hall",
     "url": "https://www.gutenberg.org/cache/epub/969/pg969.txt"},

    # Mary Shelley
    {"author": "Shelley", "title": "The Last Man",
     "url": "https://www.gutenberg.org/cache/epub/18247/pg18247.txt"},
    {"author": "Shelley", "title": "Mathilda",
     "url": "https://www.gutenberg.org/cache/epub/15238/pg15238.txt"},
    {"author": "Shelley", "title": "Frankenstein",
     "url": "https://www.gutenberg.org/cache/epub/84/pg84.txt"},

    # Charles Dickens
    {"author": "Dickens", "title": "A Tale of Two Cities",
     "url": "https://www.gutenberg.org/cache/epub/98/pg98.txt"},
    {"author": "Dickens", "title": "A Christmas Carol",
     "url": "https://www.gutenberg.org/cache/epub/24022/pg24022.txt"},
    {"author": "Dickens", "title": "Great Expectations",
     "url": "https://www.gutenberg.org/cache/epub/1400/pg1400.txt"},
]

# function to download 1 book

import requests

def download_books(url):
  text = requests.get(url).text
  start = text.find("*** START OF")
  start = text.find("\n", start)
  end = text.find("*** END OF")
  return text[start:end]

# for loop to get each book in the list to go through download function

for book in books:
  book["text"] = download_books(book["url"])
  print(book["title"], len(book["text"].split()), "words")


# split the text into words, then take words 0–500, 500–1000, and so on. Each chunk should become its own small dictionary holding the author, the title and the chunk text, all added to one big list.

def split_IntoChunks(text):
  words = text.split()
  chunks=[]
  for i in range(0,len(words), 500):
     chunk_words = words[i:i+500]
     chunks_text = " ".join(chunk_words)
     chunks.append(chunks_text)
  return chunks

all_chunks = []
for book in books:
  pieces = split_IntoChunks(book["text"])
  for piece in pieces:
    all_chunks.append({"author": book["author"], "title": book["title"], "text": piece})
print(len(all_chunks), "chunks in total")
all_chunks = [c for c in all_chunks if len(c["text"].split()) == 500]
print(len(all_chunks), "chunks after removing short ones")

# turn the list of chunks into a table              ← NEW
import pandas as pd                                 # ← NEW
df = pd.DataFrame(all_chunks)                       # ← NEW
print(df["author"].value_counts())                  # ← NEW


# function words: small, common words that don't depend on the story
function_word = ["the", "and", "a", "of", "to", "in", "that", "it", "is", "was",
                 "for", "on", "as", "with", "he", "his", "they", "i", "at", "by",
                 "this", "had", "not", "but", "from", "or", "have", "an", "which", "one",
                 "you", "were", "her", "all", "she", "there", "thereby", "their", "we", "him",
                 "been", "has", "are", "about", "who", "when", "if", "so", "no", "what",
                 "up", "out", "into", "than", "then", "them", "can", "only", "other", "its",
                 "some", "could", "these", "would", "may", "more", "most", "me", "your", "my",
                 "how", "any", "our", "upon", "after", "before", "down", "should", "must", "through",
                 "over", "between", "under", "because", "against", "during", "while", "where", "since", "until",
                 "unless", "although", "yet"]

print(len(function_word), "words")
print(len(set(function_word)), "unique words")

import re

def style_features(text):
    words = re.findall(r"[a-z]+", text.lower())
    features = {}
    for fw in function_word:
        features[fw] = words.count(fw) / len(words)
    return features

print(style_features(df["text"][0]))