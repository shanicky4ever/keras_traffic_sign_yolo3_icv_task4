# Training Step

1. pull CCTSDB dataset from https://github.com/csust7zhangjm/CCTSDB.git

2. run `python convert_gt.py` to convert data annotion

3. `pip install -r requirements.txt`

4. Download pretrained weights for backend at: https://bit.ly/39rLNoE

5. change your path in `zoo/traffic.json`

6. `python train.py -c zoo/traffic.json`

7. Use `python yolo3_one_file_to_detect_them_all.py -w {weight_file} -i {image_file}` to see task4 sample