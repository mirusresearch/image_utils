from setuptools import setup

setup(
    name='image_utils',
    version='1.0.1',
    description='Mirus Image Utilities',
    author='Frank Henard',
    author_email='frank@mirusresearch.com',
    packages=['image_utils'],
    url='https://github.com/mirusresearch/image_utils',
    license='MIT license, see LICENSE.txt',
    install_requires=[
        'Pillow>=1.7.8',
    ]
)
