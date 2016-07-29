import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

class Post(ndb.Model):
    text=ndb.StringProperty()
    name= ndb.StringProperty()
    date=ndb.DateTimeProperty(auto_now_add=True)

    def url(self):
        return '/post?key=' + self.key.urlsafe()

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        posts = Post.query().order(-Post.date).fetch()
        username = str(users.get_current_user())
        template_values = {'posts': posts,"username":username}
        template = jinja_environment.get_template('home.html','home.css')
        self.response.write(template.render(template_values))
    def post(self):
        name = str(users.get_current_user())
        text = self.request.get('text')
        post= Post(text=text, name=name)
        post.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
