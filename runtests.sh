#!/bin/bash
py.test test/*.py --doctest-modules -v --cov vpnc --cov-report term-missing
