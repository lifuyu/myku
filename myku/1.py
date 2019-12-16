from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
import os

root_dir = '/home/lifuyu/da_VOC/Annotations'
if not os.path.exists('/home/lifuyu/da_dataset/target_Annotations_new2'):
    os.mkdir('/home/lifuyu/da_dataset/target_Annotations_new2')

#os.chdir(root_dir)
#print(os.listdir('./'))

for root_dir_, dir, files in os.walk(root_dir):
    for file in files:
        #print(file)
        file_path = os.path.join(root_dir_, file)
        #print(file_path)
        

        if file_path.endswith('.xml'):
            tree = ET.parse(file_path)

            root = tree.getroot()

#            animNode = root.find('mir')
#            root.remove(animNode)
#
#            animNode1 = root.find('nir')
#            root.remove(animNode1)
            print(root[1][0].tag)
            if root[1][0].tag != 'object':
                print(file_path)
                os.system('rm {}'.format(file_path))
#            animNode2 = root.find('rgb')
#            print('animNode2', animNode2)
#            if animNode2 == None:
#                print(file_path)
#                exit()
#            root.remove(animNode2)
#
#            root = tree.getroot()
#
#            rgb_root_node = root.find('fir')
#
#            ob_node = rgb_root_node.findall('object') #找出根节点下所有标签为object的项
#
#
#
#            for node in ob_node:
#                print(node)
#                
#                names = node.find('name').text
#
#                if (names != 'person' and names != 'car'):
#                    
#                    rgb_root_node.remove(node)			#删除节点
#                    
#
#             
#            tree.write('{}/{}'.format('/home/lifuyu/da_dataset/target_Annotations_new2', file))#保存修改后的XML文件
#
#            print('save the new file {}'.format(os.path.join('/home/lifuyu/da_dataset/target_Annotations_new2', file)))
            
