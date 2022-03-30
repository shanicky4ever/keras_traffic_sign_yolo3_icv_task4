# Training Step



~~1. pull CCTSDB dataset from https://github.com/csust7zhangjm/CCTSDB.git~~

~~2. run `python convert_gt.py` to convert data annotion~~

1. Use [task4 train dataset](https://drive.google.com/file/d/1aJVd6qF58zzSKUMf8teG2ZYRPo2zbxJq/view?usp=sharing)

2. `python convert_task4_label.py --root {$TASK4_TRAIN_DATASET}`) to convert annotation file

3. `pip install -r requirements.txt`

4. Download pretrained weights for backend at: https://bit.ly/39rLNoE

5. change your path in `zoo/traffic.json`

6. `python train.py -c zoo/traffic.json`

7. Use `python yolo3_one_file_to_detect_them_all.py -w {weight_file} -i {image_file}` to see task4 sample