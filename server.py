from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms.fields import TextAreaField
from wtforms import validators


app = Flask(__name__)
# this should be changed in production
app.secret_key = 'change me'


class SourceTextForm(FlaskForm):
    source_text = TextAreaField(validators=[validators.required()])


class TypographedTextForm(FlaskForm):
    typographed_text = TextAreaField()


@app.route('/', methods=['GET', 'POST'])
def typograph():
    context = {}
    context['input_form'] = SourceTextForm(request.form)
    context['output_form'] = TypographedTextForm()
    if context['input_form'].validate_on_submit():
        context['output_form'].typographed_text = context['input_form'].source_text
    return render_template('form.html', **context)


if __name__ == "__main__":
    app.run()
