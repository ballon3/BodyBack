import os, requests, textwrap

verbose = False
token = ''
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_formats = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/formats'

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

token = (get_token('6VYNQox4No1D62HX5wF6Hf7KsTPNR5xK', 'UgsA5EeBxDMDEtve')['access_token'])

#////////////////////////////////////////////////////////////////////
# Get Forge Formats
#
#////////////////////////////////////////////////////////////////////
def forge_formats( token, verbose ):
  """Retrieve and return the file formats currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_formats, headers=headers)

  if verbose:
    print('\nForge formats call:')
    print('  Status:', r.status_code)
    print('  Headers:', r.headers['content-type'])
    print('  Content:', r.content)

  if 200 == r.status_code:
    formats = r.json()
  else:
    formats = r.json()

  return formats


def main():
  """Authenticate ourselves with Forge and
  list the file formats currently supported."""
  
  # Retrieve my Forge app credentials stored in
  # system environment variables.
  
 # client_id = os.environ['FORGE_CLIENT_ID']
 #client_secret = os.environ['FORGE_CLIENT_SECRET']

  # Authenticate the app and retrieve a
  # time limited access token.
  
 
  # Retrieve list of currently supported
  # translation file formats.
  
  formats = forge_formats( token, verbose )
  
  # Present the results in a human readable manner.
  
  # s = json.dumps(formats, indent=2, sort_keys=True) # not so nice(formats) # nicer
  
  #print(token)

  print(formats)
  
if __name__ == "__main__":
    main()