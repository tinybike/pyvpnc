#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="vpnc",
    version="0.1.0",
    description="Use VPNC from Python",
    author="Jack Peterson",
    author_email="<jack@tinybike.net>",
    maintainer="Jack Peterson",
    maintainer_email="<jack@tinybike.net>",
    license="MIT",
    url="https://github.com/tinybike/pyvpnc",
    download_url = "https://github.com/tinybike/pyvpnc/tarball/0.1.0",
    packages=["vpnc"],
    keywords = ["vpnc", "vpn", "network", "networking"]
)
