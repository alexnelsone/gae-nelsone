import os
import urllib
import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.api import mail


TEMPLATE_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
template = TEMPLATE_ENVIRONMENT.get_template('./site_files/site_homepage.html')


class MainApp(webapp2.RequestHandler):
    def get(self):
    
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.uri)
        logout_url = users.create_logout_url(self.request.uri)
        
        context = {
                    'page': "home",
                    'current_url' : self.request.url,
                     'login_url': login_url,
                    'logout_url': logout_url,
                    'user': user,
                    'response': ''
                  }
        
        self.response.out.write(template.render(context))