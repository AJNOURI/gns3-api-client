
# curl -i -X GET 'http://192.168.0.146:8000/v2/projects'


import requests

SERVER_IP = '192.168.0.146'
SERVER_PORT = '8000'
r = requests.get('http://'+SERVER_IP+':'+SERVER_PORT+'/v2/projects')
#print(r.status_code)
#print(r.headers['content-type'])
#print(r.encoding)
#print(r.text)
#print(type(r.json()))

ALL_PROJECT=[]
OPENED_PROJECT=[]
for i in r.json():
    #print(i)
    ALL_PROJECT.append([i['name'], i['project_id'],i['status']])
    if i['status'] == 'opened':
        OPENED_PROJECT.append([i['name'], i['project_id'], i['status']])

#print(PROJECT_LIST)
#for i in ALL_PROJECT:
#    print(i)

#for i in OPENED_PROJECT:
#    print(i)

MYPROJECT=OPENED_PROJECT[0][1]

REST_TAIL='/nodes'

#nodes = requests.get('http://'+SERVER_IP+':'+SERVER_PORT+'/v2/projects/'+ MYPROJECT + REST_TAIL)
#for i in nodes.json():
#    print(i)

REST_TAIL='/links'
links = requests.get('http://' + SERVER_IP + ':' + SERVER_PORT + '/v2/projects/' + MYPROJECT + REST_TAIL)
for i in links.json():
    print(i)


#TODO
# compare API version <> GNS3 version
#list all projects + name + id + status
#list all opened projects + name + id + status
#for a given project id
#    ==> list of nodes all property
#for a given node id
#    ==> list all properties
#    ==> list connections
#    ==> list interfaces

#    if i['status'] == 'opened':
#        print(i['project_id'])
#        thisproject=i['project_id']

 #   for key, value in i:
  #      print(i['status'])