# Introduction

This repository contains template Jupyter notebooks to explore data, build
MVP models, and communicate results with minimal effort and code.

The script `main.py` executes all notebooks and exports HTML reports to 
`/notebook/page`. The HTMLs appear as webpages on the published
[GitHub project site](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites).

## Table of contents

Exploratory data analysis
 
- Static graphs with Seaborn
- Interactive graphs with Plotly Express

Machine learning with PyCaret

- Regression
- Classification
- Clustering
- Forecasting
- Anomaly detection 
- Natural language processing
- Association rule mining

## Beyond notebooks

Publishing notebooks with GitHub pages is a convenient way to organize and share
work in the early stages of model development. As the model matures, more 
functional interfaces may be needed. 

Two low-code frameworks cover many use cases:

- FastAPI backend to serve predictions
- Streamlit UI to generate results for user-uploaded data

For production-ready applications, Dash or Flask may be preferable to Streamlit,
[at least for now](https://towardsdatascience.com/streamlit-can-not-yet-replace-flask-the-streamlit-2020-roadmap-64840564acde). 
