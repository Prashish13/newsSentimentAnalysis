# Sentiment analysis of English Newspapers printed in Nepal using Stacked Bidirectional Long short-term memory(BiLSTM) model.
<h3><b>Introduction</b></h3>
In this project I have developed Sentiment Analyzer using both Keras Embedding and Word2Vec Embedding. Use of Keras Embedding yielded better result so the model developed using stacked BiLSTM and Keras Embedding was later usied in Flask app to analyze the live sentiment of news published in english news papers of nepal. 
<h3><b>Required Libraries </b></h3>
- NLTK<br>
- OS<br>
- Numpy<br>
- Keras<br>
- Gensim<br>
- Pickle<br>
- Tensorflow<br>
- BeautifulSoup
- Flask
- Collections<br>
<h3><b>Dataset </b></h3>
The dataset used in this project is BBC News Dataset.It consists 0f 1500+ .txt files which have an excerpt of news related to various categories. Text files were categorized into 2 folders "neg" and "pos" based on the sentiment of text and later training and test dataset werecreated.The dataset can be found inside <b>Train Ready Dataset.zip</b>
<h3><b>Data preparation</b></h3>
The dataset was then cleaned to remove punctuations, stop words, and words with minimum occurrence. Finally, vocabulary<b>(vocab.txt)</b> was later created from the clean tokens.
<h3><b>Training Embedding Layer</b></h3>
For training Embedding layer, both keras  and Word2Wec  was used.Keras embedding was learned while training a neural network.However,for word2vec embedding, pre-processed training dataset was passed to gensim word2vec model and embedding vector was created and saved. Later on, pretrained embedding was used to form an embedding layer in the training model.  In both case, embedding vector space was kept at 100. Similarly, Keras Tokenizer API was used for preparing texts,creating a mappping from words in the vocabulary to a unique integer, and encoding the documents in the train/test set into sequence of unique integers.
<h3><b>Model</b></h3>
Model was defined using Embedding Layer,Stacked Bidirectional LSTM(BiLSTM) with dropout of 20% and 1 dense layer with 2 output..Since this is multi-class classification, so softmax classifier was used. Similarly model was compiled using 'categorical_crossentropy' loss function and "Adam" optimizer.
<h3><b>Training and Evaluation</b></h3>
Model was trained for 10 epochs and accuracy on test dataset was calculated. The accuracy of model with keras embeeding was 78.75 % while the accuracy of model built using pretrained embedding learned using Word2Vec algorithm was 60%. The tokenizer and model with high accuracy was saved later for Sentiment analysis of English Newspapers printed in Nepal.
<h3><b>Building Flask APP using Web Scrapping</b></h3>
Flask app was created to scrap news articles and display their sentiment in a web application.BeautifulSoup was used to scrap the news article from 3 leading English Newspapers of Nepal: The Himalayan Times, The Kathmandu Post, and Republica Nepal. After that, the news article was fed to our learned model, and the sentiment of the news was evaluated. At last, 3 separate HTML table was created for each Newspaper and the news headline with corresponding sentiment label was displayed in the table. Similarly, other additional functionalities to read a news article in detail and visit news article site was added. Each time, the news feed is refreshed, the application will scrape the fresh news article from the websites, fed news articles to model and display their sentiments.
<b>Screenshot of application displaying the sentiment of news article is shown below</b>
<br>
<b>Application Layout</b>
![Alt text](flaskapp1.png?raw=true "Optional Title")
<br>
<b>News article from The Himalayan Times</b>
![Alt text](flaskapp2.png?raw=true "Optional Title")
<br>
<b>News article from The Kathmandu Post</b>
![Alt text](flaskapp3.png?raw=true "Optional Title")
<br>
<b>News article from The Republica Nepal</b>
![Alt text](flaskapp4.png?raw=true "Optional Title")
<br>
<b>Option to read news article in length and vist news article site</b>
![Alt text](flaskapp5.png?raw=true "Optional Title")
<br>
<h3><b>Conclusion</b></h3>
Since the model was trained with very few news articles, and those news articles were not the best representation of the type of news published in Newspapers of Nepal, so the model was not able to generalize properly. In a later iteration of the project, the model will be trained with the news article based on the context of Nepal to increase the accuracy of sentiment prediction.

<h3><b>Efficacy of </b></h3>
The sentiment of public opinion such as movie reviews in IMDB can be construed based on the opinion gave by the original poster. But in the context of news, which is informative, it can be construed in both positive and negative ways based on the perception of the reader.
 For eg, in a news titled," US cigarette companies laud tax cut offered by the government", it can be construed in both positive and negative ways. Hence the sentiment of news predicted by the machine learning model cannot be termed as definitive.
 
 
 
 
 
 
 
 ![Alt text](flaskapp1.png?raw=true "Optional Title")
