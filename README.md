# SAN
This project aims to create social audio network for the blind, drivers or those who are bored of watching the screen. Users can hear the (authorized) individual voice of their friends to obtain what they share instead of looking the screen. To do this, we use Machine Learning to analyze individually auditory patterns and Audio Coding to change the common voice to the individual voice.

## Text to Voice (T2V)
Use supervised or unsupervised learning to group words which usually occur together and record voice of these group in order to make the speech smoother.
### Supervised - Deep Learning or Decision Trees:
The inputs are the given texts and corresponding speeches. Labels for input are pre-defined cluster. Output is MODEL predicts terms which usually occur together. Training is based on continuity of speech files and probabilities of term clustering.
### Unsupervised - Entropy or Bayesian network:
The inputs are tons of documents without speech. Outputs are TERMS which usually occur together. Training is based on the time of occurring of terms.
### Search 'CLOSE' terms
Because of the typing mistake, we can use Levenshtein distance to compare the input terms and the terms in Database. the ratio between Levenshtein distance and total possible operations is less than 20% (or distance is very small and the ratio is less than 50%) and difference of length of strings is not too different to the distance since difference between to strings should be modifying, not inserting or deleting.
### Stopwords removal
We can use tf-idf score to determine whether word is stopword. The higher tf-idf score is, the more likely stopwords are.

## Audio Coding (AC)
Use Audio Coding to change the standard voice to the individual voice learned from given voice patterns.
