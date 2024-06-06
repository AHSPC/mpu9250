from machine import SoftI2C, Pin
import math
from mpu9250 import MPU9250

# addresses 
MPU = 0x68
sda = Pin(0)
scl = Pin(1)

# create the I2C
i2c = SoftI2C(scl=scl, sda=sda)

# Scan the bus
print(i2c.scan())
m = MPU9250(i2c)

m.ak8963.calibrate(count=500, delay=50)

while True:
    print("accel: ", m.acceleration)
    print("gyro: ", m.gyro)
    mag = m.magnetic
    print("mag: ", mag, " angle: ", math.degrees(math.atan2(mag[1], mag[0])))
