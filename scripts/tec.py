from dtw import *
import csv
import numpy as np

##################CHANGE THE FOLLOWING BELOW

own_embeddings = '/home/eshi/Documents/polygence/github/poem/img/embeddings/embedding_stddevs.csv'
#fed_embeddings = '/home/eshi/Documents/polygence/github/poem/shift_img/embeddings/embedding_stddevs.csv' #shift/variations
fed_embeddings = '/home/eshi/Documents/polygence/github/poem/fed_img/embeddings/embedding_stddevs.csv' #federer

own = []
fed = []

loaded_file = open(own_embeddings,'r')
csv_reader = csv.reader(loaded_file)

for i in csv_reader:
  row = [eval(j) for j in i]
  own.append(row)

loaded_file.close()

loaded_file = open(fed_embeddings,'r')
csv_reader = csv.reader(loaded_file)

for i in csv_reader:
  row = [eval(j) for j in i]
  fed.append(row)
  
print(own)
#print("\n")
print(fed)

alignment = dtw(own, fed, keep_internals=True, step_pattern=rabinerJuangStepPattern(6, "d"))

print(alignment.distance) #variable extraction to be figured out later

index1 = alignment.index1
index2 = alignment.index2

np.savetxt('index1.txt',index1,fmt='%d')
np.savetxt('index2.txt',index2,fmt='%d')

a = alignment.plot(type="threeway")
#a.figure.savefig("alignment.png")

#alignment = dtw(own, fed, keep_internals=True, step_pattern=rabinerJuangStepPattern(6, "c")) #WORKING 
#b = dtw(own, fed, keep_internals=True, step_pattern=rabinerJuangStepPattern(6, "c"))

#c = b.plot()

#c.figure.savefig("alignment.png")

#help(DTW)
#help(stepPattern) #rabiner juang
