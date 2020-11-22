from flask import render_template, request, Blueprint
from script.models import Post
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # Adding posts to index
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', posts=posts)

@main.route('/about')
def about(): 
    return render_template('about.html', title='About')