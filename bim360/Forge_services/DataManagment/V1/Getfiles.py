import os, requests, textwrap
import json

verbose = False
token = ''
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_hubs = 'https://developer.api.autodesk.com/project/v1/hubs'

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
        'scope': 'data:read'
    }

    r = requests.post(url_authenticate, data=data)

    if 200 == r.status_code:
        return r.json()

    return None

#token = (get_token('ubrKdTcp0nOtVpqYGHQ5dQm6vUoAgryi', '7uJe1B1L6UJXU9hk')['access_token'])
token = (get_token('6VYNQox4No1D62HX5wF6Hf7KsTPNR5xK', 'UgsA5EeBxDMDEtve')['access_token'])

#////////////////////////////////////////////////////////////////////
# Get Forge hubs
#
#////////////////////////////////////////////////////////////////////
def forge_hubs( token, verbose ):
  """Retrieve and return the file hubs currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_hubs, headers=headers)
 
  
  if verbose:
    print('\nForge hubs call:')
    print('  Status:', r.status_code)
    print('  Headers:', r.headers['content-type'])
    print('  Content:', r.content)

  if 200 == r.status_code:
    hubs = r.json()
  else:
    hubs = None

  return hubs
  


def main():
  """Authenticate ourselves with Forge and
  list the file hubs currently supported."""
  
  # Retrieve my Forge app credentials stored in
  # system environment variables.
  
 # client_id = os.environ['FORGE_CLIENT_ID']
 #client_secret = os.environ['FORGE_CLIENT_SECRET']

  # Authenticate the app and retrieve a
  # time limited access token.
  
 
  # Retrieve list of currently supported
  # translation file hubs.
  
  hubs = forge_hubs( token, verbose )  
  #s = json.dumps(hubs, indent=2, sort_keys=True) 
  #print('\nBucket:')
  s = json.dumps(hubs, indent=2, sort_keys=True) 
  print(s)

   
   

  
  # Present the results in a human readable manner.
  
  # s = json.dumps(hubs, indent=2, sort_keys=True) # not so nice(hubs) # nicer
  
  #print(token)

  
if __name__ == "__main__":
    main()