from setuptools import setup, find_packages

setup(
    name='phil0-tornapi',
    version='0.2.2',
    description='An API wrapper for Torn City.',
    url='https://github.com/Phil-0/TornAPI/',
    license='GPLv3',
    author='Phil-0, PhilMe [2590086]',
    packages=find_packages(),
    install_requires=['requests~=2.25.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ]
)
