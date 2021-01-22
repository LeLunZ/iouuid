from distutils.core import setup
from pathlib import Path

try:
    this_directory = Path(__file__).absolute().parent
    with open((this_directory / 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='io-uuid',
    packages=['iouuid'],
    version='0.0.1',
    license='BSD 3-Clause',
    description='A file name generator',
    author='LeLunZ',
    author_email='l.accounts@pm.me',
    url='https://github.com/LeLunZ/iouuid',
    download_url='https://github.com/LeLunZ/iouuid/archive/0.0.1.tar.gz',
    keywords=['iouuid', 'uuid', 'name generator', 'file name generator'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
