import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web_tester",
    version="0.0.1",
    author="Vishnu Chegondi",
    author_email="vishnu.chegondi@gmail.com",
    description="A simple browser to simplify complex selenium codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishnu-chegondi/web_tester",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium >= 3.13.0'
    ],
    classifiers=[
        "Intended Audience :: Developers"
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)