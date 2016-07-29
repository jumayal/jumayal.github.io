import webapp2
import jinja2
import os
import random
from google.appengine.ext import ndb


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
class Flower(ndb.Model):
    top = ndb.IntegerProperty()
    left = ndb.IntegerProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        left = random.randint(0,100)
        top = random.randint(0,100)

        new_flower = Flower(top=top, left=left)
        new_flower.put()

        flowers = Flower.query().fetch()
        template_values = {'flowers':flowers}
        
        template = jinja_environment.get_template('garden.html')
        self.response.out.write(template.render(template_values))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
