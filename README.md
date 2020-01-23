Classifying Music by Sub-Genre
 
# Project Scope
For this project, a classification system was built to identify and arrange music by sub-genre.

Currently, Spotify has great functionality to recommend songs to its users. You can 

Music streaming services have revolutionised how we consume music. The services come with numerous perks, most notably instantaneuos access to music, without having to have it stored on your device.



However this problem comes at a price, we increasingly own less and less of the music we listen to. For most, this may not be a problem, but the lack of control of how this music is organised

Music is often generealise into wider genres, for ease of access and storage. These immutable labels, pre-determined by Spotify,   
Non-Western genres feel this the most, and are often over-generalised

Reggae was chosen as my parent genre, and I identified three sub-genres which the data will be split between. This genre was chosen because of a good domain knowledge on my part, and because a large dataset could be collated, although this process could easily be replicated with another parent genre and sub-genres.


# Repository Files
- Classification.ipynb
- Data_Prep.ipynb
- pipeline.py
- api.py
- data_cleaning.py


# Procedure and Project Overview

Problem
Data(Collect, Process, Explore)
Analysis
Results

*Visual*


# Data

<!-- Data Sources : https://developer.spotify.com/ https://www.riddimguide.com/ https://www.apple.com/uk/music/ https://www.last.fm/
 -->
For this project, the dataset was collated from playlists that were correctly labelled with their sub-genre. These songs were then searched on the Spotify API, and their audio features were recorded. 
Spotify API provides access to information about tracks, such as their popularity and release date, as well as user information, such as a user's featured playlists.  The API also provides audio features such as * , which give characteristics of a track, and pitch and timbre information. More information can be found *. 

A selection of music that would not be in my target genre was also collected, to allow for distinction between my target categories (music we can categorise), and that we cannot. 

As mentioned, the dependant variable being predicted was the sub-genre. These were given the labels:

0 = dancehall
1 = reggae
2 = soca
3 = Pop


# Model Selection

Given that a relatively small amount of data was available with the correct label, it seemed appropriate to build a classifiction model. 

A selection of models were built:

Logistic Regression
K-Nearest Neighbors
Decision Tree Classifier
AdaBoost Classifier
Gradient Boost Classifier
eXtreme Gradient Boost Classifier

A pipeline was created to build and optimise multiple models in unison. 

This process found the best model was the XGBoost Classifier.

# Results

For each sub-genre, accuracy and AUC were *, showing profficient 

* Spotify Play Button*

Success rate

Visuals

What do genres have in common?


# Next Steps
This process could easily be replicated with another genre and sub-genres, especially given the amount of data available through spotify. It can be challenging to find enough labelled data to train the model on, but

