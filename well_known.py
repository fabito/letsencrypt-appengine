import webapp2
from google.appengine.ext import ndb

#http://ciandt-com.smartcanvas.tk/.well-known/acme-challenge/YoGyaFHfhzV0koF7MPneVQi7ybl2xLBw40WBVvcg1_o
#YoGyaFHfhzV0koF7MPneVQi7ybl2xLBw40WBVvcg1_o.FHpbV2_B7iECeqhk__xAQEvWaZDxhWAJVbo7LBFIyfs

class AcmeChallenge(ndb.Model):
    solution = ndb.StringProperty(indexed=False)

    def full_solution(self):
    	return self.key.id() + "." + self.solution

class AcmeChallengeHandler(webapp2.RequestHandler):

    def get(self, challenge_id):
    	challenge_key = ndb.Key(AcmeChallenge, challenge_id)
    	acme_challenge = challenge_key.get()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(acme_challenge.full_solution())

    def post(self, challenge_id, **kwargs):
    	challenge, solution = challenge_id.split(".")
    	challenge = AcmeChallenge(id=challenge, solution=solution)
    	challenge.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(challenge_id)


app = webapp2.WSGIApplication([
    webapp2.Route('/.well-known/acme-challenge/<challenge_id>', AcmeChallengeHandler, methods=['GET', 'POST'])
], debug=True)