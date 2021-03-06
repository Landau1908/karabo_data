#!/usr/bin/env python
import os.path as osp
import re
from setuptools import setup, find_packages
import sys


def get_script_path():
    return osp.dirname(osp.realpath(sys.argv[0]))


def read(*parts):
    return open(osp.join(get_script_path(), *parts)).read()


def find_version(*parts):
    vers_file = read(*parts)
    match = re.search(r'^__version__ = "(\d+\.\d+\.\d+)"', vers_file, re.M)
    if match is not None:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(name="karabo_data",
      version=find_version("karabo_data", "__init__.py"),
      author="European XFEL GmbH",
      author_email="cas-support@xfel.eu",
      maintainer="Thomas Michelat",
      url="https://github.com/European-XFEL/karabo_data",
      description="Tools to read and analyse data from European XFEL ",
      long_description=read("README.md"),
      license="BSD-3-Clause",
      packages=find_packages(),
      entry_points={
          "console_scripts": [
              "lsxfel = karabo_data.lsxfel:main",
              "karabo-bridge-serve-files = karabo_data.export:main",
              "karabo-data-validate = karabo_data.validation:main",
          ],
      },
      install_requires=[
          'fabio',
          'h5py>=2.7.1',
          'karabo-bridge',
          'matplotlib',
          'msgpack>=0.5.4',
          'msgpack-numpy>=0.4.3',
          'numpy',
          'pandas; python_version>="3.5"',
          'pandas<0.21; python_version<"3.5"',
          'pyzmq>=17.0.0',
          'xarray',
      ],
      extras_require={
          'docs': [
              'sphinx',
              'nbsphinx',
              'ipython',  # For nbsphinx syntax highlighting
          ],
          'test': [
              'pytest',
              'pytest-cov',
              'nbval',
              'testpath',
          ]
      },
      python_requires='>=3.4',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Physics',
      ]
)
