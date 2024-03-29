import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = "url-reputation",
    version = "0.1.0",
    packages = find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=required,

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'urlreputation' package, too:
        'urlreputation': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Cory Walker",
    author_email = "cwalker32@gmail.com",
    description = ("Get number of upvotes for various social sharing sites for"
                   "a given URL."),
    license = "LICENSE.txt",
    keywords = "selenium crawling crawl automate ads landing",
    url = "https://github.com/cmwslw/url-reputation",

    long_description=read('README.md'),
    test_suite = "urlreputation.tests.test_all",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
