from script import db
from script.models import  Message
from flask import render_template, url_for, flash, redirect, request, Blueprint
from script.messages.forms import MessageForm
from flask_login import login_required

messages = Blueprint('messages', __name__)

# Message form
@messages.route('/message', methods=['GET', 'POST'])
def message(): 
    form = MessageForm()
    # messages = Message.query.all()
    page = request.args.get('page', 1, type=int)
    messages = Message.query.order_by(Message.date.desc()).paginate(page=page, per_page=20)
    if form.validate_on_submit():
        message = Message(name=form.name.data, letter=form.letter.data)
        db.session.add(message)
        db.session.commit()
        flash('Your message has been posted!', 'success')
        return redirect(url_for('messages.message'))
    return render_template('message.html', title='Message Board', form=form, posts=messages)

# Delete message
# @app.route("/message/<int:message_id>")
# def onemessage(message_id):
#     message = Message.query.get_or_404(message_id)
#     return render_template('onemessage.html', post=message)

@messages.route("/message/<int:message_id>/delete", methods=['POST']) 
@login_required
def delete_message(message_id):
    message = Message.query.get_or_404(message_id) 
    db.session.delete(message)
    db.session.commit()
    flash('Message has been deleted!', 'success') 
    
    return redirect(url_for('messages.message'))