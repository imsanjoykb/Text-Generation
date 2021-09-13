![Author](https://img.shields.io/badge/author-SanjoyBiswas-orange)
[![Stars](https://img.shields.io/github/stars/imsanjoykb/Text-Generation.svg?style=social)](https://github.com/imsanjoykb/Text-Generation/)
[![MIT](https://img.shields.io/badge/license-MIT-5eba00.svg)](https://github.com/imsanjoykb/Text-Generation/LICENCE.txt)
[![Open Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/imsanjoykb/Text-Generation/blob/master/Text_Generation.ipynb)


![alt text](Assets/banner.jpg "Title")

# Author: Sanjoy Biswas

Data Scientist | Machine Learning Engineer </br>
Website: https://imsanjoykb.github.io/ </br>
ResearchGate: https://www.researchgate.net/profile/imsanjoykb </br>
Linkedin: https://www.linkedin.com/in/imsanjoykb/ </br>
Email: sanjoy.eee32@gmail.com <br>

<hr>


## Objective

The goal of this project is to detect the topic of the text and write a proper comment for the text , store the generate comment in database and shows it with rest API.

<hr>

## Background

Text generation is an application of language modeling, and a subfield of natural language processing. It utilizes techniques in artificial intelligence to automatically generate natural language text, which fits in a certain communication context.

Text generation can be used to write stories, poems, emails, news articles, and more. It is also useful for machine translation.

<hr>

## Project Installation

<b>Install the virtualenv package</b>
```
pip install virtualenv  
```
<b>Create the virtual environment</b>
```
virtualenv venv 
```
<b>Activate the virtual environment</b>
```
mypthon\Scripts\activate
```
<b>Install Dependencies</b>
```
pip3 install -r requirements.txt
```
<b>Run the text generation code which redirect userinterface of Gradio and the input of the text generate datafile</b>
```
python Text_Generation.py
```
<b>After this, run main.py file which scale the data and connect with database to store data at DB</b>
```
python main.py
```
<b>Then run app.py file which shows all data and also Gradio </b>
```
python app.py
```

<hr>

## Project GUI
Gradio Interface for text generation:<br>

![alt text](Assets/Interface1.PNG "Title")

Shows Generated output:<br>

![alt text](Assets/Interface2.PNG "Title")

Store Data at Database:<br>

![alt text](Assets/database1.PNG "Title")

Shows generated data with timestamp in GUI:<br>

![alt text](Assets/data.PNG "Title")

<hr>

