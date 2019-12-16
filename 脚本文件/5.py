from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
import os
import numpy as np

filename = '000492.xml'



tree = ET.parse(filename)
objects = []
root = tree.getroot()
rgb_root_node = root.find('rgb')
print(rgb_root_node)
for obj in rgb_root_node.findall('object'):
  #for obj in tree.findall('object'):
    obj_struct = {}
    obj_struct['name'] = obj.find('name').text
    #obj_struct['pose'] = obj.find('pose').text
    obj_struct['truncated'] = int(obj.find('truncated').text)
    obj_struct['difficult'] = int(obj.find('difficult').text)
    bbox = obj.find('bndbox')
    obj_struct['bbox'] = [int(float(bbox.find('xmin').text)),
                          int(float(bbox.find('ymin').text)),
                          int(float(bbox.find('xmax').text)),
                          int(float(bbox.find('ymax').text))]
    objects.append(obj_struct)
print(objects)
