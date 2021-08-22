#!/usr/bin/env python
"""Connects to a remote Cisco VPN using vpnc.

Usage:

    from vpnc import VPNC

    vpn_client = VPNC(config={
        "IPSec_ID": "my IPSec ID",
        "IPSec_gateway": "my.gateway.com",
        "IPSec_secret": "my IPSec secret",
        "Xauth_username": "my Xauth username",
        "Xauth_password": "my Xauth password",
        "IKE_Authmode": "psk",
    })

    with vpn_client.vpn():
        # do stuff on the VPN!

(c) Jack Peterson (jack@tinybike.net), 8/31/2015

"""
import sys
import os
import subprocess
from contextlib import contextmanager

HERE = os.path.dirname(os.path.realpath(__file__))

class VPNC(object):

    def __init__(self, config=dict(),
                       config_file="tempvpnc.conf",
                       config_folder=None):
        self.config = config
        self.config_file = config_file
        self.temp_config_path = os.path.join(HERE, self.config_file)
        self.config_folder = config_folder
        if config_folder is None:
            if sys.platform.startswith("linux"):
                self.config_folder = "/etc/vpnc"
            elif sys.platform.startswith("darwin"):
                self.config_folder = "/usr/local/etc/vpnc"
        self.config_path = os.path.join(self.config_folder, self.config_file)

    def create_config_file(self):
        """Creates a formatted VPNC config file."""
        with open(self.temp_config_path, "w+") as f:
            f.write("IPSec gateway {}\n".format(self.config["IPSec_gateway"]))
            f.write("IPSec ID {}\n".format(self.config["IPSec_ID"]))
            f.write("IPSec secret {}\n".format(self.config["IPSec_secret"]))
            f.write("IKE Authmode {}\n".format(self.config["IKE_Authmode"]))
            f.write("Xauth username {}\n".format(self.config["Xauth_username"]))
            f.write("Xauth password {}\n".format(self.config["Xauth_password"]))

    def move_config_file(self):
        """Moves the VPNC config file to /etc/vpnc (Linux) or
        /usr/local/etc/vpnc/ (OSX).
        """
        subprocess.check_call(["sudo", "mv", self.temp_config_path, self.config_folder])
        subprocess.check_call(["sudo", "chown", "root:root", self.config_path])
        subprocess.check_call(["sudo", "chmod", "600", self.config_path])

    def remove_config_file(self):
        """Removes the auto-generated VPNC config file."""
        try:
            subprocess.check_call(["sudo", "rm", self.config_path])
            return True
        except subprocess.CalledProcessError:
            return False

    def connect(self):
        """Connects to VPNC."""
        self.create_config_file()
        self.move_config_file()
        subprocess.check_call(["sudo", "vpnc", "tempvpnc"], env=os.environ)

    def disconnect(self):
        """Disconnects from VPNC."""
        subprocess.call(["sudo", "vpnc-disconnect"])
        self.remove_config_file()

    @contextmanager
    def vpn(self):
        """Creates VPN context."""
        self.connect()
        yield
        self.disconnect()
