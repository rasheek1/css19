
import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/welcome.html')
        self.response.write (t.render())
       
class AboutPage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/welcome.html')
        self.response.write (t.render())

class NewsPage(webapp2.RequestHandler):
    def get(self):
        self.response.write ('<h3></h3>')        

class ResultPage(webapp2.RequestHandler):
    def get(self):
        self.response.write ('<h3>result</h3>')    


routes = [('/', MainPage),
             ('/about', AboutPage), 
             ('/news', NewsPage),
             ('/result', ResultPage)]
app = webapp2.WSGIApplication(routes, debug=True)

