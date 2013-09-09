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

`.travis.yml`:

.. code-block:: yaml

    before_install:
      - pip install pep8
    after_success:
      - covio

sloccount
=========

Count source lines of code (SLOC).

`.covio.yml`:

.. code-block:: yaml

    violations:
      sloccount: sloccount .

`.travis.yml`:

.. code-block:: yaml

    before_install:
      - sudo apt-get update -qq
      - sudo apt-get install -qq sloccount
    after_success:
      - covio

Python unittests
================

The Python unit testing framework, sometimes referred to as “PyUnit,” is a Python language version of JUnit, by Kent Beck and Erich Gamma. JUnit is, in turn, a Java version of Kent’s Smalltalk testing framework. Each is the de facto standard unit testing framework for its respective language.

`.covio.yml`:

.. code-block:: yaml

    violations:
      py_unittest: cat test_out

`.travis.yml` with nose:

.. code-block:: yaml

    before_install:
      - pip install nose
    script:
      - nosetests 2>test_out
    after_success:
      - covio

`.travis.yml` with django:

.. code-block:: yaml

    script:
      - ./manage.py test 2>test_out
    after_success:
      - covio
