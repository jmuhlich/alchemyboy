Automatic generation of the factory_boy_ factories for the SQLAlchemy models.
=============================================================================

.. image:: https://api.travis-ci.org/olegpidsadnyi/alchemyboy.png
   :target: https://travis-ci.org/olegpidsadnyi/alchemyboy
.. image:: https://pypip.in/v/alchemyboy/badge.png
   :target: https://crate.io/packages/alchemyboy/
.. image:: https://coveralls.io/repos/olegpidsadnyi/alchemyboy/badge.png?branch=master
   :target: https://coveralls.io/r/olegpidsadnyi/alchemyboy
.. image:: https://readthedocs.org/projects/alchemyboy/badge/?version=latest
    :target: https://readthedocs.org/projects/alchemyboy/?badge=latest
    :alt: Documentation Status

.. _alchemyboy: http://alchemyboy.readthedocs.org

Install alchemyboy
------------------

::

    pip install alchemyboy

Base model factory
------------------

The base class is abstract. In order to integrate it to your project you have to extend it and
configure the session maker.

myproject/factories/base.py:

.. code-block:: python

    from alchemyboy import BaseModelFactory
    from myproject.sqlachemy import session
    from myproject.book import Book


    class ModelFactory(BaseModelFactory):

        """Model factory class."""

        class Meta:
            session = session
            abstract = True


The base class is configured with the session maker, now you can start registering your factories.

myproject/factories/book.py:

.. code-block:: python

    from myproject.factories.base import ModelFactory
    from myproject.book import Book

    class BookFactory(ModelFactory):

        """Book factory."""

        title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))

        class Meta:
            model = Book


License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_.

© 2015 Oleg Pidsadnyi and others
