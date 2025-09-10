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

import calendar
import thread
import e32
import appuifw

def kill_reference(ref):
    print "Killing reference:"
    e32.ao_sleep(1)
    ref=None
    print "Killed reference."
    e32.ao_sleep(1)

def test_destroy_from_foreign_thread():
    thread.start_new_thread(kill_reference, (calendar.open(),))
    print "Started reference killer thread."

def access_db(db):
    print "Accessing db:"
    e32.ao_sleep(1)
    print "Number of items in db:",len(db)
    print "Accesssed db."
    e32.ao_sleep(1)

def test_access_from_foreign_thread():
    thread.start_new_thread(access_db, (calendar.open(),))

quitlock = e32.Ao_lock()
appuifw.app.menu=[(u'Destroy in foreign thread', 
                   test_destroy_from_foreign_thread),
                  (u'Access in foreign thread',
                   test_access_from_foreign_thread),
                  (u'Exit',
                   quitlock.signal)]
quitlock.wait()
