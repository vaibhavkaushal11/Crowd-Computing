import statistics
import matplotlib.pyplot as plt
estimates = [1000,500,425,145,100,125,178,180,950,1256,785,652,143,254,692,286,349,517,1100,475]
estimates.sort()
tv= int(0.1*len(estimates))
estimates = estimates[tv:]
estimates = estimates[:len(estimates)-tv]
y=[]
for number in range(len(estimates)):
	y.append(5)
plt.plot(estimates,y,'ro')
s = statistics.mean(estimates)
print("Desired Mean = ",s)
plt.plot(s,[5],'g^')
plt.show()
