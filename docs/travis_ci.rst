********************
Using with travis ci
********************

For covio add in section `after_success`:

.. code-block:: yaml

    after_success:
      - pip install coviolations_app
      - covio

For using pep8 add to section `before_install`:

.. code-block:: yaml

    before_install:
      - pip install pep8

For using sloccount add to section `before_install`:

.. code-block:: yaml

    before_install:
      - sudo apt-get update -qq
      - sudo apt-get install -qq sloccount

Example travis-ci config:

.. code-block:: yaml

    language: python
    python:
      - "2.7"
    before_install:
      - sudo apt-get update -qq
      - sudo apt-get install -qq sloccount
      - pip install pep8
    install:
      - npm install -g bower
      - pip install -U -r requirements.txt
    script:
      - ./manage.py test violations projects tasks services app
    after_success:
      - covio
