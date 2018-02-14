from setuptools import setup, find_packages

setup(
    name='image_utils_fdh',
    version='1.0.0',
    description='Mirus Image Utilities',
    author='Frank Henard',
    author_email='frank@mirusresearch.com',
    packages=find_packages(),
    url='https://github.com/mirusresearch/image_utils_fdh',
    license='MIT license, see LICENSE',
    install_requires=[
        'Pillow>=1.7.8',
    ],
    py_modules=['image_utils_fdh'],
)
