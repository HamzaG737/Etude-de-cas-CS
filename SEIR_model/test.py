import matplotlib.pyplot as plt
import numpy as np

R0 = 3.25
N=67000000
I0 = 360

gamma = 1/14 #recovery rate
beta = R0*gamma #contact rate
sigma = 1/7 #incubation

print("gamma : ",gamma)
print("beta : ",beta)
print("sigma : ",sigma)

s_pop =[]
e_pop =[]
i_pop =[]
r_pop =[]

#initial values
s_pop.append(N-I0)
e_pop.append(I0)
i_pop.append(0)
r_pop.append(0)

def add_1_day(s_pop,e_pop,i_pop,r_pop,N,sigma,gamma,beta):
    s_new = s_pop[-1] - (beta * s_pop[-1] * i_pop[-1]) / N
    e_new = e_pop[-1] + (beta * s_pop[-1] * i_pop[-1]) / N - sigma * e_pop[-1]
    i_new = i_pop[-1] + sigma * e_pop[-1] - gamma * i_pop[-1]
    r_new = r_pop[-1] + gamma * i_pop[-1]

    s_pop.append(s_new)
    e_pop.append(e_new)
    i_pop.append(i_new)
    r_pop.append(r_new)

    return s_pop,e_pop,i_pop,r_pop

t0=1
tp0=57
tf0 = t0+tp0

for i in range (t0+1,tf0):
    s_pop,e_pop,i_pop,r_pop = add_1_day(s_pop,e_pop,i_pop,r_pop,N,sigma,gamma,beta)

print("end phase 1 :",e_pop[-1]+i_pop[-1])
t1= tf0
tp1 = 15
tf1= t1+tp1
R0 = 2.76
beta = R0*gamma #contact rate

for i in range (t1,tf1):
    s_pop,e_pop,i_pop,r_pop = add_1_day(s_pop,e_pop,i_pop,r_pop,N,sigma,gamma,beta)


print("end phase 2 :",e_pop[-1]+i_pop[-1])
t2= tf1
tp2=15
tf2= t2+tp2
R0 = 1.9
beta = R0*gamma #contact rate

for i in range (t2,tf2):
    s_pop,e_pop,i_pop,r_pop = add_1_day(s_pop,e_pop,i_pop,r_pop,N,sigma,gamma,beta)


print("end phase 3 :",e_pop[-1]+i_pop[-1])
t3= tf2
tp3=79
tf3= t3+tp3
R0 = 0.5
beta = R0*gamma #contact rate

for i in range (t3,tf3):
    s_pop,e_pop,i_pop,r_pop = add_1_day(s_pop,e_pop,i_pop,r_pop,N,sigma,gamma,beta)


t_list = list(range(t0,tf3))

# plt.plot(t_list,s_pop,label='s')
# plt.plot(t_list,e_pop,label='e')
# plt.plot(t_list,i_pop,label='i')
# plt.plot(t_list,r_pop,label='r')
total_infected = np.array(e_pop)+np.array(i_pop)
plt.plot(t_list,total_infected,label = "total infected")
plt.xlabel("day")
plt.ylabel("infected + exposed")
plt.legend()

plt.show()

print("s_pop : ",s_pop)
print("e_pop ", e_pop)
print("i_pop : ", i_pop)
print("r_pop : ", r_pop)

print("end")
