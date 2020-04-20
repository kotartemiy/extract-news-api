# extract-news-api
Flask code to deploy an API to pull structured data from online news articles

## Demo
![](extract_image.png)


## Quick Start
1. Clone the repository to your local folder 

`git clone https://github.com/kotartemiy/extract-news-api.git`
2. Create a Python virtual environment (3.6+)
3. Activate the environment
4. Run `pip install -r requirements.txt`
5. Run `python app.py` in your terminal 

If everything is OK then you should be able to check your API on `http://127.0.0.1:5000/v0/article`

Example of request: `http://127.0.0.1:5000/v0/article`



## Built with
[Flask](https://github.com/pallets/flask) Copyright 2010 Pallets

[newspaper](https://github.com/codelucas/newspaper) Copyright (c) 2013 Lucas Ou-Yang

[date_guesser](https://github.com/mitmedialab/date_guesser) Copyright (c) 2018 MIT Center for Civic Media

