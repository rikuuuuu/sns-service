import os
from flask import Flask, render_template, request
from flask_cors import CORS
from app import twitter, youtube

app = Flask(__name__)

CORS(app)

# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/', methods=['POST'])
def tweet():
    post_text = request.form['post_text']
    file1 = request.files['post_img1']
    file2 = request.files['post_img2']
    file3 = request.files['post_img3']
    file4 = request.files['post_img4']
    images = []
    if not file1:
        twitter.post_tweet(post_text)
    if file1:
        file1.save(os.path.join("img/", file1.filename))
        filepath1 = os.path.join("img/", file1.filename)
        images.append(filepath1)
    if file2:
        file2.save(os.path.join("img/", file2.filename))
        filepath2 = os.path.join("img/", file2.filename)
        images.append(filepath2)
    if file3:
        file3.save(os.path.join("img/", file3.filename))
        filepath3 = os.path.join("img/", file3.filename)
        images.append(filepath3)
    if file4:
        file4.save(os.path.join("img/", file4.filename))
        filepath4 = os.path.join("img/", file4.filename)
        images.append(filepath4)
    if len(images) > 0:
        twitter.post_tweet_with_media(text=post_text, images=images)
    for image in images:
        os.remove(image)
    return render_template('index.html', post_text=post_text)

@app.route('/youtube-search/', methods=['GET'])
def search():
    query = request.args['q']
    videoIds = youtube.search_query(query=query)
    return {"videoIds": videoIds}

if __name__ == '__main__':
    app.run(debug=True)
