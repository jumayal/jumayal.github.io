import webapp2
import jinja2
import os
from google.appengine.ext import ndb

#agpkZXZ-cm9zdGVychQLEgdTdHVkZW50GICAgICAwJ8IDA

#URL Safe Key Cheat Sheet

#URL Safe Key:agpkZXZ-cm9zdGVychQLEgdTdHVkZW50GICAgICAwJ8IDA
# e # This is an entity
#urlsafe_key = e.key.urlsafe()
#
#Url Safe String => entity
#urlsafe_key # This is a String
#key = ndb.Key(urlsafe=urlsafe_key)
#e=key.get()
#
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class University(ndb.Model):
    name = ndb.StringProperty()
    location = ndb.StringProperty()

class Student(ndb.Model):
    name = ndb.StringProperty()
    #univ = ndb.StringProperty()
    team = ndb.StringProperty()
    university_key = ndb.KeyProperty(kind = University)

    def url(self):
        url = '/student?key=' + self.key.urlsafe()
        return url

class MainHandler(webapp2.RequestHandler):

    def get(self):
        students= Student.query().order(Student.team).fetch()
        template_values = {'students':students}
        template = jinja_environment.get_template('list.html')
        self.response.out.write(template.render(template_values))

    def post(self):

        name= self.request.get("name")
        univ = self.request.get("univ")
        team = self.request.get('team')

        new_row = Student(name= name, univ = univ, team=team)
        new_row.put()

        self.redirect('/')

class StudentHandler(webapp2.RequestHandler):

    def get(self):
        urlsafe_key = self.request.get('key')
        key = ndb.Key(urlsafe=urlsafe_key)
        student = key.get()
        template_values = {'student':student}
        template = jinja_environment.get_template('student.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        urlsafe_key = self.request.get('key')
        key = ndb.Key(urlsafe=urlsafe_key)
        student = key.get()
        student.name = self.request.get("name")
        student.univ = self.request.get("univ")
        student.team = self.request.get('team')
        student.put()
        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/student',StudentHandler)
], debug=True)
