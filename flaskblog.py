from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Zac',
        'title': 'Blog post 1',
        'content': 'First post Content',
        'date_posted': '20 Avril 2018'
    },
    {
        'author': 'Bob',
        'title': 'Blog post 2',
        'content': 'Second post Content',
        'date_posted': '21 Avril 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
