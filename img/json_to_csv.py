"""Convert json keypoint data to a formatted input csv"""

def run():
  import sys
  import json
  import csv

  input_json = '/home/eshi/Documents/polygence/github/poem/img/reference.json'
  input_csv = '/home/eshi/Documents/polygence/github/poem/img/input_file.csv'

  with open(input_json) as input_file:
    data = json.load(input_file)

  data = data[0]

  keypoints = data['keypoints']
  bbox = data['bbox']

  x = bbox[0]
  y = bbox[1]
  width = bbox[2]
  height = bbox[3]

  output_file = open(input_csv,'a')

  csv_writer = csv.writer(output_file)

  #Remove not needed keypoints

  for i in range(0,12):
    keypoints.pop(3)

  #keypoints = [i for i in keypoints if i != 0]
  #print(keypoints)

  for i in range(0, len(keypoints)):
    a = keypoints[i]
    if i%3 == 0 and keypoints[i] != 0:
      keypoints[i] = (a-x)/width
    elif i%3 == 1 and keypoints[i] != 0:
      keypoints[i] = (a-y)/height
    else:
      continue

  keypoints.insert(0,width) 
  keypoints.insert(1,height)

  csv_writer.writerow(keypoints)

  output_file.close()
