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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('madlibs.html')
        self.response.write(template.render())
    def post(self):
        noun1= self.request.get("noun1")
        activity= self.request.get("activity")
        teacher= self.request.get("teacher")
        celebrity= self.request.get("celebrity")
        show= self.request.get("show")
        fun= self.request.get("fun")
        template = jinja_environment.get_template('results.html')
        vals= {'activity':activity,'noun1':noun1,'teacher':teacher,'celebrity':celebrity,'show':show,'fun':fun }
        self.response.write(template.render(vals))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
