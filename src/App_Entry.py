import webapp2
import MainApp


app = webapp2.WSGIApplication([
    #I would eventually like to post the same URL
    ('/', MainApp.MainApp),
    
], debug=True)