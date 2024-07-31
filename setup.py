from setuptools import setup, find_packages

setup(
    name='HeliosJournal',
    version='1.0.0',
    author='Errahum',
    description='A simple journal app',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Errahum/Helios-Journal',
    packages=find_packages(),
    install_requires=[
        'time',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'helios_journal=main_heliosjournal:main_heliosjournal',
        ],
    },
    include_package_data=True,
    license='MIT',
)
