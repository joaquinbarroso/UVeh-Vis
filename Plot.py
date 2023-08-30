import matplotlib.pyplot as plt
import math as math
with open('ReadES2.py') as f:
	exec(f.read())
	nstates=len(nm_values)-1
	deviation=(float(dev)*ev_to_joules*1e7)/(h*c)
	ABS = []
	wavelenght=[]
	for i in range(int(lambda1),int(lambda2)+1):
		wavelenght.append(i)
		ABSi=0
		for n in range(0,nstates):
			exp=-1*(((1/i)-(1/nm_values[n]))/(deviation/1e7))**2
			ABSn=1.3062974e8*(osc_values[n]/deviation)*math.exp(exp)
			ABSi+=ABSn
		ABS.append(ABSi)
'''		with open("prueba2", "a+") as file_object:
    			file_object.seek(0)
    			data = file_object.read(1000)
    			if len(data) > 0 :
    				file_object.write("\n")
    				file_object.write(wavelenght[i],ABS[i]+'\n')'''

plt.plot(wavelenght,ABS)
plt.show()


