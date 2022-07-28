# International Cosmic Day
## Data analysis
### My implementetion
``` python
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
``` 
### Results 
<figure>
<img src="/assets/print.PNG" align="center" height = "250" widht= "400"/>
<figcaption>
<p>Console print of the value of <b>variance</b>, <b>covariance</b>, <b>parameters of the fit</b>.</p>
</figcaption>
</figure>

<figure>
<img src="/assets/fir_doppie.png" align="center" height = "250" widht= "400"/>
<figcaption>
  <p> Linear fit for <b>double</b>.</p>
</figcaption>
</figure>
