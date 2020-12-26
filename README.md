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
- Collections<br>
<h3><b>Dataset </b></h3>
The dataset used in this project is BBC News Dataset.It consists 0f 1500+ .txt files which have an excerpt of news related to various categories. Text files were categorized into 2 folders "neg" and "pos" based on the sentiment of text and later training and test dataset werecreated.The dataset can be found inside <b>Train Ready Dataset.zip</b>
<h3><b>Data pre-processing</b></h3>
The dataset was then cleaned to remove punctuations, stop words, and words with minimum occurrence. Finally, vocabulary<b>(vocab.txt)</b> was later created from the clean tokens.


<h3><b>Conclusion</b></h3>
The sentiment of public opinion such as movie reviews in IMDB can be construed based on the opinion gave by the original poster. But in the context of news, which is informative, it can be construed in both positive and negative ways based on the perception of the reader.
 For eg, in a news titled," US cigarette companies laud tax cut offered by the government", it can be construed in both positive and negative ways. Hence the sentiment of news predicted by the machine learning model cannot be termed as definitive.
