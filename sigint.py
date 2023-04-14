#!/user/bin/env python

import signal, time

def handler (signum, time):
    print ("\nI got a SIGINT, but I'm not stopping")

signal.signal(signal.SIGINT, handler)

i = 1

while True:
    time.sleep(.3)
    print("\r{}".format(i),end="")
    i += 1