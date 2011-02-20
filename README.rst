================================
MadPub.org: Mobile Web Interface
================================

This project contains a mobile web user interface frontend for the `MadPub.org`_
project.


Goals
-----

* Use a Python framework to handle creating the forms and sending the data to
  the server.
* Use `jQuery Mobile`_ to provide the interface.
* Make the application available to be used offline, then being able to send
  the data when Internet connectivity is established.


HOWTO run the application
-------------------------

Here's how to install using `virtualenvwrapper`_, because it simplifies things::

    $ pip install virtualenvwrapper
    $ mkvirtualenv madpub_django
    (madpub_django) $ cdvirtualenv
    (madpub_django) $ git clone git://github.com/malept/mad-django.git
    (madpub_django) $ cd mad-django
    (madpub_django) $ pip install -r requirements.txt
    (madpub_django) $ python setup.py install
    (madpub_django) $ python madpub/bin/manage.py runserver

If you want to work on the application, replace ``python setup.py install`` with
``python setup.py develop``.


TODO
----

* Actually send the data to the server, using `httplib2`_.
* Use `evercookie`_ to store data locally.
* Add `HTML5 offline web application`_ support.


.. _MadPub.org: http://wiki.rhok.org/MadPub.org
.. _jQuery Mobile: http://jquerymobile.com/
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/
.. _httplib2: http://httplib2.googlecode.com/
.. _evercookie: http://samy.pl/evercookie/
.. _HTML5 offline web application: http://diveintohtml5.org/offline.html
