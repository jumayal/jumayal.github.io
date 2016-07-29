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
import logging
import jinja2
import os
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('hello.html')
    self.response.write(template.render())

class SecretHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("here is my log statement")
        self.response.write('What is the passcode?')
class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("If you are reading this, I was just kidding. Do come back")
        self.response.write('See you never. Dont come back agian!!!!')

class MeHandler(webapp2.RequestHandler):
    def get(self):
        ltemplate = jinja_environment.get_template('page copy.html')
        self.response.write(ltemplate.render())

app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/goodebye', GoodbyeHandler ),
    ('/secretentrance', SecretHandler),
    ('/', MainHandler)
], debug=True)
