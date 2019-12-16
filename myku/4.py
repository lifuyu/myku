from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
import os
import numpy as np

filename = '000001.xml'
tree = ET.parse(filename)
objs = tree.findall('object')
#root = tree.getroot()
#print(root)
#for child in root:
  #print(child.tag,child.attrib)
#rgb_root_node = root.find('rgb')
#print(rgb_root_node)
#objs = rgb_root_node.findall('object')
#objs = tree.findall('objects')
print(objs)
num_objs = len(objs)
print(num_objs)
boxes = np.zeros((num_objs, 4), dtype=np.uint16)
print(boxes)



boxes = np.zeros((num_objs, 4), dtype=np.uint16)
gt_classes = np.zeros((num_objs), dtype=np.int32)
#overlaps = np.zeros((num_objs, self.num_classes), dtype=np.float32)
       # "Seg" area for pascal is just the box area
seg_areas = np.zeros((num_objs), dtype=np.float32)
ishards = np.zeros((num_objs), dtype=np.int32)

        # Load object bounding boxes into a data frame.
for ix, obj in enumerate(objs):
  bbox = obj.find('bndbox')
            # Make pixel indexes 0-based
  
  x1 = float(bbox.find('xmin').text) - 1
  y1 = float(bbox.find('ymin').text) - 1
  x2 = float(bbox.find('xmax').text) - 1
  y2 = float(bbox.find('ymax').text) - 1
  diffc = obj.find('difficult')
  difficult = 0 if diffc == None else int(diffc.text)
  ishards[ix] = difficult

            #cls = self._class_to_ind[obj.find('name').text.lower().strip()]
  
  if abs(x2-x1) >= 20 and abs(y2-y1) >= 20:
      boxes[ix, :] = [x1, y1, x2, y2]
  #gt_classes[ix] = cls
  #overlaps[ix, cls] = 1.0
  #seg_areas[ix] = (x2 - x1 + 1) * (y2 - y1 + 1)

print(boxes)



