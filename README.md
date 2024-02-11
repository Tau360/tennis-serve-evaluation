# Tennis Serve Evaluation

This repository provides the code needed to compare a tennis serve to a reference.

## Implementation Details

All material is for academic use only. Not for commercial use. Some of the images/videos are from public sources.

For implementation, clone the Github repo in Linux (Ubuntu 20.04 was used; don't use conda): https://github.com/google-research/google-research/tree/master/poem. The project uses Pr-VIPE, the probabilistic 2D pose embedding model. You can get the pretrained model here: https://drive.google.com/drive/folders/1rpgeQcPnTDHzlRMTYODJR4K7lYabFPzM. Download it and move it inside your pr_vipe folder.

Create two folders, one for each of the serves (in the demo, they are labeled "img" and "fed_img"). Split the serve videos into sequences of images from the beginning of the serve to the end (how many depends on the desired resolution) and place them into their respective folders. 

In my repo, under "img" and "fed_img" there are folders and files. Copy them and place them into your folders. You will have to change the folder path for the code in the folders, as well as infer.py in pr_vipe and the code in the folder "scripts".

Move all code in the "scripts" folder to the poem folder. Run comparison.sh and fed_comparison.sh to extract human body pose on the images, format keypoint data into a CSV, and create 2D pose embeddings. Run tec.py to use dynamic time warping (DTW) to align the corresponding images across the players' serves with the most similar body pose. Run rtec.sh to compile the image indexes from the DTW alignment to see the images aligned side by side. A compiled video from the images can be seen in the folder "sync_5" on my repo, and a research paper is available in the repo.

A Google Colab notebook link will be uploaded soon with zip folders that can be uploaded and extracted to run the tennis serve evaluation system within the Colab notebook.
