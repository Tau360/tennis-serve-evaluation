#!/bin/bash

cd /home/eshi/Documents/polygence/github/poem/fed_img

python3 -c 'import header; print (header.run())'

pip3 install openpifpaf

for i in *.png
do
  python3 -m openpifpaf.predict $i --image-output /home/eshi/Documents/polygence/github/poem/fed_img/img_output/reference.png --json-output /home/eshi/Documents/polygence/github/poem/fed_img/reference.json
  python3 -c 'import json_to_csv; print (json_to_csv.run())'
done

cd /home/eshi/Documents/polygence/github

python3 -m pip install numpy==1.24.3
pip3 install -r poem/requirements.txt
export PYTHONPATH=$PYTHONPATH:/home/eshi/Documents/polygence/github/poem

python3 /home/eshi/Documents/polygence/github/poem/pr_vipe/fed_infer.py
