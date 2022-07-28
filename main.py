import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import curve_fit
from matplotlib.pyplot import plot, figure, clf
from IPython.display import display, clear_output, Image
import math
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

#Initialize columns and load file
colonne = ['angle','xy','yz','zw','xyz','yzw','xyzw']
df = pd.read_table("data21.txt", skiprows=0, sep='\s+', header=None, names=colonne)

#Average the counts of adjacent doubles and triples

deltat21=3. 
nint21=600 #number of time intervals

av_count_double=(df["xy"]+df["yz"]+df["zw"])/3
rate_double=av_count_double/deltat21 
rate_error_double=np.sqrt(av_count_double/nint21)/deltat21


av_cont_triple=(df['xyz']+df['yzw'])/2.
rate_triple=av_cont_triple/deltat21
rate_error_triple=np.sqrt(av_cont_triple/nint21)/deltat21


count_quadruple=df['xyzw']
rate_quadruple=count_quadruple/deltat21
rate_error_quadruple=np.sqrt(count_quadruple/nint21)/deltat21

#plot
fig, ax = plt.subplots(figsize=(10,8))
plt.ylabel("Rate Counts [Hz]")
plt.xlabel("theta [deg]")
plt.errorbar(df["angle"],rate_double,yerr=rate_error_double,marker='o',linestyle='None',label="double")
plt.errorbar(df["angle"],rate_triple,yerr=rate_error_triple,marker='o',linestyle='None',label="triple")
plt.errorbar(df["angle"],rate_quadruple,yerr=rate_error_quadruple,marker='o',linestyle='None',label="quadruple")
plt.legend(loc='upper right')

fig, ax = plt.subplots(figsize=(10,8))

# calculate cos^2(theta)
cos2=np.cos(np.radians(df["angle"]))**2
plt.ylabel("Count Rate [Hz]")
plt.xlabel("cos$^2$(theta)")
plt.errorbar(cos2,rate_double,yerr=rate_error_double,marker='o',linestyle='None',label="data")

# linear fit
pp,residuals, _, _, _ = np.polyfit(cos2,rate_double,1,w=1./rate_error_double,full=True,cov=True)
xval = np.linspace(0, 1)
polynomial_p = np.poly1d(pp)
yval_p = polynomial_p(xval)
plt.plot(xval,yval_p,'-', color='g',label="double linear_fit")
plt.legend(loc='upper left')


#variance
dataset = [rate_double]
variance = np.var(dataset)
print('double_variance:', variance)

#covariance
covariance= (len(cos2)-1)/len(cos2)*np.cov([cos2, rate_double]) 
covar=covariance[1,0]
stdx_0=np.sqrt(covariance[0,0])
stdy_0=np.sqrt(covariance[1,1])
stdx=np.sqrt(np.var([cos2]))
stdy=np.sqrt(np.var([rate_double]))
Coeffcorr=covar/(stdx*stdy)
print('Coefficient of correlation - double (manual):', Coeffcorr)
r_2 = (Coeffcorr**2) 
print('Coefficient of determination - double (manual):', r_2)

#calcolo coefficiente di determinazione
x_values = [cos2]
y_values = [rate_double]
correlation_matrix = np.corrcoef(x_values, y_values)
correlation_xy = correlation_matrix[0,1]
print('Coefficient of correlation - double (numpy):', correlation_xy)
r_squared = (correlation_xy**2) 
print('Coeffcient of determination - double (numpy):', r_squared)

print('Fit Parameter double: y = %.3f * x + %.3f\n\n' % (pp[0], pp[1]))



###############################################################################
# Let's run the same code snippet to get the linear fit of triple and quadruple
###############################################################################

#triple

fig, ax = plt.subplots(figsize=(10,8))
cos2=np.cos(np.radians(df["angle"]))**2
plt.ylabel("Count Rate [Hz]")
plt.xlabel("cos$^2$(theta)")
plt.errorbar(cos2,rate_triple,yerr=rate_error_triple,marker='o',linestyle='None',label="data")
pp,residuals, _, _, _ = np.polyfit(cos2,rate_triple,1,w=1./rate_error_triple,full=True,cov=True)
xval = np.linspace(0, 1)
polynomial_p = np.poly1d(pp)
yval_p = polynomial_p(xval)
plt.plot(xval,yval_p,'-', color='r',label="triple linear_fit")
plt.legend(loc='upper left')
dataset3 = [rate_triple]
variance3 = np.var(dataset3)
print('Triple variance:', variance3)
array_1 = np.array([cos2])
array_2 = np.array([rate_triple])
covariance3= np.cov(array_1, array_2)[0][1]
print('Triple covariance:', covariance3)
x_values = [cos2]
y_values = [rate_triple]
correlation_matrix = np.corrcoef(x_values, y_values)
correlation_xy = correlation_matrix[0,1]
print('Coefficient of correlation - triple:', correlation_xy)
r_squared = correlation_xy**2
print('Coeffcient of determination - triple:', r_squared)
print('Fit parameter triple: y = %.3f * x + %.3f\n\n' % (pp[0], pp[1]))


# quadruple

fig, ax = plt.subplots(figsize=(10,8))
cos2=np.cos(np.radians(df["angle"]))**2
plt.ylabel("Count rate [Hz]")
plt.xlabel("cos$^2$(theta)")
plt.errorbar(cos2,rate_quadruple,yerr=rate_error_quadruple,marker='o',linestyle='None',label="dati")
pp,residuals, _, _, _ = np.polyfit(cos2,rate_quadruple,1,w=1./rate_error_quadruple,full=True,cov=True)
xval = np.linspace(0, 1)
polynomial_p = np.poly1d(pp)
yval_p = polynomial_p(xval)
plt.plot(xval,yval_p,'-', color='y',label="quadruple linear_fit")
plt.legend(loc='upper left')
dataset4 = [rate_quadruple]
variance4 = np.var(dataset4)
print('Qudruple_variance:', variance4)
array_1 = np.array([cos2])
array_2 = np.array([rate_quadruple])
covariance4= np.cov(array_1, array_2)[0][1]
print('Qudruple_covariance:', covariance4)
x_values = [cos2]
y_values = [rate_quadruple]
correlation_matrix = np.corrcoef(x_values, y_values)
correlation_xy = correlation_matrix[0,1]
print('Coefficient of correlation - quadruple:', correlation_xy)
r_squared = correlation_xy**2
print('Coeffcient of determination - quadruple:', r_squared)
print('Fit Parameters - quadruple: y = %.3f * x + %.3f\n\n' % (pp[0], pp[1]))
plt.show()