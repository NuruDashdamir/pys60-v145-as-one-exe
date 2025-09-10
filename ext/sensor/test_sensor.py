#
# test_sensor.py
#
# Copyright (c) 2007 Nokia Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sensor
from sensor import orientation

import e32

orientations = {
	orientation.TOP:    'top',
	orientation.BOTTOM: 'bottom',
	orientation.LEFT:   'left',
	orientation.RIGHT:  'right',
	orientation.FRONT:  'front',
	orientation.BACK:   'back' }

def print_orientation(orientation_value):
	print 'new orientation: ', orientations[orientation_value]
	
def print_tapped(dummy):
	print 'tapped'

sensors = sensor.sensors()

acc_sensor_data = sensors['AccSensor']
tap_sensor_data = sensors['Tapping sensor']

orientation_sensor = sensor.Sensor(acc_sensor_data['id'], acc_sensor_data['category'])
tap_sensor = sensor.Sensor(tap_sensor_data['id'], tap_sensor_data['category'])

orientation_sensor.set_event_filter(sensor.OrientationEventFilter())

print 'testing tapping and orientation change sensors for 15 seconds...'

orientation_sensor.connect(print_orientation)
tap_sensor.connect(print_tapped)

e32.ao_sleep(15)

orientation_sensor.disconnect()
tap_sensor.disconnect()

print 'sensor test finished'
