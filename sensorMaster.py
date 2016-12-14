#!/usr/bin/python

from sense_hat import SenseHat

def get_data():
# Environmental sensors
        humid = sense.humidity
        temp = sense.temperature
        temp_h = sense.get_temperature_from_humidity()
        temp_p = sense.get_temperature_from_pressure()
        press = sense.pressure
        #light = RCtime(gpioPin)
# IMU (inertial measurement unit) sensors
        orient_r = sense.orientation_radians
        orient_d = sense.orientation
        compass = sense.compass
        compass_r = sense.compass_raw
        gyro = sense.gyroscope
        gyro_r = sense.gyroscope_raw
        accel = sense.accelerometer
        accel_r = sense.accelerometer_raw

        return {'environment': {'humidity': humid,
                                'temperature': temp,
                                'temperature_h': temp_h,
                                'temperature_p': temp_p,
                                'pressure': press},
                                #'light': light},
                'imu': {'orientation_rad': orient_r,
                        'orientation_deg': orient_d,
                        'compass': compass,
                        'compass_r': compass_r,
                        'gyroscope': gyro,
                        'gyroscope_r': gyro_r,
                        'accelerometer': accel,
                        'accelerometer_raw': accel_r}}
# Test return
data = get_data()
imu = data['imu']

# Environmetal Data
humidity = imu['humidity']
temperature = imu['temperature']
pressure = imu['pressure']

# Location/Movement Data
compass = imu['compass']
orientation = imu['orientation_deg']
gyroscope = imu['gyroscope']
accelerometer = imu['accelerometer']


