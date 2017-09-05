from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms.fields import TextAreaField
from wtforms import validators


app = Flask(__name__)
# this should be changed in production
app.secret_key = 'change me'


class SourceTextForm(FlaskForm):
    source_text = TextAreaField(validators=[validators.required()])


@app.route('/', methods=['GET', 'POST'])
def typograph():
    form = SourceTextForm(request.form)
    if form.validate_on_submit():
        raise ValueError(form.source_text)
    return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run()
