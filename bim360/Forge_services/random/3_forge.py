#from .memo import Memo
import os, requests, textwrap

verbose = False
token = ''
url_authenticate = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
url_formats = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/formats'
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

#////////////////////////////////////////////////////////////////////
# /forge/token route
#
#////////////////////////////////////////////////////////////////////

token = (get_token('6VYNQox4No1D62HX5wF6Hf7KsTPNR5xK', 'UgsA5EeBxDMDEtve')['access_token'])
def forge_token(request):

    client_secret = os.environ['FORGE_DEV_CLIENT_SECRET']
    client_id = os.environ['FORGE_DEV_CLIENT_ID']

    token = get_token(client_id, client_secret)

    return token

def viewer_view(request):

    try:

        model_id = request.params['id']

        model_info = request.db['gallery.models'].find_one({
            '_id': ObjectId(model_id)
        })

        if model_info is None:
            return HTTPFound(location='/404')

        return {
            'token_url': '/forge/token',
            'model_info': model_info
        }

    except:

        return HTTPFound(location='/404')

#////////////////////////////////////////////////////////////////////
# Get Forge thumbnail
#
#////////////////////////////////////////////////////////////////////
def get_thumbnail(token, urn):

    base_url = 'https://developer.api.autodesk.com'

    url = base_url + '/modelderivative/v2/designdata/{}/thumbnail?{}'

    query = 'width=400&height=400'

    headers = {
        'Authorization': 'Bearer ' + token['access_token']
    }

    r = requests.get(url.format(urn, query), headers=headers)

    if 200 == r.status_code:
        return r.content

    return None

# ////////////////////////////////////////////////////////////////////
# /forge/thumbnail?id route
#
# ////////////////////////////////////////////////////////////////////
def forge_thumbnail(request):

    try:

        model_id = request.params['id']

        model_info = request.db['gallery.models'].find_one({
            '_id': ObjectId(model_id)
        })

        if model_info is None:
            return HTTPNotFound()

        urn = model_info['model']['urn']

        credentials = getCredentials(request.registry.settings)

        token = get_tokenMemo(credentials['id'], credentials['secret'])

        thumbnail = get_thumbnail(token, urn)

        return Response(thumbnail, content_type='image/png')

    except Exception as ex:

        return HTTPNotFound()


#print(token)

def forge_formats( token, verbose ):
  """Retrieve and return the file formats currently
   supported by the translation processes."""

  headers = {'Authorization': 'Bearer ' + token}
  r = requests.get(url_hubs, headers=headers)

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
  

def jprettyprint(formats):
  "Prettyprint the JSON file format list returned by Forge."
  keys = list(formats.keys())
  keys.sort()
  return '\n'.join( ['  ' + key + ': '
    + textwrap.fill( ', '.join( formats[key] ), subsequent_indent='    ')
      for key in keys] )


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
  
  print(token)

  print(formats)
  
if __name__ == "__main__":
    main()