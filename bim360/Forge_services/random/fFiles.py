import os, requests, textwrap
import json

verbose = False
token = ''
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_files = 'https://developer.api.autodesk.com/oss/v2/buckets/forgebucket_3930/objects'

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
# Get Forge files
#
#////////////////////////////////////////////////////////////////////
def forge_files( token, verbose ):
  """Retrieve and return the file files currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_files, headers=headers)
  print(r.status_code)
  
  if verbose:
    print('\nForge files call:')
    print('  Status:', r.status_code)
    print('  Headers:', r.headers['content-type'])
    print('  Content:', r.content)

  if 200 == r.status_code:
    files = r.json()
  else:
    files = r.json()

  return files
  


def main():
  """Authenticate ourselves with Forge and
  list the file files currently supported."""
  
  # Retrieve my Forge app credentials stored in
  # system environment variables.
  
 # client_id = os.environ['FORGE_CLIENT_ID']
 #client_secret = os.environ['FORGE_CLIENT_SECRET']

  # Authenticate the app and retrieve a
  # time limited access token.
  
 
  # Retrieve list of currently supported
  # translation file files.
  
  files = forge_files( token, verbose )
  print(files)

  bs = files['items']
  for x in bs:
      print( "3D Model: " + x['objectKey'])  
 
  
  #s = json.dumps(files, indent=2, sort_keys=True) 
  print('\nBucket:')


   
   

  
  # Present the results in a human readable manner.
  
  # s = json.dumps(files, indent=2, sort_keys=True) # not so nice(files) # nicer
  
  #print(token)

  
if __name__ == "__main__":
    main()