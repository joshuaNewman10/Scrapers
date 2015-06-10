import oauth2 as oauth
import urllib2 as urllib

twitterKeys = {
  'api_key': "JoY2ZAyRrem21Owc7AsCWQnA3",
  'api_secret': "08KG7ssQnqCMlSLp8Bj2o1zGE00BS3zogbmh1NNTmlMCRlPtve",
  'access_token_key': "3089520639-WkhnbsaOg3wNlDZahpQlCGQfeMnAc2w1MaDhl6E",
  'access_token_secret': "qwM8P13A1ljsR5JekBABWGExtKRlJAbtD1KljrkQnrm2e"  
}

_debug = 0

oauth_token = oauth.Token(key=twitterKeys['access_token_key'],
                          secret=twitterKeys['access_token_secret'])

oauth_consumer = oauth.Consumer(key=twitterKeys['api_key'], 
                                secret=twitterKeys['api_secret'])

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct sign, open twitter req
using hard coded credentials abvoe
'''

def twitterRequest(url, method, parameters):
  request = oauth.Request.from_consumer_and_token(oauth_consumer,
                                                  token=oauth_token,
                                                  http_method=http_method,
                                                  http_url=url,
                                                  parameters=parameters)

  request.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = request.to_header()

  if http_method == 'POST':
    encoded_post_data = request.to_postdata()
  else:
    encoded_post_data = None
    url = request.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = 'https://stream.twitter.com/1/statuses/sample.json'
  parameters = []
  response = twitterRequest(url, 'GET', parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
