#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation cla$

time.sleep(3)

print '0. taking off till 10m'
drone.take_off(10.0)
print 'taking down 5 m'
drone.position_set(8.0, 6.0, 5, relative=True)
drone.position_set(-8.0, 6.0, 0, relative=True)
drone.position_set(0, -10, 0, relative=True)

print ' 4. Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()