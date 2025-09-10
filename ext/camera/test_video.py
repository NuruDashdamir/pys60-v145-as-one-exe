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
# test_video.py
#

import appuifw
import camera
import e32

def finder_cb(im):
    appuifw.app.body.blit(im)

appuifw.app.body=appuifw.Canvas()
camera.start_finder(finder_cb)

def video_cb(err, code):
    print "error: ", err, " code: ", code

camera.start_record("c:\\data\\video\\test.3gp", video_cb)
e32.ao_sleep(10)
camera.stop_record()
camera.stop_finder()
print "Done."
