from setuptools import setup


setup(
    name='MangasReaderDownloader',
    version='0.0.1',
    py_modules=['workers'],
    install_requirements=[
        'requests',
        'lxml',
        'pytest',
        'betamax',
        'betamax-serializers',
        'regex',
        'click',
    ],
)