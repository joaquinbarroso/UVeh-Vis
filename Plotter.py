#!/usr/bin/python3
import matplotlib.pyplot as plt
import math as math
lambda1=int(lambda1)
lambda2=int(lambda2)
a=len(datas)
def lotz(osc,nm,dev):
       sup=1.3062974e8*(2/math.pi)**0.5*osc*(dev/1e7)
       inf=((1/i)-(1/nm))**2+(dev/1e7)**2
       global ABSn
       ABSn1=sup/inf
       ABSn=ABSn1/Norm
def gau(osc,nm,dev):
        exp=-1*(((1/i)-(1/nm))/(dev/1e7))**2
        global ABSn
        ABSn1=1.3062974e8*(osc/dev)*math.exp(exp)
        ABSn=ABSn1/Norm
ltz = args.lorentzian
gaus = args.gaussian
normal = args.normalized
plt.figure(figsize=(12,6))
plt.rcParams.update({'font.size': 13})
deviation=(float(dev)*ev_to_joules*1e7)/(h*c)
#Maximum det
Norm=1
osc,nm,dev,i=max_f,1,deviation,1
if ltz:
        print('\nUsing Lorentzian adjustment...')
        dist = 'Lorentzian'
        lotz(osc,nm,dev)
        MAX=ABSn
elif gaus:
        print('\nUsing Gaussian adjustment...')
        dist = 'Gaussian'
        gau(osc,nm,dev)
        MAX=ABSn
else:
        print('\nUsing Gaussian adjustment...')
        dist = 'Gaussian'
        gau(osc,nm,dev)
        MAX=ABSn
print('\nCurrent deviation value is '+str(dev))
if normal:
        print('\nNormalizing Spectra...')
        Norm=MAX
ABS_tot=[]
print(MAX)
for f in range (1,a+1):
        exec("nstates_"+str(f)+"=len(nm_values_"+str(f)+""")            
ABS_"""+str(f)+" = []")
        wavelenght=[]
        if dist == 'Lorentzian':
                for i in range(lambda1,lambda2+1):
                        wavelenght.append(i)
                        exec("ABSi_"+str(f)+"=0")
                        exec("for n in range(0,nstates_"+str(f)+"""):
                                osc = osc_values_"""+str(f)+"""[n]
                                nm = nm_values_"""+str(f)+"""[n]
                                dev = deviation
                                lotz(osc,nm,dev)
                                ABSi_"""+str(f)+"+=ABSn")
                        exec("ABS_"+str(f)+".append(ABSi_"+str(f)+")")
        elif dist == 'Gaussian':
                for i in range(lambda1,lambda2+1):
                        wavelenght.append(i)
                        exec("ABSi_"+str(f)+"=0")
                        exec("for n in range(0,nstates_"+str(f)+"""):
                                osc = osc_values_"""+str(f)+"""[n]
                                nm = nm_values_"""+str(f)+"""[n]
                                dev = deviation
                                gau(osc,nm,dev)
                                ABSi_"""+str(f)+"+=ABSn")
                        exec("ABS_"+str(f)+".append(ABSi_"+str(f)+")")
        exec("name=datas["+str(f-1)+"""].split(".")[0]
ABS_tot.append(ABS_"""+str(f)+")""")
for f in range (0,a):
        plt.plot(wavelenght,ABS_tot[f],label=datas[f-1].split(".")[0])
multip = args.showmultiplicity
if multip:             
        yval= []
        nm_range=[]
        multip_range=[]
        for n in range(0,a):
                b_max=len(all_mult[n])
                exec("nm_n = nm_values_"+str(n+1))
                ABS_n=ABS_tot[n]
                ABS_str =[str(x) for x in ABS_n]
                nm_str =[str(x) for x in nm_n]
                multip_n = all_mult[n]
                for b in range(0,b_max):
                        val=float(nm_str[b])
                        if lambda1<val<lambda2: 
                                nm_int=round(val)
                                nm_range.append(nm_int)
                                plot_ind=wavelenght.index(nm_int)
                                ABS_val=float(ABS_str[plot_ind])
                                yval.append(ABS_val)
                                mult_val=multip_n[b]
                                multip_range.append(mult_val)                                
        for x in range(0,len(yval)):
                plt.text(nm_range[x],yval[x],multip_range[x])
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
