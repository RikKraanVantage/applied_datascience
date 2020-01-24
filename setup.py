from setuptools import find_packages, setup

setup(
    name='applied_datascience',
    packages=find_packages(),
    version='0.0.1',
    description='Applied Data Scienec',
    author='Vantage AI',
    license='MIT',
    long_description="README.md",

    python_requires='>3.5',

    install_requires=[
                     "click",
                     "python-dotenv>=0.5.1",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
