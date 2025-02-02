from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import RequestPreprintForm
from app.models import Preprint
import sqlalchemy as sa
from datetime import datetime, timezone

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RequestPreprintForm()
    if form.validate_on_submit():
        preprint = Preprint(authors=form.authors.data, title=form.title.data)
        query = sa.select(Preprint).where(sa.extract('year', Preprint.timestamp) == datetime.now(timezone.utc).year)
        preprints_this_year = db.session.scalars(query).all()
        preprint.set_preprint_id(len(preprints_this_year) + 1)
        db.session.add(preprint)
        db.session.commit()
        flash('Your preprint number is {}'.format(preprint.preprint_id))
        return redirect(url_for('index'))
    return render_template('index.html', form=form)