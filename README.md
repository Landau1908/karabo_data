# h5tools-py
Python tools for reading European XFEL's h5 files


Installing
==========
This package is dependent on h5py and numpy.

Installing h5py on EuXFEL computer may require installing the *libhdf5-dev*
package from the ubuntu repositories.

Contributing
===========

Tests
-----
The naming convention is inline with EuXFEL's internal conventions
of *filename*_tests.py

Each source file should have a corresponding *_tests.py file in the *tests/*
directory.

Each test function should have a one line docstring describing the test in an
intuitive way.

Tests can be run as follows:

    nosetests -v tests
