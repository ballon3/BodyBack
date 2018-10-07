# Hubs

### 1. GET hubs
### 2. GET hubs/:hub_id

# Projects

### 1. GET hubs/:hub_id/projects
### 2. GET hubs/:hub_id/projects/:project_id
### 3. GET hubs/:hub_id/projects/:project_id/hub
### 4. GET hubs/:hub_id/projects/:project_id/topFolders
### 5. GET projects/:project_id/downloads/:download_id
### 6. GET projects/:project_id/jobs/:job_id
### 7. POST projects/:project_id/downloads
### 8. POST projects/:project_id/storage

# Folders

### 1. GET projects/:project_id/folders/:folder_id
### 2. GET projects/:project_id/folders/:folder_id/contents
### 3. GET projects/:project_id/folders/:folder_id/parent
### 4. GET projects/:project_id/folders/:folder_id/refs
### 5. GET projects/:project_id/folders/:folder_id/relationships/links
### 6. GET projects/:project_id/folders/:folder_id/relationships/refs
### 7. GET projects/:project_id/folders/:folder_id/search
### 8. PATCH projects/:project_id/folders/:folder_id
### 9. POST projects/:project_id/folders
### 10. POST projects/:project_id/folders/:folder_id/relationships/refs

# Items

### 1. GET projects/:project_id/items/:item_id
### 2. GET projects/:project_id/items/:item_id/parent
### 3. GET projects/:project_id/items/:item_id/refs
### 4. GET projects/:project_id/items/:item_id/relationships/links
### 5. GET projects/:project_id/items/:item_id/relationships/refs
### 6. GET projects/:project_id/items/:item_id/tip
### 7. GET projects/:project_id/items/:item_id/versions
### 8. PATCH projects/:project_id/items/:item_id
### 9. POST projects/:project_id/items
### 10. POST projects/:project_id/items/:item_id/relationships/refs

# Versions

### 1. GET projects/:project_id/versions/:version_id
### 2. GET projects/:project_id/versions/:version_id/downloadFormats
### 3. GET projects/:project_id/versions/:version_id/downloads
### 4. GET projects/:project_id/versions/:version_id/item
### 5. GET projects/:project_id/versions/:version_id/refs
### 6. GET projects/:project_id/versions/:version_id/relationships/links
### 7. GET projects/:project_id/versions/:version_id/relationships/refs
### 8. PATCH projects/:project_id/versions/:version_id
### 9. POST projects/:project_id/versions
### 10. POST projects/:project_id/versions/:version_id/relationships/refs

# Buckets

### 1. POST buckets
### 2. GET buckets
### 3. GET buckets/:bucketKey/details
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

# Objects

### 1. PUT buckets/:bucketKey/objects/:objectName
### 2. PUT buckets/:bucketKey/objects/:objectName/resumable
### 3. GET buckets/:bucketKey/objects/:objectName/status/:sessionId
### 4. GET buckets/:bucketKey/objects
### 5. GET buckets/:bucketKey/objects/:objectName/details
### 6. GET buckets/:bucketKey/objects/:objectName
### 7. POST buckets/:bucketKey/objects/:objectName/signed
### 8. PUT signedresources/:id
### 9. PUT signedresources/:id/resumable
### 10. GET signedresources/:id
### 11. DELETE signedresources/:id
### 12. PUT buckets/:bucketKey/objects/:objectName/copyto/:newObjectName
### 13. DELETE buckets/:bucketKey/objects/:objectName

# Commands

### 1. CheckPermission
### 2. ListRefs
### 3. ListItems
### 4. CreateFolder
### 5. PublishModel
### 6. GetPublishModelJob