from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.debug = True
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = 'filesystem'
# Session(app)
comments = []


def get_pages():
    pages_method = ['what_is_lorem_ipsum', 'generate_lorem_ipsum', 'leave_a_comment', 'get_comments_list']
    pages_name = [str.join(" ", page.split('_')).capitalize() for page in pages_method]
    return [x for x in zip(pages_method, pages_name)]


@app.route('/')
def index():
    return render_template('index.html', pages=get_pages())


@app.route('/what-is-lorem-ipsum')
def what_is_lorem_ipsum():
    return render_template('loremipsum.html')


@app.route('/generate-lorem-ipsum')
def generate_lorem_ipsum():
    return render_template('generate.html')


@app.route('/leave-a-comment', methods=['GET', 'POST'])
def leave_a_comment():
    if request.method == 'POST':
        if request.form.get('name') is not "":
            name = request.form.get('name')
            comment = request.form.get('comment')
            comments.append(comment)
        else:
            comment = request.form.get('comment')
            comments.append((comment, 'Anonymous'))
    return render_template('leave-a-comment.html')


@app.route('/comments-list', methods=['GET'])
def get_comments_list():
    return render_template('comments-list.html', comments=comments)


if __name__ == '__main__':
    app.run()
