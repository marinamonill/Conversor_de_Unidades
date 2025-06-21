from setuptools import setup, find_packages

setup(
    name='conversor_unidades',
    version='0.1.0',
    description='Conversor de unidades de longitud, temperatura y masa',
    author='Marina Monill',
    author_email='marinamonill@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
