from setuptools import setup

setup(
    name='IVObject',
    version='1.0.2',
    license='MIT',
    author='Unay Santisteban',
    author_email='usantisteban@othercode.es',
    description='A Immutable Value Object implementation in Python.',
    long_description=open('README.md').read(),
    url='https://github.com/othercodes/ivobject',
    download_url='https://github.com/othercodes/ivobject/releases',
    keywords=['python', 'ddd', 'value object', 'hexagonal architecture'],
    packages=['ivobject'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
