import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class Post(ndb.Model):
    text=ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    title = ndb.StringProperty()

    def url(self):
        return '/post?key=' + self.key.urlsafe()

class Comment(ndb.Model):
    text=ndb.StringProperty()
    name= ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    post_key = ndb.KeyProperty(kind = Post)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #logic
        posts = Post.query().order(-Post.date).fetch()
        template_values = {'posts': posts}
        #Render Response
        template = jinja_environment.get_template('home.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        # Get info from Request
        title=self.request.get('title')
        text=self.request.get('text')
        #Logic
        post= Post(title=title,text=text)
        post.put()
        self.redirect('/')
        #Render a response

class PostHandler(webapp2.RequestHandler):
    def get(self):

        urlsafe_key = self.request.get('key')
        key = ndb.Key(urlsafe=urlsafe_key)
        post = key.get()

        newposts = Comment.query(Comment.post_key == key).order(-Comment.date).fetch()
        template_values= {'post':post, 'newposts': newposts}

        template = jinja_environment.get_template('comment.html')
        self.response.out.write(template.render(template_values))
    def post(self):

        text = self.request.get('text')
        post_key_urlsafe = self.request.get('key')
        post_key = ndb.Key(urlsafe=post_key_urlsafe)
        post = post_key.get()

        comment = Comment(text=text,name='Anonymous Coward', post_key=post.key)
        comment.put()

        self.redirect(post.url())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/post', PostHandler),

], debug=True)
