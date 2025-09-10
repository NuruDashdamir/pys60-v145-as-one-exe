# Copyright (c) 2008 Nokia Corporation
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

import e32, appuifw, socket

app_lock = e32.Ao_lock()
appuifw.app.title = u'Access point problem'
appuifw.app.exit_key_handler = lambda:app_lock.signal()
apid = socket.select_access_point()
apo = socket.access_point(apid)
socket.set_default_access_point(apo)

try:
    import urllib
    f = urllib.urlopen("http://www.yahoo.com")
    print f.read()
except Exception, e:
    print 'Exception: ', e

app_lock.wait()
apo.stop()
