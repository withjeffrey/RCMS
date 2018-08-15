X = list(range(10000))
YCE = []
YCA = []
YSB = []
YSBV = []

#定义Cloud Essential
YCE[0:50] = [10*i for i in X[0:50]]
YCE[50:100] = [9*i for i in X[50:100]]
YCE[100:250] = [8.5*i for i in X[100:250]]
YCE[250:] = [8*i for i in X[250:]]

#定义Cloud Advanced
YCA[0:50] = [40*i for i in X[0:50]]
YCA[50:100] = [38*i for i in X[50:100]]
YCA[100:250] = [36*i for i in X[100:250]]
YCA[250:] = [34*i for i in X[250:]]

#定义Stack Basic with Rlink only (suggested servers)
YSB[0:5000] = [30000-10000 for i in X[0:5000]]
YSB[5000:] = [30000-10000 for i in X[5000:]]

#定义Stack Basic with RVPN (suggested servers)
YSBV[0:150] = [30000-10000 for i in X[0:150]]
YSBV[150:400] = [30000+10000-10000 for i in X[150:400]]
YSBV[400:900] = [30000+12500-10000 for i in X[400:900]]
YSBV[900:1900] = [30000+20000-10000 for i in X[900:1900]]
YSBV[1900:4400] = [30000+37500-10000 for i in X[1900:4400]]
YSBV[4400:9400] = [30000+50000-10000 for i in X[4400:9400]]
YSBV[9400:10000] = [30000+50000+20000-10000 for i in X[9400:10000]]

#绘制图形
import matplotlib.pyplot as plt
plt.plot(X,YCE,label='Cloud with Rlink only')
plt.plot(X,YCA,label='Cloud with Rlink and RVPN')
plt.plot(X,YSB,label='Stack with Rlink only')
plt.plot(X,YSBV,label='Stack with Rlink and RVPN')
plt.xlabel('device number')
plt.ylabel('price in first year')
plt.legend()
plt.show()
