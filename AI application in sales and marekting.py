#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import matplotlib.pyplot as plt
import random


# In[ ]:


#choose rqndo, number from function distribution beta,   then see which strqtegy brignd the best result
#tampsong is giving a chance to the thing thqt gives you the best chance


# In[13]:


#create an envirenment
#setting the parameters
conversionRates=[0.05,0.13,0.09,0.16,0.11,0.04,0.20,0.08,0.01] 
N=10000 
d=len(conversionRates) 


# In[14]:


#Building the envirenment  inside a simultion
X=np.zeros((N,d)) 
for i in range(N):
    for j in range (d):
        if np.random.rand() < conversionRates[j]: # if the random, number between 0 ,1    x<0.15 =1  ,x>0.15= 0
            X[i][j]=1


# In[20]:


sum(X)  #see number of rewards which is conversion rate*10000 


# In[15]:


#rewards
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)


# In[16]:


#taking our best slotmachine throufh beta distribution  and updting losses and wins   
#tirage aleatoire de tompson
for i in range(N) :
    selected = 0
    maxRandom = 0
    for j in range(d) :
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            maxRandom = randomBeta
            selected = j
    if X[i][selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1
            
        
# we updated our npos and neg depending on whether you have won or not . we can do that with code 


# In[17]:


#showing which slot machine is considered the best 
nSelected = nPosReward + nNegReward
for i in range(d):
    print('Machine number ' + str(i+1) + ' was selected ' + str(nSelected[i]) + ' times')
print('Conclusion: Best machine is machine number ' + str(np.argmax(nSelected) + 1))


# In[79]:


N=10000
d=9


# In[80]:


conversion_rates=[0.05,0.13,0.09,0.16,0.11,0.04,0.20,0.09,0.01]
x=np.array(np.zeros([N,d]))
for i in range(N):
    for j in range (d):
        if np.random.rand() <= conversion_rates[j]:
            x[i,j]=1


# In[81]:


sum(x)


# In[85]:


#Implementing Random Selection and Tompson Sampling 
strategies_selected_rs=[]
strategies_selected_ts=[]
total_reward_rs=0
total_reward_ts=0
numbers_of_rewards_1=[0]*d
numbers_of_rewards_0=[0]*d


# In[86]:


for n in range(0,N):
    
    #random selection
    strategy_rs=random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs=X[n,strategy_rs]
    total_reward_rs=total_reward_rs+reward_rs
    
    #thompson selection
    strategy_ts=0
    max_random=0
    for i in range(0,d):
        random_beta=random.betavariate(numbers_of_rewards_1[i]+1,numbers_of_rewards_0[i]+1)
        if random_beta>max_random:
            max_random=random_beta
            strategy_ts=i
        reward_ts=X[n,strategy_ts]
        if reward_ts==1:
            numbers_of_rewards_1[strategy_ts]=numbers_of_rewards_1[strategy_ts]+1
        else:
            numbers_of_rewards_0[strategy_ts]=numbers_of_rewards_0[strategy_ts]+1
    strategies_selected_ts.append(strategy_ts)
    total_reward_ts=total_reward_ts+reward_ts
    
        


# In[ ]:





# In[87]:


#to see if the strategy is good we will add an a=indicator
#computing the relative return
relative_return=(total_reward_ts - total_reward_rs)/total_reward_rs*100
relative_return


# In[88]:


#plotting the histogram
plt.hist(strategies_selected_ts)
plt.title('histogram of Selections')
plt.xlabel('strategy')
plt.ylabel('number of times the strategy was selected')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




