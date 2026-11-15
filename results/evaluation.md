# Evaluation log

Notes on each experiment we run, newest will be at the bottom.

## How we evaluate

- Train/test split is done by book, so the model is always tested on books it hasn't seen
- Metric: accuracy, plus a confusion matrix to see which authors get mixed up
- Baselines:
  - random guessing across 6 authors ≈ 17% accuracy
  - always guessing the biggest author in the test set ≈ [ ]% (fairer bar since the data is unbalanced)

## Dataset

- 16 public-domain books from Project Gutenberg, 6 authors, all originally written in English
- Authors: Conan Doyle, Gilman, Charlotte Brontë, Anne Brontë, Shelley, Dickens
- Gutenberg header/licence removed; books split into 500-word chunks; leftover chunks shorter than 500 words dropped
- 3,503 chunks before filtering, [ ] after
- Test books (one per author): The Return of Sherlock Holmes, Herland, Shirley, Agnes Grey, Frankenstein, Great Expectations

**Known issues with the data:**
- Unbalanced: Charlotte Brontë has roughly 2.5x as many chunks as Gilman, because book lengths vary a lot
- Gilman's *Human Work* is non-fiction; all other books are fiction
- *The Yellow Wallpaper* is very short (~6,000 words)
- With Herland held out for testing, Gilman is trained only on The Yellow Wallpaper and Human Work, so the model learns mostly from her non-fiction and is tested on her fiction
- Charlotte and Anne Brontë only have 2 books each, so the model trains on just one book per sister
- *Mathilda* has more words than expected (~48,000); may include an editor's introduction (to check)
- Books span 1818–1915, so era may affect style as well as author

---

## Experiment 1 - 15 Nov 2026

**What we tried:** Baseline: can function-word frequencies identify the author of a 500-word passage?
**Features:** Rates of 93 function words per chunk (count ÷ chunk length), standardised with StandardScaler (fitted on training set only)
**Model:** Logistic regression (class_weight="balanced" to handle the imbalance, max_iter=1000)
**Result:** *not run yet*
**What we noticed:** 
**Next:** Confusion matrix and most important words per author