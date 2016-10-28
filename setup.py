# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

install_requires = [
    'Keras',
    'python-qt'
    ]

setup(
    name='NNTester',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='A desktop app for Keras based digit recognition',

    # The project's main homepage.
    url='https://github.com/cgianmarco/quick-nn-tester.git',

    # Author details
    author='Gianmarco Caramitti',
    author_email='c.giammy95@gmail.com',

    # Choose your license
    license='MIT',

    # What does your project relate to?
    keywords='keras testing neural network',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['NNTester'],

    install_requires=install_requires,

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'data': ['weights.best.conv.hdf5'],
    #     'data': ['weights.best.conv2.hdf5']
    # },

    data_files=[('data', ['data/weights.best.conv.hdf5', 'data/weights.best.conv2.hdf5'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
