#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class Email(object):
    def __init__ (self, subject, unread, notspam):
        self.subject = subject
        self.unread = unread
        self.notspam = notspam

class listHandler(webapp2.RequestHandler):
    def get(self):
        emails=[
            Email("Hello",True,True),
            Email("Welcome to CSSI",False,True),
            Email("Send Money Now",True,True)
        ]
        template = jinja_environment.get_template('list.html')
        vals={'emails': emails}
        self.response.write(template.render(vals))
class singleHandler(webapp2.RequestHandler):
    def get(self):
        subject = self.request.get('subject')
        notspam = self.request.get('notspam')
        template = jinja_environment.get_template('email.html')
        self.response.write(template.render({'subject': subject, 'notspam': notspam}))

app = webapp2.WSGIApplication([
    ('/', listHandler),
    ('/email', singleHandler)
], debug=True)
