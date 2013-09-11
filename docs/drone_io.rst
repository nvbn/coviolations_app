********************
Using with drone.io
********************

At the end of project script add

.. code-block:: bash

    pip install coviolations_app
    COVIO_TOKEN="token" covio

Replace `token` with project token from project page.

Example project script config:

.. code-block:: bash

   sudo apt-get update -qq
   sudo apt-get install -qq sloccount
   pip install pep8
   pip install -U -r requirements.txt
   nosetests 2>test_out
   COVIO_TOKEN="token" covio
