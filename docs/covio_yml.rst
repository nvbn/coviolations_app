***************
.covio.yml file
***************

In this file you need to specifie project name and violations.
Example for django project:

.. code-block:: yaml

    violations:
      pep8: pep8 . --exclude='*migrations*'
      sloccount: sloccount .

You can use full-length violation declaration:

.. code-block:: yaml

    violations:
        pep8: pep8 . --exclude='*migrations*'
        pip_review:
            command: pip-review
            nofail: true

`nofail` - set force success status to violation.
