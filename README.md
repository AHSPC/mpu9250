NOTE: you should probably use the original repo. I only forked this to make a couple quick
modifications and not loose track of them. They are not intended for upstreaming
and this repo will not be kept up to date.

# MPU9250 for MicroPython on the Raspberry Pi Pico
For more information, robotics projects and tutorials visit <www.smarsfan.com>

---

## MPU9250
The MPU9250 combines both the MPU6500 and ak8963 libraries into a single wrapper library.
The MPU6500 provides the accelerometer and gyroscopic measurements.
The ak8963 provides the magnetometer measurements.

---

`test.py` is a test program to show current telemetry data from the sensor

`simple_test.py` is a simpler test program

`ak8962.py` is the magnetometer library, used by the mpu9250 library

`mpu6500.py` is the accelerometer and gyroscope library

`mpu9250.py` is the main library that comines all two libraries together
