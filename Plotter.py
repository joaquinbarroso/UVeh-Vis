#!/usr/bin/python3
import matplotlib.pyplot as plt
import math as math
import numpy as np

def lotz(osc,nm,dev):
       sup=1.3062974e8*(2/math.pi)**0.5*osc*(dev/1e14)
       inf=4*((1/i)-(1/nm))**2+(dev/1e7)**2
       global ABSn
       ABSn=sup/inf
       return ABSn
def gau(osc,nm,dev):
        exp=-1*(((1/i)-(1/nm))/(dev/1e7))**2
        global ABSn
        ABSn=1.3062974e8*(osc/dev)*math.exp(exp)
        return ABSn

deviation=(float(dev)*ev_to_joules*1e7)/(h*c)
lambda1=int(lambda1)
lambda2=int(lambda2)

a=len(datas)
ABS_tot=[]
Adj_key={'GaussianAdj': gau , 'LorentzianAdj' : lotz}

plt.figure(figsize=(12,6))
plt.rcParams.update({'font.size': 13})

if ltz:
        print('\nUsing Lorentzian adjustment...')
        dist = 'LorentzianAdj'
elif gaus:
        print('\nUsing Gaussian adjustment...')
        dist = 'GaussianAdj'
        
print('\nCurrent deviation value is '+str(dev))
Spec = Adj_key[dist]

for f in range (1,a+1):
        exec("nstates_"+str(f)+"=len(nm_values_"+str(f)+""")            
ABS_"""+str(f)+" = []")
        wavelenght=[]
        for i in range(lambda1,lambda2+1):
                wavelenght.append(i)
                exec("ABSi_"+str(f)+"=0")
                exec("for n in range(0,nstates_"+str(f)+"""):
                        osc = osc_values_"""+str(f)+"""[n]
                        nm = nm_values_"""+str(f)+"""[n]
                        dev = deviation
                        ABSn=Spec(osc,nm,dev)
                        ABSi_"""+str(f)+"+=ABSn")
                exec("ABS_"+str(f)+".append(ABSi_"+str(f)+")")
        exec("name=datas["+str(f-1)+"""].split(".")[0]
ABS_tot.append(ABS_"""+str(f)+")")

y=np.array([np.array(xi) for xi in ABS_tot])
MAX=y.max()

if normal:
        print('\nNormalizing Spectra...')
        ABS_tot = [i/MAX for i in ABS_tot]
        plt.ylabel('Normalized Absorbance', size=15)
        y=np.array([np.array(xi) for xi in ABS_tot])
        MAX=y.max()
else:
        plt.ylabel('$\\epsilon$ / $L$ $mol^{-1}$ $cm^{-1}$', size=15)
for f in range (0,a):
        plt.plot(wavelenght,ABS_tot[f],label=datas[f].split(".")[0])
if multip >= 0.0:
        print('\nCalculating coordinates of multiplicity flags...')           
        yval= []
        nm_range=[]
        multip_range=[]
        min_val= multip*MAX
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
                if yval[x] > min_val:
                        plt.text(nm_range[x],yval[x],multip_range[x])
if incsv:
       plt.plot(x_csv,y_csv,label=incsv.split(".")[0])
       if wavelenght[0]<x_csv[0] or wavelenght[-1]>x_csv[-1]:
               print(f'Warning: Plot wavelenght range is out of {incsv} wavelenght range, discontinuities would be shown')
plt.legend(edgecolor='None')
plt.xlabel('Wavelenght / nm', size=15)
plt.xlim(lambda1,lambda2)
if not temp_files==[]:
        for x in temp_files:
                os.remove(x) 
with open(citePATH) as f:
        exec(f.read())
time.sleep(1)
if csv:
        csvPATH=PATH+'/gen_csv'
        with open(csvPATH) as f:
            exec(f.read())
plt.show()
