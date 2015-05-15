import os
import urllib
import webapp2
import jinja2
from google.appengine.api import users

TEMPLATE_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
template = TEMPLATE_ENVIRONMENT.get_template('./site_files/login_test.html')

LOGOUT_URL = users.create_logout_url("/")

class UserLogin(webapp2.RequestHandler):

    
    
        
    def get(self):
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.uri)
        
        
        #reverse this. It would be easier.  So if user NOT logged in redirect to login page.
        #if logged in do a bunch of other stuff.
        
        if user:
            context = {
                    'page': "home",
                    'current_url' : self.request.url,
                     'login_url': login_url,
                    'logout_url': LOGOUT_URL,
                    'user': user,
                    'response': ''
                  }
        
            self.response.out.write(template.render(context))
        else:
            
            self.redirect(users.create_login_url(self.request.uri))
            
            
    def post(self):
        user = users.get_current_user()
        if user:
            self.redirect(LOGOUT_URL)