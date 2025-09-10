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

# NOTE: Sets/Get the status(1=unread, 0=read) of SMS.
import inbox, appuifw, e32

inb = inbox.Inbox()
sms_ids = inb.sms_messages()
msgs = []
msg_unread = []
msg_read = []

for id in sms_ids:
    msgs.append(inb.content(id))

def setreadunread(message, status):
    global msgs
    i = 0
    for msg in msgs:
        if message == msg:
            if status == 1:
                inb.set_unread(sms_ids[i],1)
            else:
                inb.set_unread(sms_ids[i],0)      
        i = i+1                                
            
def get_readandunreadmessages_inlist():
    global msg_unread
    global msg_read
    msg_unread = []
    msg_read = []
    for id in sms_ids:
        if inb.unread(id):
            msg_unread.append(inb.content(id))
        else:
            msg_read.append(inb.content(id))

def setmessageunread():
    global msg_read
    get_readandunreadmessages_inlist()
    index = appuifw.selection_list(msg_read, 1)
    if index != None and index >= 0:
        print index
        setreadunread(msg_read[index], 1)
        print "Done"

def setmessageread():
    global msg_unread
    get_readandunreadmessages_inlist()
    index = appuifw.selection_list(msg_unread, 1)
    if index != None and index >= 0:
        print index
        setreadunread(msg_unread[index], 0)
        print "Done"

def showmessagestatus():
    global sms_ids
    for id in sms_ids:
        print inb.content(id)[:20]
        print inb.unread(id)

def quit():
    app_lock.signal()
    
appuifw.app.exit_key_handler = quit
appuifw.app.menu = [(u"Mark_read", setmessageread),
                    (u"Mark_unread", setmessageunread),
                    (u"Show_read/unread_status", showmessagestatus)]
app_lock = e32.Ao_lock()
app_lock.wait()
