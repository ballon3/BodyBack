import os, requests, textwrap
import json

verbose = False
token = ''
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_buckets = 'https://developer.api.autodesk.com/oss/v2/buckets'
#////////////////////////////////////////////////////////////////////
# Get Forge token
#
#////////////////////////////////////////////////////////////////////
def get_token(client_id, client_secret):

    base_url = 'https://developer.api.autodesk.com'
    url_authenticate = base_url + '/authentication/v1/authenticate'

    data = {
        'grant_type': 'client_credentials',
        'client_secret': client_secret,
        'client_id': client_id,
        'scope': 'bucket:read'
    }

    r = requests.post(url_authenticate, data=data)

    if 200 == r.status_code:
        return r.json()

    return None

token = (get_token('ubrKdTcp0nOtVpqYGHQ5dQm6vUoAgryi', '7uJe1B1L6UJXU9hk')['access_token'])

#////////////////////////////////////////////////////////////////////
# Get Forge buckets
#
#////////////////////////////////////////////////////////////////////
def forge_buckets( token, verbose ):
  """Retrieve and return the file buckets currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_buckets, headers=headers)
  print(r.status_code)
  #print(r.json())
  if verbose:
    print('\nForge buckets call:')
    print('  Status:', r.status_code)
    print('  Headers:', r.headers['content-type'])
    print('  Content:', r.content)

  if 200 == r.status_code:
    buckets = r.json()
  else:
    buckets = None

  return buckets
  


def main():
  """Authenticate ourselves with Forge and
  list the file buckets currently supported."""
  
  # Retrieve my Forge app credentials stored in
  # system environment variables.
  
 # client_id = os.environ['FORGE_CLIENT_ID']
 #client_secret = os.environ['FORGE_CLIENT_SECRET']

  # Authenticate the app and retrieve a
  # time limited access token.
  
 
  # Retrieve list of currently supported
  # translation file buckets.
  
  buckets = forge_buckets( token, verbose )
  
  # Present the 
  # results in a human readable manner
  s = json.dumps(buckets, indent=2, sort_keys=True) 

  
  print(s)

  print('\nBucket:')

  bs = buckets['items']
  for x in bs:
      print( "bucket Key:" + x['bucketKey'])  
   
   
  
if __name__ == "__main__":
    main()