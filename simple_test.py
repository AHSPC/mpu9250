

from machine import SoftI2C, Pin
import math
from mpu9250 import MPU9250
from ak8963 import AK8963, MODE_CONTINOUS_MEASURE_2
from time import sleep

# addresses 
MPU = 0x68
sda = Pin(0)
scl = Pin(1)
# 
# create the I2C
i2c = SoftI2C(scl=scl, sda=sda)

# Scan the bus
print(i2c.scan())
m = MPU9250(i2c, ak8963=AK8963(i2c, mode=MODE_CONTINOUS_MEASURE_2))

m.ak8963.calibrate(count=500, delay=50)

while True:
    # print("x", m.acceleration[0],"y", m.acceleration[1], "z", m.acceleration[2])
    # print("gyro: ", m.gyro)
    mag = m.magnetic
    print("angle: ", math.degrees(math.atan2(mag[1], mag[0])))
