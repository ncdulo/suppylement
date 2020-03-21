from setuptools import setup


setup(
        name='suppylement',
        version='0.0.1',
        py_modules=['cli'],
        install_requires=[
            'numpy',
            'pandas',
        ],
        entry_points = {
                'console_scripts':
                    ['suppylement=suppylement.main:main'],
            }
    )
