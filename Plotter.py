#!/usr/bin/python3
import matplotlib.pyplot as plt
import math as math
a=len(datas)+1
for f in range (1,a):
        exec("nstates_"+str(f)+"=len(nm_values_"+str(f)+""")            
ABS_"""+str(f)+" = []")
        wavelenght=[]
        deviation=(float(dev)*ev_to_joules*1e7)/(h*c)
        for i in range(int(lambda1),int(lambda2)+1):
                wavelenght.append(i)
                exec("ABSi_"+str(f)+"=0")
                exec("for n in range(0,nstates_"+str(f)+"""):
                        exp=-1*(((1/i)-(1/nm_values_"""+str(f)+"""[n]))/(deviation/1e7))**2
                        ABSn=1.3062974e8*(osc_values_"""+str(f)+"""[n]/deviation)*math.exp(exp)
                        ABSi_"""+str(f)+"+=ABSn")
                exec("ABS_"+str(f)+".append(ABSi_"+str(f)+")")
        exec("name=datas["+str(f-1)+"""].split(".")[0]
plt.plot(wavelenght,ABS_"""+str(f)+",label=name)")
plt.legend()
plt.show()




