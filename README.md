# spam-sentiment-analysis
Code to to spam analysis on emails and sentiment analysis on IMDB reviews.

The analysis involves the implementation of NAIVE BAYES model with smoothing to do spam analysis on a large email data
set and also do sentiment analysis on IMDB reviews.
File nblearn.py uses the training labeled data to generate a model and nbclassify.py uses the genrated model to do
classification of test data.
NAIVE BAYES is then compared to SVM and MegaM models in terms of Precision, recall and F1 score values.
