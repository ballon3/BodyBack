import os, requests, textwrap
import json



verbose = False
token = ''
client_id = 'ubrKdTcp0nOtVpqYGHQ5dQm6vUoAgryi'
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_bucket = 'https://developer.api.autodesk.com/oss/v2/details'
url_details = 'https://developer.api.autodesk.com/oss/v2/buckets'
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
        'scope': 'bucket:create',
        

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




def forge_post( token, verbose ):
  """Post a Bucket to Autodesk Forge OSS API."""
  
  bname = input("Bucket Key Name: ") 
 
  headers = {

      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
      }
 
  data = {

      'bucketKey': ''+ bname,
      'authId': client_id,
      'access': 'full',
      'policyKey': 'persistent'

      }

  print(json.dumps(data))
 
 
  
  r = requests.post(url_details, data=json.dumps(data), headers=headers )
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

  return r.json()


#////////////////////////////////////////////////////////////////////
# Merge Methods 2 Main
#
#////////////////////////////////////////////////////////////////////


def main():
  """Authenticate ourselves with Forge and
  list the file details currently supported."""
  
  details = forge_post( token, verbose )
  
  # Present the  results in a human readable manner
  s = json.dumps(details, indent=2, sort_keys=True) 
  print(s)

if __name__ == "__main__":
    main()