#!/usr/bin/env python
"""Unit tests for vpnc."""
import sys
import os
import json
import subprocess
import unittest

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
sys.path.insert(0, ROOT)

from vpnc import VPNC

class TestVPNC(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(HERE, "config.json")) as f:
            self.vpnc = VPNC(config=json.load(f))
        assert(self.vpnc is not None)
        assert(self.vpnc.config is not None)
        assert(type(self.vpnc.config) == dict)
        assert(set(self.vpnc.config.keys()) >= set(("IPSec_ID",
                                                    "IPSec_gateway",
                                                    "IPSec_secret",
                                                    "Xauth_username",
                                                    "Xauth_password",
                                                    "IKE_Authmode")))
        assert(self.vpnc.config_file == "tempvpnc.conf")
        assert(self.vpnc.temp_config_path == os.path.join(ROOT,
                                                          "vpnc",
                                                          "tempvpnc.conf"))
        assert(self.vpnc.config_folder == "/etc/vpnc")
        assert(self.vpnc.config_path == "/etc/vpnc/tempvpnc.conf")

    def test_create_config_file(self):
        self.vpnc.create_config_file()
        assert(os.path.isfile(self.vpnc.temp_config_path))

    def test_move_config_file(self):
        self.vpnc.create_config_file()
        self.vpnc.move_config_file()
        assert(os.path.isfile(self.vpnc.temp_config_path) == False)
        subprocess.check_call(["sudo", "cat", self.vpnc.config_path])

    def test_remove_config_file(self):
        assert(self.vpnc.remove_config_file() == False)
        self.vpnc.create_config_file()
        self.vpnc.move_config_file()
        assert(self.vpnc.remove_config_file())

    def test_connect(self):
        self.vpnc.connect()
        assert(os.path.isfile(self.vpnc.temp_config_path) == False)
        subprocess.check_call(["ifconfig", "tun"])
        subprocess.check_call(["sudo", "cat", self.vpnc.config_path])
        subprocess.check_call(["pidof", "vpnc"])

    def test_disconnect(self):
        self.vpnc.connect()
        self.vpnc.disconnect()
        assert(os.path.isfile(self.vpnc.temp_config_path) == False)
        assert(subprocess.call(["sudo", "cat", self.vpnc.config_path]) == 1)

    def test_vpn(self):
        with self.vpnc.vpn():
            subprocess.check_call(["ifconfig", "tun"])
            assert(os.path.isfile(self.vpnc.temp_config_path) == False)
            subprocess.check_call(["sudo", "cat", self.vpnc.config_path])
            subprocess.check_call(["pidof", "vpnc"])

    def tearDown(self):
        if subprocess.call(["pidof", "vpnc"]) == 0:
            self.vpnc.disconnect()
        if os.path.isfile(self.vpnc.temp_config_path):
            os.remove(self.vpnc.temp_config_path)
        try:
            subprocess.check_call(["sudo", "rm", self.vpnc.config_path])
        except subprocess.CalledProcessError:
            pass
        assert(os.path.isfile(self.vpnc.temp_config_path) == False)
        assert(os.path.isfile(self.vpnc.config_path) == False)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVPNC)
    unittest.TextTestRunner(verbosity=2).run(suite)
