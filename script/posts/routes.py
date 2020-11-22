from flask import render_template, url_for, flash, redirect, request, Blueprint
from script.models import Post
from script import db
from script.posts.forms import NewPostForm, EditPostForm
from flask_login import current_user, login_required

posts = Blueprint('posts', __name__)

#New post
@posts.route('/newpost', methods=['GET', 'POST'])
@login_required
def newpost(): 
    form = NewPostForm()
    if form.validate_on_submit():
        # Add new post to database
        post = Post(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()

        flash('New poem posted', 'success')
        return redirect(url_for('main.home'))
    return render_template('newpoem.html', title='New Post', form=form, legend='New Post')

# Update Post
@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
# Checking entered data (current user) against database using query
def updatepost(post_id):

    form = NewPostForm()

    post = Post.query.get_or_404(post_id)
    # make sure only author can edit
    if post.author != current_user:
    # 403 - forbidden route
        abort(403)

    # validate and update
    if form.validate_on_submit(): 
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))

    # automatically fill in current username/email in fields
    elif request.method == 'GET': 
        form.title.data = post.title
        form.content.data = post.content

    return render_template('newpoem.html', title='Update Post', form=form, legend='Update Post')

# Individual posts
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

# Index of post titles
@posts.route("/titles")
def titles():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.title.asc()).paginate(page=page, per_page=100)
    return render_template('titles.html', title='Index', posts=posts)

# Delete posts
@posts.route("/post/<int:post_id>/delete", methods=['POST']) 
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id) 
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success') 
    
    return redirect(url_for('main.home'))