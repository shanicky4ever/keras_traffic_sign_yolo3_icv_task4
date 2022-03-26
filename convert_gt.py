from math import ceil
import os
from tqdm import tqdm
from dict2xml import dict2xml
import shutil

if __name__=='__main__':
    data_root = os.path.join(os.getcwd(), '..', 'CCTSDB')
    anno_ori_file = os.path.join(data_root, 'GroundTruth', 'groundtruth0000-9999.txt')
    anno_convert_folder = os.path.join(os.getcwd(),'..','CCTSDB_anno')
    if os.path.exists(anno_convert_folder):
        shutil.rmtree(anno_convert_folder)
    os.mkdir(anno_convert_folder)
    label_convert = {'prohibitory':'0', 'mandatory':'1', 'warning':'2'}
    rf = open(anno_ori_file,'r')
    boxes = list()
    last_num  = -1
    for line in tqdm(rf.readlines()):
        attr = line.strip().split(';')
        if not attr[-1]:
            continue
        num = int(attr[0].split('.')[0])
        #label = label_convert[attr[-1]]
        label = attr[-1]
        boxes.append([int(float(x)) for x in attr[1:-1]] + [label])
        if num == last_num:
            continue
        else:
            img_folder = 'image' + f'{num//1000}000-{num//1000}999'
            anno_info = {
                'folder': img_folder,
                'filename': attr[0],
                'path': os.path.join(img_folder, attr[0])
            }
            for index, b in enumerate(boxes):
                anno_info[f'object_{index}'] = {
                    'name': b[-1],
                    'bndbox':{
                        'xmin': b[0],
                        'ymin': b[1],
                        'xmax': b[2],
                        'ymax': b[3]
                    }
                }
            with open(os.path.join(anno_convert_folder, attr[0].replace('png','xml')), 'w') as wf:
                xml = dict2xml(anno_info, wrap ='annotation', indent ="    ")
                wf.write(xml)
            last_num = num
            boxes=list()

    rf.close()
        
