from pylab import *

N = 10000
tid = 20
dt = tid/N


a = zeros(N)
v = zeros(N)
t = zeros(N)
s = zeros(N)

g = 9.81
k = 0.1
m = 0.25
t[0] = 0
v[0] = 100
s[0] = 1.6

for i in range(N-1):
    a[i] = ((k*abs(v[i])**2)/m)-g
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = s[i] + v[i]*dt
    t[i+1] = t[i] + dt
   
subplot(3,1,1)
plot(t[:-1], a[:-1], 'b')

subplot(3,1,2)
plot(t, v, 'r')

subplot(3,1,3)
plot(t, s, 'g')