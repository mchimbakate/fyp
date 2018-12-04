import os
from xml.etree import ElementTree

file_name = 'asthma.xml'
# full_file = os.path.join('data',file_name)
# print(file_name)
# dom = ElementTree.parse(full_file)
dom = ElementTree.parse(file_name)
# print(dom)

pathways = dom.findall('nodes/node')
for c in pathways: 
#to get the first row of nodes
   node_id = c.attrib['id']
   node_id = node_id.replace("nodes-","")
   node_id = node_id.replace("-"," ")
   nodes = node_id
   print(node_id)

