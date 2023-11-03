# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "midjourney-api-client"
VERSION = "1.0.1"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python_dateutil >= 2.5.3",
    "pydantic >= 1.10.5, < 2",
    "aenum >= 3.1.11"
]

setup(
    name=NAME,
    version=VERSION,
    license="ISC",
    author="Use API",
    author_email="support@useapi.net",
    url="https://useapi.net",
    keywords=["Midjourney", "API", "useapi.net"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    description="Midjourney API by useapi.net",
    long_description_content_type='text/markdown',
    long_description=open("README.md").read(),
    package_data={"midjourney_api_client": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",  
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3", 
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],    
)
