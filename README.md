# ReviewSummarization
Aspect Based Review Summarization
 
Sequence of Project Activities
0. Data Extraction and Filtering
1. Topic Analysis and Mapping
2. Sentiment Analysis
3. Summarization
4. Displaying Result

===============================================================================
DATA EXTRACTION AND FILTERING
Yelp business data in English is used as base data.

Data Location:
Main/Data/OriginalEngishReviews/
Main/Data/HindiReviews/

Main/Data/OriginalEngishReviews/ contains reviews which are shortlisted for the
purpose of translation.
Main/Data/HindiReviews/ contains manually translated reviews in Hindi.

All the pre-processing of data is done by
a. parseBusinessID.py
b. parseReviews.py
c. CountRestaurants.py

===============================================================================
TOPIC ANALYSIS and MAPPING
LDA technique is used to identify topics from reviews. These identified topics
are then mapped to aspects of our interest. These aspects are shorlisted via
internet research.
Topic analysis is done for each sentence in a review and as per the topic the
sentence will be classified into its corresponding aspect.

Apects of our interest are:
a. Ambience
b. Food
c. Service
d. value

Code Location:
Main/LDA/

===============================================================================
SENTIMENT ANALYSIS
1. Bayes Classifier
For each topic identified we run sentiment analysis on them classifying each
sentence as positive and negative. This classification will help user get both
the point of opinion on restaurant of choice.

Code Location:
Main/Classifier/

===============================================================================
SUMMARIZATION
Once data is classified into sentiments for each aspect and for each restaurant
we are now ready to run summarization on it.

Code Location:
TODO

===============================================================================
DISPLAYING RESULTS
The above result will be displayed via web interface dialog box. This box
provides a selection of restaurant and the feature user is interested in. Once,
this selection is made we display the summary of reviews for each sentiment on
this web interface.

Code Location:
TODO

===============================================================================
