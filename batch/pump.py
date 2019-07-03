#!/usr/bin/python3

import time
import pigpio

SIG = 18


class pump:
    """
    This class helps with the operating of a small pump, or
    any other piece of equipment connected to a pin via a
    relay.
    """

    def __init__(self, pi, sig):
        self.pi = pi
        self._sig = sig

        self._sig_mode = pi.get_mode(self._sig)
