#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import numpy as np
import pprint
import pandas as pd
import time
# import plotly.graph_objects as go

# empty dataframe hidden until user inputs data
df = pd.DataFrame()


# In[7]:


st.title('CSE Calcul ASC 2023')
st.write('')


# In[ ]:


# add some space between photo and instructions
st.write('')
st.subheader('vous pouvez saisir vos informations pour le calcul ASC')


# In[9]:


# Function to convert 
copper = 1/100
silver = 1/10
electrum = 1/2
gold = 1
platinum = 10


def getCoins(coins, amount, coinIndex = 0):
    
    amount = float(amount)
    if amount == 0:
        return [] # all done! You did it!
    if coinIndex >= len(coins):
        return None # don't have enough money / coins
    
    # names of coins to print later
    coinNames = ['', 'Copper', 'Silver']
    
    # start calculations
    coin = coins[coinIndex] # 1= gold, 2= platinum, ...
    coinIndex += 1 
    # First, take as may as possible from first listed coin (will start at Index 1 (gold))
    canTake = int(min(amount / coin['value'], coin['count']))
    
    #Reduce the number taken from this coin until success
    for count in np.arange(canTake, -1.0, -1):  # take away 1 until count reaches 0
        
        # Recurse to decide how many to take from next coin
        change = getCoins(coins, amount - coin['value'] * count, coinIndex)
        if change != None: # Success! We are done!
            if count: # Register this number for this coin
                return change + [{'Coin Name': coinNames[coinIndex], 'Amount': int(count)}]
            return change


# In[ ]:


# create placeholders to clear inputs when clicking "start over" button
placeholder_c = st.empty()
placeholder_s = st.empty()



# In[9]:


# have user input the amount they have for each coin

userNumCopper = placeholder_c.number_input('Revenu fiscal de reference 2023 (sur les revenus 2022) en euros: ', min_value= 0, value=100000, step=0.5)
userNumSilver = placeholder_s.number_input('Nombre de parts ', min_value= 1, step=0.5)



# In[ ]:


# tell user how much they have in gold pieces

totalGold = (userNumCopper / userNumSilver / 12) 
totalGold = round(totalGold)

st.subheader(f'Votre Quotient Familial {totalGold:,d} .')


# In[ ]:


st.write('')

if totalGold > 2200:
    st.write('Vous avez l\'enveloppe standard de 183 euros.')
    st.write('Pas besoin de venir nous voir :) ')
elif 1700 < totalGold <= 2200 :
   st.write('Vous avez une enveloppe de 250 euros.')
elif 1200 < totalGold <= 1700:
    st.write('Vous avez une enveloppe de 350 euros.')
elif totalGold <= 1200:
    st.write('Vous avez une enveloppe de 450 euros.')
else: 
    st.write('Vous avez une enveloppe bonifiée.')
    st.write('Vous pouvez venir nous voir!! :) ')



# In[ ]:


# create dividing line to separate calculations from reset
st.write('-------------------------')


# In[ ]:


# create columns to right align restart button
col1, col2, col3 = st.columns([1,1,.5])
click_clear = col3.button('Start Again')

# set fields back to 0 when clicking button
if click_clear:

    userNumCopper = placeholder_c.number_input('Enter number of Copper: ', 
                                               min_value= 0, value= 0, key= 'redo')
    userNumSilver = placeholder_s.number_input('Enter number of Silver: ', 
                                               min_value= 1, value= 1, key= 'redo1')

    col3.write('The values have been reset')
    st.balloons()



