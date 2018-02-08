
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

for i in OPENED_PROJECT:
    print(i)

MYPROJECT=OPENED_PROJECT[0][2]
MYPROJECT='017a3d81-ad55-48f3-adc1-695fa58e9078'
REST_TAIL='/nodes'

nodes = requests.get('http://'+SERVER_IP+':'+SERVER_PORT+'/v2/projects/'+ MYPROJECT + REST_TAIL)
print('### Nodes')
for i in nodes.json():
    print(i)
    print(i['node_id'])
    print(i['ports'])

REST_TAIL='/links'
links = requests.get('http://' + SERVER_IP + ':' + SERVER_PORT + '/v2/projects/' + MYPROJECT + REST_TAIL)
print('### Links')
for i in links.json():
    print(i)


#create_links
ADAPTER_NBR1="0"
NODE_ID1='"5cc4a8f6-f4f2-4a0f-8d08-86d041601284"'
PORT_NBR1="0"
ADAPTER_NBR2="0"
NODE_ID2='"e8cfb52f-ee29-4c3b-b8be-f55dc6e1cea5"'
PORT_NBR2="0"

CreateLinkUrl='http://' + SERVER_IP + ':' + SERVER_PORT + '/v2/projects/' + MYPROJECT + REST_TAIL
data='{"nodes": [{"adapter_number": '+ ADAPTER_NBR1 +', "node_id": '+NODE_ID1+', "port_number": '+PORT_NBR1+'}, {"adapter_number": '+ADAPTER_NBR2+', "node_id": '+NODE_ID2+', "port_number": '+ PORT_NBR2+'}]}'
print(CreateLinkUrl)
CreateLinkRequest = requests.post(CreateLinkUrl, data)

print(CreateLinkRequest)
#linkReq=
#requests.get('http://' + SERVER_IP + ':' + SERVER_PORT + '/v2/projects/' + MYPROJECT + REST_TAIL+ ' -d' + ' {"nodes": [{"adapter_number": 0, "node_id": "f124dec0-830a-451e-a314-be50bbd58a00", "port_number": 0}, {"adapter_number": 0, "node_id": "83892a4d-aea0-4350-8b3e-d0af3713da74", "port_number": 0}]}'

# Working shell request
# curl -X POST  "http://192.168.0.146:8000/v2/projects/017a3d81-ad55-48f3-adc1-695fa58e9078/links" -d '{"nodes": [{"adapter_number": 0, "node_id": "5cc4a8f6-f4f2-4a0f-8d08-86d041601284", "port_number": 0}, {"adapter_number": 0, "node_id": "e8cfb52f-ee29-4c3b-b8be-f55dc6e1cea5", "port_number": 0}]}'


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