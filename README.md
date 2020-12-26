# Sentiment analysis of English Newspapers printed in Nepal using Stacked Bidirectional Long short-term memory(BiLSTM) model.

<h3><b>Required Libraries </b></h3>
- NLTK<br>
- OS<br>
- Numpy<br>
- Keras<br>
- Gensim<br>
- Pickle<br>
- Tensorflow<br>
- Collections<br>
<h3><b>Dataset </b></h3>
The dataset used in this project is BBC News Dataset.It consists 0f 1500+ .txt files which have an excerpt of news related to various categories. Text files were categorized into 2 folders "neg" and "pos" based on the sentiment of text and later training and test dataset was created.The dataset can be found inside <b>Train Ready Dataset.zip</b>
<h3><b>Data pre-processing</b></h3>


In this project I have developed Sentiment Analyzer using both Keras Embedding and Word2Vec Embedding. Use of Keras Embedding yielded better result so the model developed using stacked BiLSTM and Keras Embedding was later usied in Flask app to analyze the live sentiment of news published in english news papers of nepal. 
