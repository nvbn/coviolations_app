***************
Available violations
***************

PEP8
=====

Check your Python code against some of the style conventions in PEP 8.

`.covio.yml`:

.. code-block:: yaml

    violations:
      pep8: pep8 . --exclude='*migrations*'

For travis-ci in `.travis.yml`:

.. code-block:: yaml

    before_install:
      - pip install pep8
    after_success:
      - covio

For drone.io and jenkins in project script:

.. code-block:: bash

    pip install pep8
    COVIO_TOKEN="token" covio

sloccount
=========

Count source lines of code (SLOC).

`.covio.yml`:

.. code-block:: yaml

    violations:
      sloccount: sloccount .

For travis-ci in `.travis.yml`:

.. code-block:: yaml

    before_install:
      - sudo apt-get update -qq
      - sudo apt-get install -qq sloccount
    after_success:
      - covio

For drone.io and jenkins in project script:

.. code-block:: bash

    sudo apt-get update -qq
    sudo apt-get install -qq sloccount
    COVIO_TOKEN="token" covio

Python unittests
================

The Python unit testing framework, sometimes referred to as “PyUnit,” is a Python language version of JUnit, by Kent Beck and Erich Gamma. JUnit is, in turn, a Java version of Kent’s Smalltalk testing framework. Each is the de facto standard unit testing framework for its respective language.

`.covio.yml`:

.. code-block:: yaml

    violations:
      py_unittest: cat test_out

For travis-ci in `.travis.yml` with nose:

.. code-block:: yaml

    before_install:
      - pip install nose
    script:
      - nosetests 2>test_out
    after_success:
      - covio

For travis-ci in `.travis.yml` with django:

.. code-block:: yaml

    script:
      - ./manage.py test 2>test_out
    after_success:
      - covio

For drone.io and jenkins in project script with nose:

.. code-block:: bash

    pip install nose 2>test_out
    COVIO_TOKEN="token" covio

For drone.io and jenkins in project script with django:

.. code-block:: bash

    ./manage.py test 2>test_out
    COVIO_TOKEN="token" covio

pip-review
==========

Keeps your Python package dependencies pinned, but fresh.

`.covio.yml`:

.. code-block:: yaml

    violations:
      pip_review: pip-review

For travis-ci in `.travis.yml`:

.. code-block:: yaml

    before_install:
      - pip install pip-tools
    after_success:
      - covio

For drone.io and jenkins in project script:

.. code-block:: bash

    pip install pep-tools
    COVIO_TOKEN="token" covio

testem
======

Unit testing in Javascript can be tedious and painful, but Testem makes it so easy that you will actually want to write tests.

`.covio.yml`:

.. code-block:: yaml

    violations:
      testem: cat testem_out

For travis-ci in `.travis.yml`:

.. code-block:: yaml

    script:
      - testem ci > testem_out
    after_success:
      - covio

For drone.io and jenkins in project script:

.. code-block:: bash

    testem ci > testem_out
    COVIO_TOKEN="token" covio

