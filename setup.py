from setuptools import setup
VERSION = '0.0.1'
DESCRIPTION = 'This is a package for audio input and output using python.'
LONG_DESCRIPTION = 'This is a package for audio input and output using python, written in python.'

# Setting up
setup(
    name="AwazIO",
    version=VERSION,
    author="Shivansh Mathur",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['AwazIO'],
    install_requires=['gtts','translate','SpeechRecognition'],
    keywords=['python', 'audio', 'mic', 'speak', 'Voice Recognition', 'AI']
)