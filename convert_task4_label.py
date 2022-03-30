from textwrap import indent
from dict2xml import dict2xml
import json
import os
import shutil
from tqdm import tqdm
import argparse

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default=os.path.join(os.getcwd(),'..','task4_train'))
    args = parser.parse_args()
    data_root = args.root

    anno_ori_folder = os.path.join(data_root,'labels')
    anno_convert_folder = os.path.join(data_root,'labels_xml')

    if os.path.exists(anno_convert_folder):
        shutil.rmtree(anno_convert_folder)
    os.mkdir(anno_convert_folder)
    for anno_file in tqdm(os.listdir(anno_ori_folder)):
        with open(os.path.join(anno_ori_folder,anno_file),'r') as af:
            anno_data = json.load(af)
        new_anno = {
            'filename': anno_file,
            'folder': 'images',
            'path': os.path.join('images', anno_data['info']['image_name'])
        }
        for i,box in enumerate(anno_data['annotation']):
            bbox = box['bbox']
            new_anno[f'object_{i}']={
                'name': box['category'],
                'bndbox':{
                    'xmin': int(bbox[0] - bbox[2]/2),
                    'ymin': int(bbox[1] - bbox[3]/2),
                    'xmax': int(bbox[0] + bbox[2]/2),
                    'ymax': int(bbox[1] + bbox[3]/2)
                }
            }
        with open(os.path.join(anno_convert_folder,anno_file.replace('json','xml')),'w') as f:
            xml = dict2xml(new_anno,wrap='annotation',indent="    ")
            f.write(xml)