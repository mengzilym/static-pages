"""
mdweb
-----

mdweb is just a practise demo.

:copyright: (c) 2017 by Max Flew.
:license: MIT, see LICENSE for more details.

"""
# -*- coding="utf-8" -*-

from flask import Flask, render_template, url_for, redirect
from flask_flatpages import FlatPages, pygments_style_defs


app = Flask(__name__)

FLATPAGES_EXTENSION = ['.md', '.html']
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite(linenums=True)']
FLATPAGES_ROOT = 'pages'
app.config.from_object(__name__)

flatpages = FlatPages(app)


@app.route('/')
@app.route('/pages/<path:path>.html')
def show_page(path=None):
    _pages = [p for p in flatpages if 'title' in p.meta]
    pages = list(range(len(_pages)))
    for p in _pages:
        pages[p.meta['id']] = p
    if not path:
        if pages:
            return render_template('page.html', pages=pages, page=pages[0])
        else:
            return render_template('index.html', pages=pages)
    page = flatpages.get_or_404(path)
    return render_template('page.html', pages=pages, page=page)


@app.route('/static/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    app.run(
        debug=True,
        # host='0.0.0.0'
        )
