from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm


posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(username=current_user, date_posted=form.date_posted.data, pin=form.pin.data, 
                    associate=form.associate.data, dept=form.dept.data, team_mgr=form.team_mgr.data,
                    ops_mgr=form.ops_mgr.data, surv_trigg=form.surv_trigg.data, surv_deliv=form.surv_deliv.data,
                    del_rate=form.del_rate.data, resp_cnt=form.resp_cnt.data, popo=form.popo.data,
                    resp_rate=form.resp_rate.data, avg_rating=form.avg_rating.data, five_stars=form.five_stars.data,
                    four_stars=form.four_stars.data, three_stars=form.three_stars.data, two_stars=form.two_stars.data,
                    one_stars=form.one_stars.data, five_star=form.five_star.data, four_star=form.four_star.data,
                    three_star=form.three_star.data, two_star=form.two_star.data, one_star=form.one_star.data,
                    team_lead=form.team_lead.data, chan=form.chan.data)
        db.session.add(post)
        db.session.commit()
        flash(f'Your post has been created!', 'success')
        return redirect(url_for('posts.new_post'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.username != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.date_posted = form.date_posted.data
        post.pin = form.pin.data
        post.associate = form.associate.data
        post.dept = form.dept.data
        post.team_mgr = form.team_mgr.data
        post.ops_mgr = form.ops_mgr.data
        post.surv_trigg = form.surv_trigg.data
        post.surv_deliv = form.surv_deliv.data
        post.del_rate = form.del_rate.data
        post.resp_cnt = form.resp_cnt.data
        post.popo = form.popo.data
        post.resp_rate = form.resp_rate.data
        post.avg_rating = form.avg_rating.data
        post.five_stars = form.five_stars.data
        post.four_stars = form.four_stars.data
        post.three_stars = form.three_stars.data
        post.two_stars = form.two_stars.data
        post.one_stars = form.one_stars.data
        post.five_star = form.five_star.data
        post.four_star = form.four_star.data
        post.three_star = form.three_star.data
        post.two_star = form.two_star.data
        post.one_star = form.one_star.data
        post.team_lead = form.team_lead.data
        post.chan = form.chan.data
        db.session.commit()
        flash('Your change has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.pin.data = post.pin
        form.associate.data = post.associate
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.username != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


