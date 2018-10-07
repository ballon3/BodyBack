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
# Get Forge Buckets
#
#////////////////////////////////////////////////////////////////////


def forge_bs(token, verbose):
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

#////////////////////////////////////////////////////////////////////
# Mend Methods in Main
#
#////////////////////////////////////////////////////////////////////

def main():
  ''' Authenticate ourselves with Forge and list the file details currently supported. '''
  
  bs = forge_bs( token, verbose)
  
  # Present the results in a human readable manner
  s = json.dumps(bs, indent=2, sort_keys=True) 
  #print(bs)

  t = bs['items']
  for x in t:
      print( "Bucket Key: " + x['bucketKey'])  
   

if __name__ == "__main__":
    main()