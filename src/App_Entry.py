import webapp2
import MainApp
import User_Login


app = webapp2.WSGIApplication([
    #I would eventually like to post the same URL
    ('/', MainApp.MainApp),
    ('/protected', User_Login.UserLogin),
    
], debug=True)