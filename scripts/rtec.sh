#!/bin/bash

cd /home/eshi/Documents/polygence/github/poem
#navigate to the folder, then run ./rtec.sh

#python3 tec.py

#DTW means index1 and index2 both are the same length
LENGTH=$(wc -l < index1.txt)
#echo $LENGTH


INPUT1_STRING=""
INPUT2_STRING=""

while read i
do
  INPUT1_STRING="$INPUT1_STRING $i"
done < index1.txt

while read i
do
  INPUT2_STRING="$INPUT2_STRING $i"
done < index2.txt

#echo $INPUT1_STRING
#echo $INPUT2_STRING

IFS=' ' read -r -a ARRAY1 <<< "$INPUT1_STRING"
IFS=' ' read -r -a ARRAY2 <<< "$INPUT2_STRING"

for i in $(seq 0 $(($LENGTH-1)))
do
  INDEX1=${ARRAY1[$i]}
  INDEX2=${ARRAY2[$i]}
  #echo $INDEX1
  printf -v FORMAT '%05d' $(($INDEX1+18))
  #echo $FORMAT
  IMG1="vlc_extracted$FORMAT.png"
  FILEPATH1="/home/eshi/Documents/polygence/github/poem/img/$IMG1"
  
  IMG2="$(($INDEX2+15)).png"
  FILEPATH2="/home/eshi/Documents/polygence/github/poem/fed_img/$IMG2" 
  #printf -v FORMAT '%05d' $(($INDEX2+1))
  #IMG2="vlc_extracted$FORMAT.png"
  #FILEPATH2="/home/eshi/Documents/polygence/github/poem/shift_img/$IMG2"
  
  #echo $IMG1
  #echo $FILEPATH1
  #echo $IMG2
  #echo $FILEPATH2
  
  SAVED_FILEPATH="/home/eshi/Documents/polygence/github/poem/sync_5/$(($i+1)).png" 
  echo $SAVED_FILEPATH
  
  ffmpeg -i $FILEPATH2 -vf scale="-1:1280" -y resize.png
  ffmpeg -i resize.png -vf "crop=720:1280:600:0" -y cropped.png
  ffmpeg -i $FILEPATH1 -i cropped.png -filter_complex hstack $SAVED_FILEPATH

done
