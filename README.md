Classifying Music by Sub-Genre
 
Project Scope
For this project, a classification system was built to identify and arrange music by sub-genre.
Currently, Spotify has functionality to do ....
Allowing for more flexibility in how music is stred will ...
Music streaming services have revolutionised how we consume music
The services come with numerous perks, most notably instantaneuos access to music, without having to have it stored on your device. 
However this problem comes at a price: the lack of ownership of music. 
Lack of control of how this music is organised
Music is often generealise into wider genres, for ease of access and storage. These immutable labels, pre-determined by Spotify, can range from spookily accurate 
Non-Western genres feel this the most
Chose reggae, for domain and large data selection, but also apppicable to rising number of distinct genres in UK music scene.


Repo Files

Procedure and Project Overview

Problem
Data(Collect, Process, Explore)
Analysis
Results

*Visual*


Data

Data Sources : https://developer.spotify.com/ https://www.riddimguide.com/

All data was collected from the Spotify Web API. 
Spotify API provides access to information about tracks, such as *, as well as user information, such as *. 
The API also provides audio features such as * .

For this project, the dataset was built from playlists that were correctly labelled with their sub-genre,
Riddim Guide was an essential resource for this.

I also incuded a selection of music that would not be in my target genre, to allow for distinction between my target categories, as well as between music we can categorise, and that we cannot. 

As mentioned, the dependant variable being predicted was the sub-genre, given the labels:

# 0 = dancehall
# 1 = reggae
# 2 = soca
# 3 = Pop




Model Selection

Given that a relatively small amount of data was available with the correct label, it seemed appropriate to build a classifiction model instea of a network, where some work has been done previously. *?* 

A pipeline was created to build and optimise multiple models in unison. This process found the best model was *.

Logistic Regression
K-Nearest Neighbors
Decision Tree Classifier
Random Forrest Classifier
AdaBoost Classifier
Gradient Boost Classifier
eXtreme Gradient Boost Classifier
<!-- Support Vector Machine -->

Results

For each sub-genre, accuracy and AUC

* Spotify Play Button*

Success rate

Visuals

What do genres have in common?

Creating your own playlist

 
Reccomendation




Next Steps

More data

Different genres

