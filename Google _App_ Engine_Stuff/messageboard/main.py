import webapp2
import os
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty()
    comment = ndb.StringProperty()
    time = ndb.DateTimeProperty(auto_now=True)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        users = User.query().order(-User.time).fetch()
        template_values = {'users': users}
        template = jinja_environment.get_template('board.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        name= str(users.get_current_user())
        comment = self.request.get("comment")
        new_comment = User(name= name, comment = comment)
        new_comment.put()

        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
