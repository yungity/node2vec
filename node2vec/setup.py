from distutils.core import setup
import setuptools

setup(
    name='node2vec',
    packages=['node2vec'],
    version='0.3.2',
    description='Implementation of the node2vec algorithm.',
    author='Elior Cohen',
    author_email='elior.cohen.p@gmail.com',
    license='MIT',
    url='https://github.com/eliorc/node2vec',
    install_requires=[
        'networkx',
        'gensim',
        'numpy',
        'tqdm',
        'joblib>=0.13.2'
    ],
    keywords=['machine learning', 'embeddings'],
)