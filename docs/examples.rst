***********************
Example configurations
***********************

Some example configurations.

Django project with travis-ci
------------------------------

We want use `pep8`, `sloccount`, `python unittests`, `coverage` and `pip-review` violations.

`.travis.yml`:

.. code-block:: yaml

    language: python
    python:
      - "2.7"
    before_install:
      - sudo apt-get update -qq
      - sudo apt-get install -qq sloccount
      - pip install pep8 pip-tools coviolations_app coverage
    script:
      - coverage run manage.py test 2>test_result
    after_script:
      - coverage report
      - covio

`.covio.yml`:

.. code-block:: yaml

    violations:
      pep8: pep8 . --exclude='*migrations*,*settings*,*components*,*docs*'
      sloccount: sloccount .
      py_unittest: cat test_result
      coverage: coverage report
      pip_review:
        command: pip-review
        nofail: true

We add `nofail` to `pip_review`, because we don't need to mark task failed if we have outdated packages.

Django project with jenkins or drone.io
----------------------------------------

Run script:

.. code-block:: bash

    pip install pep8 pip-tools coviolations_app coverage
    coverage run manage.py test 2>test_result
    coverage report
    COVIO_TOKEN='' covio

You can obtain token on project page.

`.covio.yml`:

.. code-block:: yaml

    violations:
      pep8: pep8 . --exclude='*migrations*,*settings*,*components*,*docs*'
      py_unittest: cat test_result
      coverage: coverage report
      pip_review:
        command: pip-review
        nofail: true

Python project with nose with travis-ci
---------------------------------------

`.travis.yml`:

.. code-block:: yaml

    language: python
    python:
      - "2.7"
    before_install:
      - sudo apt-get update -qq
      - sudo apt-get install -qq sloccount
      - pip install pep8 pip-tools coviolations_app coverage
    script:
      - nosetests --with-coverage 2>test_result
    after_script:
      - coverage report
      - covio

`.covio.yml`:

.. code-block:: yaml

    violations:
      pep8: pep8 . --exclude='*migrations*,*settings*,*components*,*docs*'
      sloccount: sloccount .
      py_unittest: cat test_result
      coverage: coverage report
      pip_review:
        command: pip-review
        nofail: true

Python project with nose with jenkins or drone.io
--------------------------------------------------

Run script:

.. code-block:: bash

    pip install pep8 pip-tools coviolations_app coverage
    nosetests --with-coverage 2> test_result
    coverage report
    COVIO_TOKEN='' covio

You can obtain token on project page.

`.covio.yml`:

.. code-block:: yaml

    violations:
      pep8: pep8 . --exclude='*migrations*,*settings*,*components*,*docs*'
      py_unittest: cat test_result
      coverage: coverage report
      pip_review:
        command: pip-review
        nofail: true

JavaScript project with testem with travis-ci
---------------------------------------------

We want use `testem` and `jslint`.


`.travis.yml`:

.. code-block:: yaml

    language: node_js
    python:
      - "2.7"
    node_js:
      - "0.10"
    before_install:
      - npm install testem jslint
      - pip install coviolations_app
    script:
      - testem>test_result
    after_script:
      - covio

`.covio.yml`:

.. code-block:: yaml

    violations:
      testem: cat test_result
      jslint: jslint *.js

JavaScript project with testem with jenkins or drone-io
--------------------------------------------------------

Run script:

.. code-block:: bash

    npm install testem jslint
    pip install coviolations_app
    testem>test_result
    COVIO_TOKEN='' covio

`.covio.yml`:

.. code-block:: yaml

    violations:
      testem: cat test_result
      jslint: jslint *.js
