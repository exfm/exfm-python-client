from setuptools import setup

version = '0.1-dev'

setup(name='exfm-client',
    version=version,
    description='Python client for exfm API',
    long_description=open('./README.md').read(),
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        'License :: OSI Approved :: BSD License',
        ],
    keywords='sailthru api',
    author='Prajwal Tuladhar',
    author_email='praj@sailthru.com',
    url='https://github.com/exfm/exfm-python-client',
    license='BSD',
    packages=['exfm'],
    include_package_data=True,
    zip_safe=True)
