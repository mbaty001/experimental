Analyzer
========

;-)

Install 
-------

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Install Analyzer::

    $ pip install -e .

Run
---

::

    $ export FLASK_APP=analyzer
    $ export FLASK_ENV=development
    $ flask run

Open http://127.0.0.1:5000 in a browser or use curl.

Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
