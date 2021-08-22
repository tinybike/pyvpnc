#!/usr/bin/env python
import os
import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = "0.2.0"
URL = "https://github.com/tinybike/pyvpnc"
DOWNLOAD_URL = (URL + "/tarball/" + VERSION)
HERE = os.path.dirname(os.path.realpath(__file__))

with codecs.open(os.path.join(HERE, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="vpnc",
    version=VERSION,
    description="Cisco VPN connector",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Jack Peterson",
    author_email="<jack@tinybike.net>",
    maintainer="Jack Peterson",
    maintainer_email="<jack@tinybike.net>",
    license="MIT",
    url=URL,
    download_url=DOWNLOAD_URL,
    packages=["vpnc"],
    keywords = ["vpnc", "vpn", "network", "Cisco", "concentrator"]
)
