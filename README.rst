pyvpnc
======

.. image:: https://badge.fury.io/py/pyvpnc.svg
    :target: http://badge.fury.io/py/pyvpnc

Use VPNC from Python.

Installation
^^^^^^^^^^^^

First you need to install `vpnc`.  On Debian/Ubuntu::

    apt-get install vpnc

On OSX::

    brew install vpnc

Then install pyvpnc using pip::

    pip install vpnc

Usage
^^^^^

.. code-block:: python

    from vpnc import VPNC

    example_config = {
        "IPSec_ID": "my IPSec ID",
        "IPSec_gateway": "my.gateway.com",
        "IPSec_secret": "my IPSec secret",
        "Xauth_username": "my Xauth username",
        "Xauth_password": "my Xauth password",
        "IKE_Authmode": "psk",
        "IKE_DH_Group": "dh2",
        "DNSUpdate": "no",
        "NAT_Traversal_Mode": "force-natt",
        "Local_Port": 0,
        "Cisco_UDP_Encapsulation_Port": 0
    }
    vpnc = VPNC(config=example_config)

    with vpnc.vpn():
        # do stuff on the VPN!

Tests
^^^^^

Unit tests are in the test/ directory.
