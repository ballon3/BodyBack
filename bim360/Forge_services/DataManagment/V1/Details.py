import os, requests, textwrap
import json

verbose = False
token = ''
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_bucket = 'https://developer.api.autodesk.com/oss/v2/details'
url_buckets = 'https://developer.api.autodesk.com/oss/v2/buckets'
url_details = 'https://developer.api.autodesk.com/oss/v2/buckets/brett-ubrkdtcp0notvpqyghq5dqm6vuoagryi/details'

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
# Get Forge details
#
#////////////////////////////////////////////////////////////////////
def forge_details( token, verbose ):
  """Retrieve and return the file details currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_details, headers=headers)
  print(r.status_code)
  #print(r.json())
  if verbose: 
    print('\nForge details call:')
    print('  Status:', r.status_code)
    print('  Headers:', r.headers['content-type'])
    print('  Content:', r.content)

  if 200 == r.status_code:
    details = r.json()
  else:
    details = None

  return details
  
def forge_bs( token, verbose ):
  """Retrieve and return the file details currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_buckets, headers=headers)
  print(r.status_code)
  #print(r.json())
  if verbose: 
    print('\nForge details call:')
    print('  Status:', r.status_code)
    print('  Headers:', r.headers['content-type'])
    print('  Content:', r.content)

  if 200 == r.status_code:
    details = r.json()
  else:
    details = None

  return details
  

def main():
  """Authenticate ourselves with Forge and
  list the file details currently supported."""
  
  # Retrieve my Forge app credentials stored in
  # system environment variables.
  
 # client_id = os.environ['FORGE_CLIENT_ID']
 #client_secret = os.environ['FORGE_CLIENT_SECRET']

  # Authenticate the app and retrieve a
  # time limited access token.
  
 
  # Retrieve list of currently supported
  # translation file details.
  
  details = forge_details( token, verbose )
  bs = forge_bs( token, verbose)
  
  # Present the 
  # results in a human readable manner
  s = json.dumps(bs, indent=2, sort_keys=True) 
  print(bs)

if __name__ == "__main__":
    main()