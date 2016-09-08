from setuptools import setup

setup(
    name='morseconverter',
    version='0.1',
    packages = ['morseconverter'],
    package_dir = {'morseconverter' : 'morseconverter'},
    url = 'https://github.com/gokhanm/morseconverter',
    license = 'GPLv3',
    author = 'Gokhan MANKARA',
    author_email = 'gokhan@mankara.org',
    description = 'Real Time Morse Converter',
    entry_points = {
        'console_scripts': [
            'morseconverter = morseconverter.__main__:main',
        ],
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',        
        'License :: OSI Approved :: GPLv3',
    ]
)

