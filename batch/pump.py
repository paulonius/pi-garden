#!/usr/bin/python3
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

        pi.set_mode(self._sig, pigpio.OUTPUT)

        self._inited = True

    def start_pump(self):
        """
        Starts the pump
        """
        if self._inited:
            self.pi.write(self._sig, pigpio.HIGH)
        else:
            return None

    def stop_pump(self):
        """
        Stops the pump
        """
        if self._inited:
            self.pi.write(self._sig, pigpio.LOW)
        else:
            return None

    def toggle_pump(self):
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

    def get_current_state(self):
        """
        Returns pump current state
        """
        if self._inited:
            state = self.pi.read(self._sig)
            if (state == pigpio.LOW):
                return 'OFF'
            else:
                return 'ON'
        else:
            return None


if __name__ == "__main__":

    import sys
    import time
    import getopt

    usage = 'pump.py [-d <seconds>] [-p <pin>] [-h] [-t toggle]'
    pin = SIG
    duration = 300

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:p:t",
                                   ["help", "duration=", "pin=", "toggle"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    toggle = False
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ('-d', '--duration'):
            duration = int(arg)
        elif opt in ('-p', '--pin'):
            pin = int(arg)
        elif opt in ('-t', '--toggle'):
            toggle = True

    pi = pigpio.pi()
    device = pump(pi, pin)

    if (toggle):
        device.toggle_pump()
        print("Pump is now {}".format(device.get_current_state()))
        sys.exit()

    print("Starting pump for {} seconds".format(duration))
    device.start_pump()
    time.sleep(duration)
    device.stop_pump()
    print("Finished pumping at {}".format(time.ctime()))
    pi.stop()
