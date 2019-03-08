import setuptools

# quick instructions in case forgetten
# only reupload to pypi if new, fully completed features have been implemented and tested
# it's better to wait a few days, just for the BotD
# edit setup.py (this file) and bump the version number
# the version number reads like follows:
# Major Release . Feature . Bug fixes
# run the markdown to rst script
# $ python rst_helper.py
# git add and git commit change to github, merge with master
# now, clear out build/* and dist/*
# rm -rf dist build
# cd to the project folder and type in terminal:
# $ python setup.py develop
# $ python setup.py sdist bdist_wheel
# after that's done, type:
# $ twine upload dist/*
# after it's uploaded, install the new version:
# $ pip install --update structured-markdown

with open("README.rst", "r") as fin:
    long_description = fin.read()

setuptools.setup(
    name="structured_markdown",
    version="0.1.1",
    description="Add an extra dimension to your markdown documents",
    long_description=long_description,
    url="https://github.com/Structured-Markdown/structured_markdown",
    author="Structured-Markdown",
    author_email="isaacimagine@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        "mistune",
        "m2r"
    ],
    zip_safe=False,
)
