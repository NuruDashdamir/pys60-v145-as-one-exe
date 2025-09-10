#
# allcalls.py
#
# Copyright (c) 2006 - 2007 Nokia Corporation
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

import logs
import contacts
#
print "getting CALL logs. be patient..."
evlist = logs.calls(mode='in')
evlist.extend(logs.calls(mode='out'))
#
db = contacts.open()
#
for d in evlist:
    if len(d) > 0:
        print '%s %s' %(d['description'], d['direction'])
        if len(d['name']) < 1:
            if d['contact'] == -1:
                print '%s \'unknown\''%(d['number'])
            else:
                id=d['contact']
                contact=db[id]
                fnames=contact.find('first_name')
                lname=contact.find('last_name')
                if len(fnames)>0 and len(lname)>0:
                    full_name = lname[0].value +' '+fnames[0].value
                    print '%s %s'%(d['number'],full_name)
                else:
                    print '%s N/A'%d['number']
        else:
            print '%s %s'%(d['number'],d['name'])
#
print "done ..."
