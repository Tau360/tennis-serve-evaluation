def run():
  import csv

  input_csv = '/home/eshi/Documents/polygence/github/poem/img/input_file.csv'

  title = ['image/width','image/height','image/object/part/NOSE_TIP/center/x','image/object/part/NOSE_TIP/center/y','image/object/part/NOSE_TIP/score','image/object/part/LEFT_SHOULDER/center/x','image/object/part/LEFT_SHOULDER/center/y','image/object/part/LEFT_SHOULDER/score','image/object/part/RIGHT_SHOULDER/center/x','image/object/part/RIGHT_SHOULDER/center/y','image/object/part/RIGHT_SHOULDER/score','image/object/part/LEFT_ELBOW/center/x','image/object/part/LEFT_ELBOW/center/y','image/object/part/LEFT_ELBOW/score','image/object/part/RIGHT_ELBOW/center/x','image/object/part/RIGHT_ELBOW/center/y','image/object/part/RIGHT_ELBOW/score','image/object/part/LEFT_WRIST/center/x','image/object/part/LEFT_WRIST/center/y','image/object/part/LEFT_WRIST/score','image/object/part/RIGHT_WRIST/center/x','image/object/part/RIGHT_WRIST/center/y','image/object/part/RIGHT_WRIST/score','image/object/part/LEFT_HIP/center/x','image/object/part/LEFT_HIP/center/y','image/object/part/LEFT_HIP/score','image/object/part/RIGHT_HIP/center/x','image/object/part/RIGHT_HIP/center/y','image/object/part/RIGHT_HIP/score','image/object/part/LEFT_KNEE/center/x','image/object/part/LEFT_KNEE/center/y','image/object/part/LEFT_KNEE/score','image/object/part/RIGHT_KNEE/center/x','image/object/part/RIGHT_KNEE/center/y','image/object/part/RIGHT_KNEE/score','image/object/part/LEFT_ANKLE/center/x','image/object/part/LEFT_ANKLE/center/y','image/object/part/LEFT_ANKLE/score','image/object/part/RIGHT_ANKLE/center/x','image/object/part/RIGHT_ANKLE/center/y','image/object/part/RIGHT_ANKLE/score']

  output_file = open(input_csv,'w')
  csv_writer = csv.writer(output_file)
  csv_writer.writerow(title)

  output_file.close()
