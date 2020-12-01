import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

R0 = 3.25
N=100
I0 = 10

gamma = 1/14 #recovery rate
sigma = 1/7 #incubation
beta = R0*gamma #contact rate

# s_pop_0 = 69000000
# e_pop_0 = 0
# i_pop_0 = 360
# r_pop_0 = 0


s_pop_0 = 1000
e_pop_0 = 0
i_pop_0 = 1
r_pop_0 = 0

print("gamma : ", gamma)
print("beta : ", beta)
print("sigma : ", sigma)

class SEIR :

    def __init__(self,t0=0, steps=100, Susceptible=950, Exposed = 100, Infected=50, Resistant=0, rateSI=beta, rateIR=gamma, rateEI =sigma):
        self.t0 = t0
        self.steps = steps
        self.Susceptible = Susceptible
        self.Exposed = Exposed
        self.Infected = Infected
        self.Resistant = Resistant
        self.rateSI = rateSI #beta
        self.rateEI = rateEI #sigma
        self.rateIR = rateIR #gamma
        self.numIndividuals = Susceptible + Infected + Resistant + Exposed # total population
        self.results = None
        self.modelRun = False

    def init(self,t0=0, steps=100, Susceptible=950, Exposed = 100, Infected=50, Resistant=0, rateSI=beta, rateIR=gamma, rateEI = sigma):
        print(t0, steps,R0)

        self.t0 = t0
        self.steps = steps
        self.Susceptible = Susceptible
        self.Exposed = Exposed
        self.Infected = Infected
        self.Resistant = Resistant
        self.rateSI = rateSI #beta
        self.rateEI = rateEI #sigma
        self.rateIR = rateIR #gamma
        self.numIndividuals = Susceptible + Infected + Resistant + Exposed # total population
        self.results = None
        self.modelRun = False

    def run(self, death_rate=0):
        Susceptible = [self.Susceptible]
        Exposed = [self.Exposed]
        Infected = [self.Infected]
        Resistant = [self.Resistant]
        time = list(range(self.t0,self.t0+self.steps))
        print("beta",self.rateSI)

        for step in range(self.t0+1, self.t0 + self.steps):
            S_to_E = (self.rateSI * Susceptible[-1] * Infected[-1]) / self.numIndividuals
            E_to_I = (self.rateEI * Exposed[-1])
            I_to_R = (Infected[-1] * self.rateIR)

            Susceptible.append(Susceptible[-1] - S_to_E)
            Exposed.append(Exposed[-1] + S_to_E - E_to_I)
            Infected.append(Infected[-1] + E_to_I - I_to_R)
            Resistant.append(Resistant[-1] + I_to_R)

        # Death is death_rate* recovery group
        Death = list(map(lambda x: (x * death_rate), Resistant))
        # Heal is removed - Death
        Heal = list(map(lambda x: (x * (1 - death_rate)), Resistant))
        self.results = pd.DataFrame.from_dict({'Time': time,
                                               'Susceptible': Susceptible, 'Exposed': Exposed, 'Infected': Infected,
                                               'Resistant': Resistant,
                                               'Death': Death, 'Heal': Heal},
                                              orient='index').transpose()
        self.modelRun = True
        return self.results

    def plot(self,  all = False):
        if self.modelRun == False:
            print('Error: Model has not run. Please call SIR.run()')
            return
        print("Maximum infected case: ",
              format(int(max(self.results['Infected']))))
        if plt.get_fignums():
            pass
        else :
            fig, ax = plt.subplots(figsize=(10, 6))

        if all :
            plt.plot(self.results['Time'], self.results['Susceptible'], color='blue')
            plt.plot(self.results['Time'], self.results['Infected'], color='red')
            plt.plot(self.results['Time'], self.results['Exposed'], color='orange')
            # plt.plot(self.results['Time'], self.results['Resistant'], color='palegreen')
            plt.plot(self.results['Time'], self.results['Heal'], color='green')
            plt.plot(self.results['Time'], self.results['Death'], color='grey')

        else :
            plt.plot(self.results['Time'], self.results['Infected'])    
            # plt.plot(self.results['Time'], self.results['Infected'], color='red')
            # plt.plot(self.results['Time'], self.results['Exposed'], color='orange')



    def display(self,title, ylabel, xlabel,all = False):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if all :
            plt.legend(['Susceptible', 'Infected', 'Exposed', 'Heal', 'Death'], prop={'size': 12},
                    fancybox=True, shadow=False)
        else :
            plt.legend(['Infected'], prop={'size': 12},
                       bbox_to_anchor=(0.5, 1.02), ncol=6, fancybox=True, shadow=True)
        plt.title(title, fontsize = 20)


def run_periods(model,times,R0_list):
    "run the SEIR model for the given periods times/RO_list"
    #first period
    t0 = times[0]
    tf = times[1]
    R0 = R0_list[0]
    beta = R0*gamma
    seir_model=model
    seir_model.init(t0,tf,s_pop_0,e_pop_0,i_pop_0,r_pop_0,beta,gamma,sigma)
    res = seir_model.run(0.1)
    seir_model.plot(all=True)

    #next period
    for i in range(1,len(R0_list)):
        R0 = R0_list[i]
        beta = R0*gamma
        t0 = times[i]
        tf = times[i+1]
        seir_model.init(t0, tf-t0+1, res["Susceptible"].iloc[-1], res["Exposed"].iloc[-1], res["Infected"].iloc[-1],
                        res["Resistant"].iloc[-1], beta)
        res = seir_model.run(0.1)
        seir_model.plot(all=True)

    seir_model.display("seir model","pop","days",all=True)
    plt.show()

times = [1,59,69,79,120]
R0_list = [3.25,2,1,0.6]
seir_model = SEIR(times,R0_list)


times = [1,100]
R0_list = [10]
seir_model = SEIR(times,R0_list)
run_periods(seir_model,times,R0_list)
