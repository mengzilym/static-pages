# -*- coding='utf-8' -*-

from flask_frozen import Freezer
from mdweb import app
import sys

freezer = Freezer(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        freezer.run(debug=True)
    else:
        freezer.freeze()
