from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy 

def extract_features(words):
   return dict([(word, True) for word in words])

if __name__=='__main__':
   fileids_pos = movie_reviews.fileids('pos')
   fileids_neg = movie_reviews.fileids('neg')
   features_pos = [(extract_features(movie_reviews.words(
      fileids=[f])), 'Positive') for f in fileids_pos]
   features_neg = [(extract_features(movie_reviews.words(
      fileids=[f])), 'Negative') for f in fileids_neg]

threshold = 0.8
num_pos = int(threshold * len(features_pos))
num_neg = int(threshold * len(features_neg))
features_train = features_pos[:num_pos] + features_neg[:num_neg]
features_test = features_pos[num_pos:] + features_neg[num_neg:]
print('\nNumber of training datapoints:', len(features_train))
print('Number of test datapoints:', len(features_test))
classifier = NaiveBayesClassifier.train(features_train)
print('\nAccuracy of the classifier:', nltk_accuracy(
   classifier, features_test))
N = 15
print('\nTop ' + str(N) + ' most informative words:')
for i, item in enumerate(classifier.most_informative_features()):
   print(str(i+1) + '. ' + item[0])
   if i == N - 1:
      break
input_reviews = ['Why do these movies feel they need to include a bratty, spoiled, overbearing kid??',
                 'The ridiculous performance of Jaden Smith added annoyance to the empty script.',
                 'The movie starts off well enough, and then tries miserably to develop the characters and make us care for them.',
                 'The Bates role is absurd;',
                 "Cleese's role has virtually nothing to say this amazing encounter.",
                 "The military point of view is typical; as if there's only one area where the military is useful (I would expect nothing less from 'Hollywood').",
                 'There were some very interesting ideas (the sphere-like ship, the nanobots, the Gort acronym) and the effects were top notch, however Gort (the one thing the movie had going for it) was on screen for less then 10 minutes.',
                 "Keanu was perfectly cast and Connelly does a good job with what's given to her.",
                 'All in all, another flop of a remake. This actually makes the War of the Worlds remake shine.',
                 "I saw this movie in IMAX - if you're going to see it, find an IMAX theater.",
                 'Lastly, am I the only sick of seeing the same old New York back drop? I love New York City, but come on! Be original!.']

print("\nMovie review predictions:")
for review in input_reviews:
   print("\nReview:", review)
   probabilities = classifier.prob_classify(extract_features(review.split()))
   predicted_sentiment = probabilities.max()
   print("Predicted sentiment:", predicted_sentiment)
   print("Probability:", round(probabilities.prob(predicted_sentiment), 2))
