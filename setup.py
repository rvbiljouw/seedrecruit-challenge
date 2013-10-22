from distutils.core import setup

setup(
    name='seedrecruit-challenge',
    version='1.0',
    author='Rick van Biljouw',
    author_email='rb10054603@gmail.com',
    packages=['seedrecruit', 'seedrecruit.data',
              'seedrecruit.util', 'seedrecruit.test'],
    scripts=['bin/calculator.py'],
    description='A candidate calculator for seedrecruit',
    install_requires=[
        "PyYAML==3.10",
        "argparse==1.2.1",
        "jsonpickle==0.6.1",
        "lxml==3.2.3",
        'nltk==2.0.4'
    ],
)

