# Copyright (c) 2005-2008 Nokia Corporation
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
import appuifw, e32, messaging
def msg1():
    print "Sending SMS...."
    messaging.sms_send("1234567890",u"message has send with inbuild script",'7bit', None, "Marry")
    # Instead of "1234567890", put number to whom you want to send message.
    appuifw.note(u"Sms sent, check sent item")

def msg2():
    msg = appuifw.multi_query(u"Phone Number", u"Message")
    if msg:
        phoneNumber, Message = msg
        resName = appuifw.multi_query(u"FirstName", u"lastName")
    if resName:
        fname, sname = resName
        name = sname+" "+fname
    else:
        appuifw.note(u"cancel!")
    print "Sending SMS: " + Message
    messaging.sms_send(phoneNumber,Message,'7bit',None,name)
    appuifw.note(u"Sms Sent, check sent item")
    
def msg3():
    msg = appuifw.multi_query(u"Phone Number", u"Message")
    if msg:
        phoneNumber, Message = msg
    else:
        appuifw.note(u"cancel!")
    print "Sending SMS: " + Message
    messaging.sms_send(phoneNumber,Message)
    appuifw.note(u"Sms Sent, check sent item")

def send_long_message():
    print "Sending SMS..."
    # This message is of length 39015 charcters.
    msg = u"hello"
    txt = msg * 7802
    txt = txt + u"Nokia"
    print txt
    # Instead of "1234567890", put number to whom you want to send message.
    messaging.sms_send("1234567890", txt, '7bit', None, "Marry")
    appuifw.note(u"Sms sent, check sent item")
    print "message length = ", len(txt)
    
def quit():
    app_lock.signal()
appuifw.app.title = u"test_messaging"
appuifw.app.screen = "normal"
appuifw.app.menu = [(u"HardCodedMessage",msg1),(u"UserInputAndMessage",msg2),(u"WithoutReciNameMessage",msg3),(u"HardCodedLongMessage",send_long_message)]
appuifw.app.exit_key_handler = quit

app_lock = e32.Ao_lock()
app_lock.wait()


