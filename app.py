from flask import Flask, jsonify, request
from newspaper import Article
from date_guesser import guess_date, Accuracy
from langdetect import detect, detect_langs


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/v0/article', methods=['GET'])
def get_article():
    url = None

    url = request.args.get('url', type=str)

    if url == None:
        return 'url parameter is required', 400

    article = Article(url)
    article.download()

    if (article.download_state == 2):
        article.parse()
        article_dict = {}
        article_dict['status'] = 'ok'

        article_dict['article'] = {}
        article_dict['article']['source_url'] = article.source_url


        try:
            guess = guess_date(url = url, html = article.html)
            article_dict['article']['published'] = guess.date
            article_dict['article']['published_method_found'] = guess.method
            article_dict['article']['published_guess_accuracy'] = None
            if guess.accuracy is Accuracy.PARTIAL:
                article_dict['article']['published_guess_accuracy'] = 'partial'
            if guess.accuracy is Accuracy.DATE:
                article_dict['article']['published_guess_accuracy'] = 'date'
            if guess.accuracy is Accuracy.DATETIME:
                article_dict['article']['published_guess_accuracy'] = 'datetime'
            if guess.accuracy is Accuracy.NONE:
                article_dict['article']['published_guess_accuracy'] = None
        except:
            article_dict['article']['published'] = article.publish_date
            article_dict['article']['published_method_found'] = None
            article_dict['article']['published_guess_accuracy'] = None

        article_dict['article']['title'] = article.title
        article_dict['article']['text'] = article.text
        article_dict['article']['authors'] = list(article.authors)

        try:
            title_lang = detect(article.title)
        except:
            title_lang = None


        try:
            text_lang = detect(article.text)
        except:
            text_lang = None

        article_dict['article']['images'] = list(article.images)
        article_dict['article']['top_image'] = article.top_image
        article_dict['article']['meta_image'] = article.meta_img
        article_dict['article']['movies'] = list(article.movies)
        article_dict['article']['meta_keywords'] = list(article.meta_keywords)
        article_dict['article']['tags'] = list(article.tags)
        article_dict['article']['meta_description'] = article.meta_description
        article_dict['article']['meta_lang'] = article.meta_lang
        article_dict['article']['title_lang'] = str(title_lang)
        article_dict['article']['text_lang'] = str(text_lang)
        article_dict['article']['meta_favicon'] = article.meta_favicon
        return jsonify(article_dict)

    else:
        article_dict = {}
        article_dict['status'] = 'error'
        article_dict['article'] =  article.download_exception_msg
        return jsonify(article_dict)


if __name__ == '__main__':
    app.run()