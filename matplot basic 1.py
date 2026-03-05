#import matplotlib.pyplot as plt
#print("module ok")
#score=[10,25,35,45,60,77,88,90,99]
#plt.plot(score)
#plt.show()

#import mat#plotlib.pyplot as plt
#print("module ok")
#score=[10,25,35,45,60,77,88,90,99]
#plt.xlabel("overs")
#plt.ylabel("runs")
#plt.plot(score)
#plt.show

#import matplotlib.pyplot as plt
#print("module ok")
#overs=[1,2,3,4,5,6,7,8,9,10,11]
#score=[10,25,35,45,54,60,66,77,88,90,99]
#plt.title("India Cricket Scores")
#plt.xlabel("overs")
#plt.ylabel("runs")
#plt.plot(overs,score)
#plt.show()

#import matplotlib.pyplot as plt
#plt.title("student mark list")
#rno=[1001,1002,1003,1004,1005,1006,]
#avg=[99.5,44.5,55.6,77.9,89.8,67.9]
#plt.grid(True)
#plt.axis([999,1010,0,100])
#plt.plot(rno,avg)
#plt.show()

#import matplotlib.pyplot as plt
#ind=[11,19,31,44,55,66,70,88,99,110]
#aus=[22,30,40,44,50,60,72,81,90,101]
#overs=[1,2,3,4,5,6,7,8,9,10]
#plt.plot(overs,ind,label="INDIA")
#plt.plot(overs,aus,label="AUSTRALIA")
#plt.plot(overs,ind,"bs")
#plt.plot(overs,aus,"ro")
#plt.legend()
#plt.grid(True)
#plt.title("India vs Australia")
#plt.show()

import matplotlib.pyplot as plt
ind=[11,19,31,44,55,66,70,88,99,110]
aus=[22,30,40,44,50,60,72,81,90,101]
overs=[1,2,3,4,5,6,7,8,9,10]
plt.plot(overs,ind,label="INDIA")
plt.plot(overs,aus,label="AUSTRALIA")
plt.plot(overs,ind,"b^")
plt.plot(overs,aus,"ro")
plt.legend()
plt.grid(True)
plt.title("India vs Australia")
plt.xlabel("Team india and australia")
plt.ylabel("overs")
for i in range(0,10):
    plt.text(overs[i],ind[i],ind[i])
for i in range(0,10):
    plt.text(overs[i],aus[i],aus[i])
plt.savefig("padam.jpg")    
plt.show()
