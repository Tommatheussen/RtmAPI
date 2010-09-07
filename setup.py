from distutils.core import setup

setup(
    name='RtmAPI',
    author='Michael Gruenewald',
    author_email='mail@michaelgruenewald.eu',
    url='https://bitbucket.org/michaelgruenewald/rtmapi',
    version='0.1',
    packages=['rtmapi',],
    license='License :: OSI Approved :: MIT License',
    long_description=open('README.txt').read(),
    requires=['httplib2 (>=0.6.0)'],
)
