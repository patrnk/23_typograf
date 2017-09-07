from flask import Flask, render_template, request

from utils import typograph_text


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def typograph():
    context = {}
    context['source_text'] = request.form.get('text')
    if context['source_text']:
        typographed_text = typograph_text(context['source_text'])
        context['typographed_text'] = typographed_text
    return render_template('form.html', **context)


if __name__ == "__main__":
    app.run()