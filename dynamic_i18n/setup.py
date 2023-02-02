from setuptools import setup, find_packages

setup(
    name='dynamic_class_i18n',
    version='0.1',
    packages=find_packages(),
    author='Jeferson Peter',
    author_email='jeferson.peter@protonmail.com',
    description='A simple dynamic class to create i18n configurations from a json file or dictionary.',
    install_requires=[],  # List of dependencies
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)