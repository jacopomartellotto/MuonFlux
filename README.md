# International Cosmic Day
The International Cosmic Day took place on November 10, 2021. On this day, the focus is on the science related to cosmic rays. These are invisible messengers from the cosmos that constantly permeate us, bringing messages that allow us to understand the Universe. 
Furthermore, each participating student has the opportunity to draw up a report and participate in the competition, of which I was the winner, "Stage at the Frascati Laboratories".
In the <a href="Relation.pdf">report</a> you can find a reference to the data analysis conducted in the laboratories, after the launch of a stratospheric balloon. <br>
<b>The INFN group of Lecce, which organized the day, illustrated the physics of cosmic rays and presented the python code, which I subsequently implemented with the calculation of variance and covariance, for the dtai analysis.</b>
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
<p align="center">
<img width="460" height="300" src="/assets/print.PNG">
<figcaption>
<p align="center">Console print of the value of <b>variance</b>, <b>covariance</b>, <b>parameters of the fit</b>.</p>
</figcaption>
</p>

<p align="center">
<img width="537.6" height="268.5" src="/assets/plot.png">
<figcaption>
<p align="center"><b>Plot</b>.</p>
</figcaption>
</p>

<p align="center">
<img width="768" height="383.5" src="/assets/fit_doppie.png">
<figcaption>
<p align="center">Linear fit for <b>double</b>.</p>
</figcaption>
</p>

<p align="center">
<img width="768" height="383.5" src="/assets/fit_triple.png">
<figcaption>
<p align="center">Linear fit for <b>triple</b>.</p>
</figcaption>
</p>

<p align="center">
<img width="768" height="383.5" src="/assets/fit_quadruple.png">
<figcaption>
<p align="center">Linear fit for <b>quadruple</b>.</p>
</figcaption>
</p>
