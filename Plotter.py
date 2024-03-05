#!/usr/bin/python3
import matplotlib.pyplot as plt
import math as math
lambda1=int(lambda1)
lambda2=int(lambda2)
a=len(datas)
plt.figure(figsize=(12,6))
plt.rcParams.update({'font.size': 13})
ltz = args.lorentzian
if ltz:
        print('\nUsing lorentzian adjustment...')
else:
        print('\nUsing gaussian adjustment...')
deviation=(float(dev)*ev_to_joules*1e7)/(h*c)
print('\nCurrent deviation value is '+str(dev))
for f in range (1,a+1):
        exec("nstates_"+str(f)+"=len(nm_values_"+str(f)+""")            
ABS_"""+str(f)+" = []")
        wavelenght=[]
        if ltz:
                for i in range(lambda1,lambda2+1):
                        wavelenght.append(i)
                        exec("ABSi_"+str(f)+"=0")
                        exec("for n in range(0,nstates_"+str(f)+"""):
                                sup=1.3062974e8*(2/math.pi)**0.5*osc_values_"""+str(f)+"""[n]*(deviation/1e7)
                                inf=((1/i)-(1/nm_values_"""+str(f)+"""[n]))**2+(deviation/1e7)**2
                                ABSn=sup/inf
                                ABSi_"""+str(f)+"+=ABSn")
                        exec("ABS_"+str(f)+".append(ABSi_"+str(f)+")")
        else:
                for i in range(lambda1,lambda2+1):
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
plt.xlabel('Wavelenght / nm', size=15)
plt.xlim(lambda1,lambda2)
with open(citePATH) as f:
        exec(f.read())
time.sleep(2)
if csv:
        csvPATH=PATH+'/gen_csv'
        with open(csvPATH) as f:
            exec(f.read())
        plt.show()
else:
        plt.show()
with open(issuePATH) as f:
        exec(f.read())




