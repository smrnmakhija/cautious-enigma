import csv
import math
from random import randrange
import random as rnd
from statistics import mode
 
classs=[]
label=[]
readdata = csv.reader(open("output.csv"))

for row in readdata:
	temp=[]
	for val in row[0].split():
		try:
			temp.append(float(val))
		except ValueError:

			temp.append(None)

	classs.append(temp)
	label.append(temp[-1])

target=[]
testarget=[]
test=[]
train=[]
training=[] 
testing=[]
for row in classs:
	if((rnd.randint(0,100))<85):
		training.append(row)
		train.append(row[0:-1])
		target.append(row[-1])
	else:
		testing.append(row)
		test.append(row[0:-1])
		testarget.append(row[-1])


def get_dist(test_sample,arr):

	distance=0
	dist =0
	for x in range(len(test_sample)):
		distance+=pow((test_sample[x]-arr[x]),2)
	dist=math.sqrt(distance)
	return dist

t1=[]
t2=[]
t6=[]
for test_sample in test:
	for arr in training:
		d=get_dist(test_sample,arr[0:-1])
		t1.append((d,arr[-1]))
	t1.sort()
	t3=t1[:11]
	
	t4=[t[1] for t in t3]
	t6.append(mode(t4))
#t2.append(t6)
print (t6)
print (testarget)
c=0
for x in range(len(t6)):
	if (t6[x]==testarget[x]):
		c+=1
print ((c/len(t6))*100)
