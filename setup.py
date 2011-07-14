from setuptools import setup
import codecs

setup(
    name='RtmAPI',
    author='Michael Gruenewald',
    author_email='mail@michaelgruenewald.eu',
    description='API package for rememberthemilk.com',
    long_description=codecs.getreader('utf-8')(open('README', 'rb')).read(),
    license='License :: OSI Approved :: MIT License',
    url='https://bitbucket.org/michaelgruenewald/rtmapi',
    version='0.5.1',
    packages=['rtmapi',],
    requires=['httplib2 (>=0.6.0)'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
    ],
    use_2to3 = True,
)
