

import xml.etree.ElementTree as ET

#import glob
#
def read_content(xml_file: str):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []

    for boxes in root.iter('object'):

        filename = root.find('filename').text

        ymin, xmin, ymax, xmax = None, None, None, None

        for box in boxes.findall("bndbox"):
            ymin = int(box.find("ymax").text)
            xmin = int(box.find("xmin").text)
            ymax = int(box.find("ymin").text)
            xmax = int(box.find("xmax").text)

        list_with_single_boxes = [xmin, ymin, xmax, ymax]
        list_with_all_boxes.append(list_with_single_boxes)

    return filename, list_with_all_boxes
import glob
import pandas as pd
box=[]
q=''
a=glob.glob("DatasetNew/xml/*")
for i in range(0,len(a)):
    name, boxes = read_content(a[i])
    q='DatasetNew/images' +name
    
    
    for j in range(0,len(boxes)):
        boxes[j].insert(0,str(q))
    box.extend(boxes)
    
df = pd.DataFrame(box)     
df.columns=['image-path','xmin','ymin','xmax','ymax']
df.set_index(['image-path'], inplace=True)
cls=[]
for i in range(0,df.shape[0]):
  cls.append('crop')
df['cls']=cls
df.to_csv('/content/drive/My Drive/Dataset/test/test_annotations_1.csv',header=None) 
#df.to_csv('/content/annotate.txt', header=None, sep=',')

#name, boxes = read_content('/home/ambuje/ambuje/Corn Yield/AI03_Yield prediction in corn fields/sample_data/annotation_files/DJI_0015.xml')
