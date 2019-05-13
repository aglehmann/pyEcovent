from setuptools import setup

long_description = None

with open("README.md", 'r') as fp:
    long_description = fp.read()

setup(
    name = 'pyEcovent',
    packages = ['ecovent'],
    version='0.8.1',
    description='Python3 library for single-room energy recovery ventilators from Vents / Blauberg / Flexit',
    long_description=long_description,
    python_requires='>=3.6.7',
    author='Aleksander Lehmann',
    author_email='aleksander@flovik.no',
    url='https://github.com/aglehmann/pyEcovent',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
