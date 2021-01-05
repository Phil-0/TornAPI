from setuptools import setup, find_packages

setup(
    name='TornAPI',
    version='0.1',
    description='An API wrapper for Torn City.',
    url='https://github.com/Phil-0/TornAPI/',
    license='GPLv3',
    author='Phil-0',
    packages=find_packages(),
    install_requires=['requests~=2.5.4.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ]
)
