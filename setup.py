from distutils.core import setup

setup(
    name='RtmAPI',
    author='Michael Gruenewald',
    author_email='mail@michaelgruenewald.eu',
    description='API package for rememberthemilk.com',
    long_description=open('README.txt').read(),
    license='License :: OSI Approved :: MIT License',
    url='https://bitbucket.org/michaelgruenewald/rtmapi',
    version='0.2dev',
    packages=['rtmapi',],
    requires=['httplib2 (>=0.6.0)'],
)
