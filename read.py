import scipy.io
import numpy as np
data = scipy.io.loadmat('realitymining.mat')
for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("fook.csv"),data[i],delimiter=',')
