# Customer_identification_using_Web_basedHigh-value consumer profiling using a hybrid                                      text-based and web-based approach


# ===== Project Description =====#


In this project, we propose an approach to find out new potential consumers for a specific product or service offering using the social media presence of consumers. Using a hybrid, text-based and web-based approach we aim to identify and rank high-value customers using text-analysis, network-analysis and machine learning. This allows businesses to better design customer engagement programs targeting the right social media audience that are most likely to convert into consumers, thus improving the efficiency of customer acquisition, and increasing return on investment.


The approach was demonstrated by gathering tweets for Tesla, several non-target accounts, 405 followers of Tesla and a total of 7570 neighbors. A text-based decision tree ensemble model classified tweets with a F1-accuracy of 0.984. The web-based approaches are compared against the text-based approach, where the proposed relational classifier outperforms the community-approach in capturing the text-based classifications in absence of enough text. 


The following are required installations:
- Python 3 and its libraries
- Jupyter notebooks


# ===== Installation ===== #
1. Python: Can be downloaded from https://www.python.org/downloads/
2. Jupyter Notebooks: Link for downloading: https://jupyter.org/install
3. Related libraries:
* NLTK: https://www.nltk.org/install.html
* Sklearn: https://scikit-learn.org/stable/
* Tweepy: http://docs.tweepy.org/en/latest/install.html
* Matplotlib: https://matplotlib.org/
* Networkx: https://networkx.github.io/

4. Twitter API: Request API keys for gathering twitter data from Developer documents: https://developer.twitter.com/en 

# ===== Running the Scripts ===== #
1. Gathering Tweets: 
Target and Non-Target accounts:
run tweets_api.py for gathering tweets for 10 twitter accounts: 'tesla', 'ladygaga', 'usedgov', 'FoodandTravelEd', 'nytimes', 'premierleague', 'MTV','facebook', 'eBay', 'parenting'. These are saved in the folder ‘tweets_raw’.

* Followers’ Tweets
  This script also gathers tweets for Tesla followers and followers of Tesla followers and stores them as-
  1. Followers_pull1.json
  2. Followers_pull2.json
  3. Followers_pull3.json

2. Text Based Approach: Run the following files-
* Data_Cleaning.ipynb 
   * Performs cleaning of tweets and stores them in ‘cleaned_csv’
   * Generates tf-idf matrices for target and non target accounts and stores them in ‘tfidf_matrices’ folder

* POS_tagging.ipynb - Extracts nouns and stores them in ‘pos_csv’ folder in corresponding csv files

* Evaluation 1 _TF nouns.ipynb - 
   * Performs topic modeling: results are stored in ‘topic_modelling_nouns’ folder
   * Extracts top tf terms per account: output can be found in ‘terms_frequency_nouns’ folder

* Evaluation 2_and_3.ipynb - Chisq Test and Ranking : 
   * Performs feature selection for the target and non target accounts
   * This generates the tf-idf matrix for every user, classifies the tweets and accordingly ranks the users.

3. Web Based Approach- Community: 
* Web based approach.ipynb - calculates score for first and second level users

4. Web Based Approach: Relational Classifier:
*  Homophily_Relational.ipynb - Performs the Test of Homophily and Relational classification_techniques
