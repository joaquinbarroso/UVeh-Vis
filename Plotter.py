#!/usr/bin/python3
import matplotlib.pyplot as plt
import math as math
a=len(datas)+1
lambda1=int(lambda1)
lambda2=int(lambda2)
plt.figure(figsize=(10,6))
plt.rcParams.update({'font.size': 13})
for f in range (1,a):
        exec("nstates_"+str(f)+"=len(nm_values_"+str(f)+""")            
ABS_"""+str(f)+" = []")
        wavelenght=[]
        deviation=(float(dev)*ev_to_joules*1e7)/(h*c)
        for i in range(lambda1,lambda2):
                wavelenght.append(i)
                exec("ABSi_"+str(f)+"=0")
                exec("for n in range(0,nstates_"+str(f)+"""):
                        exp=-1*(((1/i)-(1/nm_values_"""+str(f)+"""[n]))/(deviation/1e7))**2
                        ABSn=1.3062974e8*(osc_values_"""+str(f)+"""[n]/deviation)*math.exp(exp)
                        ABSi_"""+str(f)+"+=ABSn")
                exec("ABS_"+str(f)+".append(ABSi_"+str(f)+")")
        exec("name=datas["+str(f-1)+"""].split(".")[0]
plt.plot(wavelenght,ABS_"""+str(f)+",label=name)")
csv = args.table
plt.legend(edgecolor='None')
plt.xlabel('Wavelenght /nm', size=15)
plt.xlim(lambda1,lambda2)
if csv:
        csvPATH=PATH+'/gen_csv'
        with open(csvPATH) as f:  #15/01/24
            exec(f.read())        #15/01/24
        plt.show()
else:
        plt.show()




