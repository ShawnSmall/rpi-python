#! /usr/bin/env python3
# access the local time and then emit a string formatted as a time stamp every five seconds.

import time
while True:
  timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  print(timestamp)
  time.sleep(5)


