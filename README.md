<h1 align="center"> IMMO Eliza ML </h1>
<p align="center">
    <img src="assets/images/banner.png">
</p>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Mission](#mission)
- [Overview](#overview)
- [Dependencies](#dependencies)
- [Project structure](#project-structure)
- [Personal situation](#personal-situation)

## Mission

The real estate company Immo Eliza is really happy with your regression model and current work up to now.

They would like you to create an API so their web developers can access the predictions whenever they need to. They also want to have a small web application for the non-technical employees and possibly their clients to use. The API and the web application should be intertwined but separate.

## Overview

This is a small web application that allows to predict the price of a property in Belgium, depending on the characteristics of the property. To achieve this it makes use of an <a href="https://github.com/karelrduran/immo-eliza-api">API</a> previously developed as part of a previous step of the project.

The application was deployed at https://immo-eliza-price-predict.streamlit.app/

## Dependencies
    streamlit~=1.32.2
    streamlit-image-select~=0.6.0
    requests~=2.31.0

## Project structure
- [/](/)
  - [assets/](assets) -- Contains project assets
      - [images/](assets/images) -- Images used in project
  - [src/](src) -- Contains the source code of the project
    - [data_predict.py](src/data_predict.py) -- Uses an API to predict the price of a property
    - [forms](src/forms.py) -- -- Module defining Streamlit forms
  - [app.py](app.py) -- Main script that runs the application
  - [README.md](README.md) -- Readme file
  - [requirements.txt](requirements.txt) -- Contains required packages by the project



## Personal situation
While doing this project I was part of the ARAI6 group of the <a href="https://becode.org/all-trainings/pedagogical-framework-ai-data-science/">AI Bootcamp</a> training organized by <a href="https://becode.org/">BeCode</a> in Ghent. 

______________________________________
  <img src="https://avatars.githubusercontent.com/u/106887418?s=400&u=82192b481d8f03c3eaad34ca2bd67889fce6a0c2&v=4" width=115><br><sub><img src="assets/images/linkedin.png" alt="Miniatura" width=20><a href="https://www.linkedin.com/in/karel-rodriguez-duran/">Karel Rodríguez Durán</a></sub>