# Stylometry
Trying to work out who wrote a piece of text just from the writing style.

The idea is that authors use small common words (the, of, upon, which...) at fairly
consistent rates no matter what the story is about, so counting them should give a
kind of fingerprint for each author.

Still working on this, it's not finished yet.

## Books used

All from Project Gutenberg.

- Arthur Conan Doyle - Adventures, Memoirs and Return of Sherlock Holmes
- Charlotte Perkins Gilman - The Yellow Wallpaper, Human Work, Herland
- Charlotte Brontë - Jane Eyre, Shirley
- Anne Brontë - Agnes Grey, The Tenant of Wildfell Hall
- Mary Shelley - Frankenstein, The Last Man, Mathilda
- Charles Dickens - A Tale of Two Cities, A Christmas Carol, Great Expectations

I put both Brontë sisters in on purpose to see if the model can tell them apart.

## What it does so far

- downloads the books and cuts off the Gutenberg header/footer
- splits each book into 500 word chunks (drops the last short one)
- puts the chunks in a pandas dataframe
- counts how often each function word appears in a chunk

## To do

- [ ] train a classifier
- [ ] test on books it hasn't seen before
- [ ] see which authors get mixed up
- [ ] try other features like sentence length and punctuation

## Running it

```
pip install -r requirements.txt
python python stylometry.py
```

## Team

Made by Asra Arbabi and Aayushi Chauhan.
