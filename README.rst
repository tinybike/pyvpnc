pyvpnc
======

.. image:: https://badge.fury.io/py/vpnc.svg
    :target: http://badge.fury.io/py/vpnc

pyvpnc is a Python connector for `vpnc <http://linux.die.net/man/8/vpnc>`_, a Cisco VPN concentrator/router client.  The vpnc daemon requires elevated permissions to run; you will be prompted for your admin/sudo password if needed.

Installation
^^^^^^^^^^^^

First, install vpnc.  On Debian/Ubuntu::

    apt-get install vpnc

On OSX::

    brew install vpnc

Then install pyvpnc using pip::

    pip install vpnc

Usage
^^^^^

.. code-block:: python

    from vpnc import VPNC

    vpn_client = VPNC(config={
        "IPSec_ID": "my IPSec ID",
        "IPSec_gateway": "my.gateway.com",
        "IPSec_secret": "my IPSec secret",
        "Xauth_username": "my Xauth username",
        "Xauth_password": "my Xauth password",
        "IKE_Authmode": "psk"
    })

    with vpn_client.vpn():
        # do stuff on the VPN!

Tests
^^^^^

Unit tests are in the test/ directory.
