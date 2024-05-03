import numpy as np
import matplotlib.pyplot as plt
import Conversion
from datetime import datetime

mean = 1/7
windows = np.arange(0,1.5,0.1) 

#distribution1 = np.random.exponential(mean,1000000)
#distribution2 = np.random.exponential(mean,1000000)
#distribution2 = distribution1

#origin1 = [7.249768647]
#origin2 = [0.006497556]
#data2 = [7.249768647+window*1.0001]

def randoms_distribution(mean, nb_tot, origin1, origin2):
    distribution1 = np.random.exponential(mean,nb_tot)
    distribution2 = np.random.exponential(mean,nb_tot)
    #distribution2 = distribution1
    data1 = origin1
    data2 = origin2
    #data2 = [7.249768647+window*1.0001]

    for i in range(len(distribution1)):
        data1.append(data1[i] + distribution1[i])
        
    for i in range(len(distribution2)):
        data2.append(data2[i] + distribution2[i])

    if data1[0] <= data2[0]:
        list1 = data2
        list2 = data1

    else :
        list1 = data1
        list2 = data2

    return list1, list2

#list1, list2 = randoms_distribution(mean, 1000000, origin1, origin2)

list1 = Conversion.list1
list2 = Conversion.list2

def coincidence(list1, list2, window):
    m = len(list1)
    id_n = 0
    coincidence_sortie = []
    for i in range(m):
        while id_n < len(list2):
            if list2[id_n] >= list1[i] :
                if abs(list2[id_n] - list1[i]) <= window :
                    coincidence_sortie.append(list1[i])
                elif abs(list1[i] - list2[id_n - 1]) <= window :
                    coincidence_sortie.append(list1[i])
                break
            id_n += 1
    return coincidence_sortie

def deltamin(list1, list2):
    m = len(list1)
    dmin = np.zeros((m, 1))
    for i in range(m):
        if i/100 == int(i/100):
            print(i)
        dmin[i] = min(abs(list2 - list1[i]))
    return dmin

def deltat(list1, list2):
    m = len(list1)
    delta = list2 - list1[0]
    delta_ns = delta / np.timedelta64(1, 'ns')
    fenetre = 1e6
    hist_tot, x = np.histogram(delta_ns[abs(delta_ns)<1e9], bins=10000, range=(-fenetre, fenetre))
    for i in range(1, m):
        if i/100 == int(i/100):
            print(i)
        delta = list2 - list1[i]
        delta_ns = delta / np.timedelta64(1, 'ns')
        h, _ = np.histogram(delta_ns[abs(delta_ns)<1e9], bins=10000, range=(-fenetre, fenetre))
        #print(h, len(h))
        hist_tot += h
        #print(hist_tot, len(hist_tot))
    return hist_tot, x

#dmin = deltamin(list1, list2)
#plt.hist(dmin[dmin<1000000])
#plt.savefig('histogramme_muons.jpg')
#plt.show()


#hist_tot, x = deltat(list1, list2)
#plt.plot(x[:-1], hist_tot)
#plt.show()

#window = (1/3)*(10**-5)
#window = np.timedelta64(100000, "ns")

#windows = np.array([0, 1000, 10000, 100000, 1000000])
#windowsLen = len(windows)
#windows_datetime = []
#for i in range (windowsLen):
#    windows_datetime.append(np.timedelta64(int(windows[i]), "ns"))
    
#nb_coincidence = []
#for window in windows_datetime:
#    nb_coincidence.append(len(coincidence(list1, list2, window)))
    #print(coincidence(list1, list2, window))

#print(nb_coincidence)
#print(len(coincidence(list1, list2, window)))
#plt.plot(windows, nb_coincidence,'.k')
#plt.show()


delta = list1 - list2
delta_ns = delta / np.timedelta64(1, 'ns')
delta_s = delta / np.timedelta64(1, 's')
list1_s = list1.astype('float') * 1e-9
clock = list1_s % 1

plt.plot(clock, delta_ns, '+')
plt.show()