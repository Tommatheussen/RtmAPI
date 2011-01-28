from distutils.core import setup

setup(
    name='RtmAPI',
    author='Michael Gruenewald',
    author_email='mail@michaelgruenewald.eu',
    description='API package for rememberthemilk.com',
    long_description=open('README').read(),
    license='License :: OSI Approved :: MIT License',
    url='https://bitbucket.org/michaelgruenewald/rtmapi',
    version='0.4',
    packages=['rtmapi',],
    requires=['httplib2 (>=0.6.0)'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
    ],
)
