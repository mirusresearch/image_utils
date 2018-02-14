from setuptools import setup, find_packages

setup(
    name='mirus_image_utils',
    version='1.0.1',
    description='Mirus Image Utilities',
    author='Frank Henard',
    author_email='frank@mirusresearch.com',
    packages=find_packages(),
    url='https://github.com/mirusresearch/image_utils',
    license='MIT license, see LICENSE.txt',
    install_requires=[
        'Pillow>=1.7.8',
    ]
)
