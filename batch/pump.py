#!/usr/bin/python3
import pigpio
import configparser
import os

dirname = os.path.dirname(__file__)
if "pi-garden" in dirname:
    config_file = os.path.join(dirname, '../config.ini')
else:
    config_file = os.path.join(os.environ['HOME'], 'pi-garden/config.ini')

config = configparser.ConfigParser()
config.read(config_file)

SIG = int(config['SENSORS']['Pump'])


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

        pi.set_mode(self._sig, pigpio.OUTPUT)

        self._inited = True

    def start(self):
        """
        Starts the pump
        """
        if self._inited:
            self.pi.write(self._sig, pigpio.HIGH)
        else:
            return None

    def stop(self):
        """
        Stops the pump
        """
        if self._inited:
            self.pi.write(self._sig, pigpio.LOW)
        else:
            return None

    def toggle(self):
        """
        Toggles pump function
        """
        if self._inited:
            state = self.pi.read(self._sig)
            if (state == pigpio.LOW):
                self.pi.write(self._sig, pigpio.HIGH)
            else:
                self.pi.write(self._sig, pigpio.LOW)
        else:
            return None

    def is_running(self):
        """
        Returns pump current state
        """
        if self._inited:
            state = self.pi.read(self._sig)
            if (state == pigpio.LOW):
                return False
            else:
                return True
        else:
            return None


if __name__ == "__main__":

    import sys
    import time
    import getopt

    usage = 'pump.py [-d <seconds>] [-p <pin>] [-h] [-t toggle] [-s status]'
    pin = SIG
    duration = 300

    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "hd:p:ts",
            ["help", "duration=", "pin=", "toggle", "status"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    program = ""
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ('-d', '--duration'):
            duration = int(arg)
        elif opt in ('-p', '--pin'):
            pin = int(arg)
        elif opt in ('-t', '--toggle'):
            program = "toggle"
        elif opt in ('-s', '--status'):
            program = "status"

    pi = pigpio.pi()
    device = pump(pi, pin)

    if program == "toggle":
        device.toggle()
        state = "ON" if device.is_running() else "OFF"
        print("Pump is now {}".format(state))
        sys.exit()
    elif program == "status":
        state = "ON" if device.is_running() else "OFF"
        print("Pump is currently {}".format(state))
        sys.exit()
    else:
        try:
            print("Starting pump for {} seconds".format(duration))
            device.start()
            time.sleep(duration)
            device.stop()
            print("Finished pumping at {}".format(time.ctime()))
            pi.stop()
        except KeyboardInterrupt:
            print("Pumping interrupted by User")
            device.stop()
            pi.stop()
