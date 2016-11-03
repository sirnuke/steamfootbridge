from setuptools import setup

setup(name='steamfootbridge',
      version='0.0.1',
      packages=['steamfootbridge'],
      scripts=['bin/steamfootbridge'],
      install_requires=[
        'steamodd',
        ],
)
