#!/usr/bin/env python3
from setuptools import setup


def readme():
    with open("README.rst", "r") as f:
        return f.read()


setup(
    name="muchnotify",
    version="0.1",
    description="Display desktop notifications for unread mail in notmuch " "database",
    long_description=readme(),
    author="Kiprianas Spiridonovas and Julian Hauser",
    author_email="julian@julianhauser.com",
    url="https://github.com/jghauser/muchnotify",
    license="GPL3",
    packages=["muchnotify"],
    scripts=["bin/muchnotify"],
    install_requires=[
        "notmuch",
        "pygobject",
    ],
)
