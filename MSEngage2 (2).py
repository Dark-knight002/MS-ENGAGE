#!/usr/bin/env python
# coding: utf-8

# In[105]:


from numpy import *
from pandas import *
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
set_option('display.max_columns',None) 
import streamlit as st
from PIL import Image


# In[106]:


st.title("DATA ANYLASIS OF AUTOMOBILE INDUSTRY")


# In[107]:


st.markdown("#### Hey there this a web app for data anylasis on automobile industry. It consist of 3 sections namely: ")
st.markdown("#### Section A -  Know your dataset (This answers the basic questions related to dataframe)")
st.markdown("#### Section B - Important Features of dataset (This section answers the indepth questions about the features and gives important data anylasis. This section explains the relation through graphs and plots and at the end summarizes it. There are separate buttons for each functionality)")
st.markdown("#### Section C - Important Correlations and Information.(This section forms important correlations between features and helps forming the business use case from the given dataset. This section is explained through graphs and plots and also summarizes the information from the plots. There are separate buttons for each functionality)")
st.markdown("#### The link for the dataset is: https://docs.google.com/spreadsheets/d/1eW3ipCvxaKTMWup_AMLgRfEp5hrDuNa0/edit?usp=sharing&ouid=101164161980498112535&rtpof=true&sd=true")


# In[108]:


image = Image.open('h.jpg')

st.image(image)


# In[109]:


st.markdown("# **SECTION-A**")


# In[110]:


st.markdown("# *GET TO KNOW UR DATAFRAME*")


# In[111]:


st.markdown("### 1.GET A VIEW OF YOUR DATAFRAME")


# In[112]:


data=pandas.read_excel('Automobile_data.xlsx')

test = data.head().astype(str)

button1 = st.button(" The Dataframe")
if button1:
    
    st.table(test)
    


# In[113]:


st.markdown("---")


# In[ ]:





# In[114]:


st.markdown("### 2.GET SOME ADVANCED INFORMATION ABOUT YOUR DATASET")


# In[115]:


Info2 = data.describe()

button3 = st.button("ADVANCED INFORMATION ABOUT DATASET")

if button3:
    st.write(Info2)


# In[116]:


st.markdown("---")


# In[117]:


st.markdown("### 3.GET THE DIMENSIONS OF THE DATASET")


# In[118]:


button41 = st.button("DIMENSIONS")

if button41:
    Info10 = data.shape
    st.write(Info10)


# SHOW INFO FUNCTION (its a function to show the missing values)

# In[119]:


def show_info(col):
    print(f'Type of {col} : {data[col].dtype}')
    print(data[col].value_counts())
    print(f'Number of missing values : {data[col].isnull().sum()}')


# SHOW DISTRIBUTION OUTLIERS FUNCTION (it displays the outliers)

# In[120]:


def show_distribution_outliers(col):
    f=plt.figure(figsize=(20,9))
    ax=f.add_subplot(121)
    sns.boxplot(data=data,x=col,ax=ax)
    ax.set_title('Show outliers')

    ax=f.add_subplot(122)
    data.hist(col,ax=ax)
    ax.set_title(f'{col} Distribution')


# In[121]:


st.text("")


# In[122]:


st.text("")


# In[123]:


st.markdown("# **SECTION B**")


# In[124]:


st.markdown("# *INFORMATION OF IMPORTANT COLOUMNS OF DATASET*")


# In[125]:


st.markdown("### 1.NORMALIZED LOSSES")


# # Data Cleaning & Some Visualization

# In[126]:


data['normalized-losses']=to_numeric(data['normalized-losses'],downcast='integer',errors='coerce')


    


# In[127]:


# show the outliers of the column & his distribution

button4 = st.button("Show the information about Normalized-Losses")


if button4:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_distribution_outliers('normalized-losses'))
    

button5 = st.button("SUMMARY OF NORMALIZED LOSSES")

if button5:
    
    st.markdown("## From the plot - the biggest normalized losses is in range 100 to 125")
    
    



# From the plots :
#     
#     
# -the biggest normalized losses is in range 100 to 125

# In[128]:


#In this case , the best way to refill the missing values is median
data.fillna({'normalized-losses':data['normalized-losses'].median()},inplace=True)

#To cross check whether there are more 
data['normalized-losses'].isnull().sum()


# In[129]:


st.markdown("---")


# In[130]:


st.markdown("### 2.MAKE")


# In[ ]:





# Function to show the precentage of each column in the plot

# In[131]:



def show_percent(col):
    plt.figure(figsize=(20,12))
    ax=sns.countplot(data=data,x=col)
    plt.xticks(rotation=90)
    plt.title(f'{col} Distribution')
    
    total=float(len(data))
    for p in ax.patches:
        height=p.get_height()
        percent=(height*100)/total
        ax.text(p.get_x()+p.get_width()/2,height+1,'{:.0f}%'.format(percent),ha='center',weight='bold',fontsize=20)


# In[132]:


button6 = st.button("Show the information about Make")

if button6:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_percent('make'))
    


# In[133]:


st.markdown("---")


# In[134]:


st.markdown("### 3.FUEL TYPE")


# In[ ]:






# FUNCTION TO SHOW PIEPLOT FOR DISPLAYING INFORMATION ABOUT A PARTICULAR COLOUMN

# In[135]:


def show_pieplot(col):
    plt.figure(figsize=(10,7))
    x=data[col].value_counts()
    plt.pie(x.values,autopct='%1.1f%%',labels=x.index.tolist());
    plt.title(f'{col} Distribution')


# In[136]:


button7 = st.button("Show the information about fuel type")

if button7:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_pieplot('fuel-type'))
    
button8 = st.button("SUMMARY OF FUEL TYPE")

if button8:
    st.markdown("## THE MORE USED FUEL TYPE IS GAS")


# In[137]:


st.markdown("---")


# In[138]:


st.markdown("### 4.ASPIRATION")


# In[ ]:





# In[139]:


button9 = st.button("Show the information of Aspiration")

if button9:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_pieplot('aspiration'))
    
button10 = st.button("SUMMARY OF ASPIRATION")

if button10:
    st.markdown("## THE MOST USED ASPIRATION TYPE IS STD")


# In[140]:


st.markdown("---")


# In[141]:


st.markdown("### 5.NUM OF DOORS")


# In[ ]:





# In[142]:


#The missing values of num-of-doors will be refilled by 'four'
data['num-of-doors']=data['num-of-doors'].replace('?','four')


# In[143]:


button11 = st.button("Show the information about the Num Of Doors")

if button11:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_pieplot('num-of-doors'))

    
button12 = st.button("SUMMARY OF NUM OF DOORS")

if button12:
    st.markdown("## THE MORE POPULAR VERSION IS THE FOUR DOOR")
    


# THE MORE POPULAR VERSION IS THE FOUR DOOR 

# In[144]:


data.loc[data['num-of-doors']=='four','num-of-doors']=4
data.loc[data['num-of-doors']=='two','num-of-doors']=2


# In[ ]:





# In[145]:


data['num-of-doors']=to_numeric(data['num-of-doors'],errors='coerce')
data['num-of-doors'].dtype


# In[146]:


st.markdown("---")


# In[147]:


st.markdown("### 6.BODY STYLE")


# In[ ]:





# In[148]:


plt.figure(figsize=(12,8))


button13 = st.button("Show the information of body style ")


if button13:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_pieplot('body-style'))
    

button14 = st.button("SUMMARY OF BODY STYLE")

if button14:
    st.markdown("## THE MOST USED IS SEDAN AND THE SECOND IS HATCHBACK")


# THE MOST USED IS SEDAN 
# 
# 
# 
# 
# THE SECOND IS HATCHBACK

# In[149]:


show_info('symboling')


# In[150]:


# In this column , we can observe that it has unsigned values like -1 and -2
# This values will be replaced by 0
data['symboling']=data['symboling'].replace(-1,0)
data['symboling']=data['symboling'].replace(-2,0)


# In[151]:


st.markdown("---")


# In[152]:


st.markdown("### 7.SYMBOLING")


# In[ ]:





# In[153]:


button15 = st.button("Show the information of Symboling")


if button15:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_pieplot('symboling'))
    
button16 = st.button("SUMMARY OF SYMBOLING")

if button16:
    st.markdown("## MAJORITY OF CARS DO NOT HAVE SYMBOLS")


# In[154]:


st.markdown("---")


# In[155]:


st.markdown("### 8.PRICE")


# In[ ]:





# In[156]:


data['price']=to_numeric(data['price'],errors='coerce')


# In[157]:


button17 = st.button("Show the information about Price ")


if button17:
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_distribution_outliers('price'))


# In[158]:


# Also in this case , the best way to refill the missing values is median
data.fillna({'price':data['price'].median()},inplace=True)


# In[159]:



st.markdown("---")


# In[160]:


st.markdown("### 9.Drive Wheels")


# In[ ]:





# In[161]:


button18 = st.button("Show the information about drive wheels")

if button18:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_pieplot('drive-wheels'))
    
button19 = st.button("SUMMARY OF DRIVE WHEELS")

if button19:
    
    st.markdown("## THE MOST COMMON WHEEL IS FWD")


# THE MOST COMMON WHEEL IS FWD 

# In[162]:


st.markdown("---")


# In[163]:


st.markdown("### 10.ENGINE-LOCATION")


# In[ ]:





# In[164]:


button20 = st.button("Show the information of engine location")

if button20:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_pieplot('engine-location'))
    
button21 = st.button("SUMMARY OF ENGINE LOCATION") 

if button21:
    st.markdown("## Engine-location the cars are usually in front of the car")


# Engine-location the cars are usually in front of the car

# In[165]:


st.markdown("---")


# In[166]:


st.markdown("### 11.ENGINE TYPE")


# In[ ]:





# In[167]:


button22 = st.button("Show the Information of Engine Type")

if button22:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_percent('engine-type'))


button23 = st.button("SUMMARY OF ENGINE-TYPE")

if button23:
    st.markdown("## THE MOST USED ENGINE TYPE IS OHC")


# In[168]:


st.markdown("---")


# In[169]:


st.markdown("### 12.NUM OF CYLINDERS")


# In[ ]:





# In[170]:


button24 = st.button("Show the information about num of cylinders")


if button24:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_percent('num-of-cylinders'))
    
    
button25 = st.button("SUMMARY OF NUM OF CYLINDERS")

if button25:
    st.markdown("## THE MOST USED CYLINDER TYPE IS 4")


# In[171]:


st.markdown("---")


# In[172]:


st.markdown("### 13.FUEL SYSTEMS")


# In[ ]:





# In[173]:


button26 = st.button("Show the information  of Fuel-System")

if button26:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_percent('fuel-system'))


button27 = st.button("SUMMARY OF FUEL SYSTEM")

if button27:
    st.markdown("## THE MOST USED FUEL SYSTEM IS MPFI")


# In[174]:


st.markdown("---")


# In[175]:


st.markdown("### 14.BORE")


# In[ ]:





# In[176]:


data['bore']=to_numeric(data['bore'],errors='coerce')


# In[177]:


# show the outliers of the column & his distribution
button28 = st.button("Show information about bore")


if button28:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_distribution_outliers('bore'))


# In[178]:


# There is no outliers , so we can refill missing values by median or mean.
data.fillna({'bore':data['bore'].median()},inplace=True)


# In[179]:


data['stroke']=to_numeric(data['stroke'],errors='coerce')


# In[180]:


st.markdown("---")


# In[181]:


st.markdown("### 15.HORSEPOWER")


# In[182]:


data['horsepower']=to_numeric(data['horsepower'],errors='coerce')


# In[183]:


button29 = st.button("Show the information about Horsepower ")

if button29:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_distribution_outliers('horsepower'))


# In[184]:


# refill missing values by median
data.fillna({'horsepower':data['horsepower'].median()},inplace=True)


# In[185]:


data['peak-rpm']=to_numeric(data['peak-rpm'],errors='coerce')


# In[186]:


st.markdown("---")


# In[187]:


st.markdown("### 16.PEAK-RPM")


# In[188]:


button30 = st.button("Show the information about Peak Rpm ")

if button30:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(show_distribution_outliers('peak-rpm'))


# In[189]:


# There is outlier in column.
data.fillna({'peak-rpm':data['peak-rpm'].median()},inplace=True)


# # PART - 3

# In[190]:


st.text("")


# In[191]:


st.text("")


# In[192]:


st.markdown("# **SECTION C** ")


# In[193]:


st.markdown("# *IMPORTANT CORRELEATIONS AND INFORMATION FROM THOSE* ")


# In[194]:


st.markdown("### 1.Relation between type of the car & price according to body style")


# In[195]:


button31 = st.button("Relation between type of the car & price according to body style")

if button31:
    fig =plt.figure(figsize=(10, 4))
    sns.swarmplot(data=data,x='make',y='price',hue='body-style')
    plt.xticks(rotation=90)
    st.pyplot(fig)
        
        
button32 = st.button("SUMMARY OF RELATION BETWEEN TYPE OF THE CAR AND PRICE ACCORDING TO BODY STYLE")

if button32:
    st.markdown("## 1)Mercedes-Benz is the highest price and the body style of the highest price is a hardtop")
    st.markdown("## 2)Mercedes-Benz made many kinds of body styles like a wagon, sedan, convertible, and hardtop.")
    st.markdown("## 3)The second highest in prices is BMW.")
    st.markdown("## 4)The only kind that BMW works on is a sedan")
    st.markdown("## 5)Also Porsche has high prices. It made different kinds of body types like hatchback, convertible, and hardtop.")
        


# In[196]:


st.markdown("---")


# In[197]:


st.markdown("### 2.Relation between horse power of the car & price")


# In[198]:


button33 = st.button("Relation between horse power of the car & price")

if button33:
    fig=plt.figure(figsize=(20,9))
    sns.swarmplot(data=data,x='horsepower',y='price')
    plt.xticks(rotation=90)
    st.pyplot(fig)
    
    

button34 = st.button("SUMMARY OF RELATION BETWEEN HORSE POWER OF THE CAR AND PRICE")

if button34:
    st.markdown("## THERE IS A STRONG RELATION BETWEEN HORSEPOWER AND PRICE (POSITIVE RELATIONSHIP).")


# In[199]:


st.markdown("---")


# In[200]:


st.markdown("### 3.Relation between make and price according to fuel type")


# In[201]:


button35 = st.button("Relation between make and price according to fuel type")

if button35:
    fig = plt.figure(figsize=(20,12))
    sns.swarmplot(data=data,x='make',y='price',hue='fuel-type')
    plt.xticks(rotation=90)
    st.pyplot(fig)
    
    
button36 = st.button("SUMMARY OF RELATION BETWEEN MAKE AND PRICE ACCORDING TO FUEL TYPE")

if button36:
    st.markdown("## 1.Most cars use gas.")
    st.markdown("## 2.Mercedes-Benz uses gas and diesel. And other kinds of cars do that")
    st.markdown("## 3.BMW does not use diesel.")


# In[ ]:





# In[202]:


st.markdown("---")


# In[203]:


st.markdown("### 4.Relation between the type of the car & price according to engine type")


# In[204]:


button38 = st.button("Relation between the type of the car & price according to engine type")

if button38:
    fig = plt.figure(figsize=(12,9))
    sns.swarmplot(data=data,x='make',y='price',hue='engine-type')
    plt.xticks(rotation=90)
    st.pyplot(fig)
    
    

button39 = st.button("SUMMARY OF RELATION BETWEEN THE TYPE OF CAR AND PRICE ACCORDING TO ENGINE TYPE")

if button39:
    st.markdown("## 1.Mercedes-Benz is also different from others. It always works on any kind of one feature.")
    st.markdown("## 2.In this plot, It used many types of an engine like ohc, ohcv. The highest price is ohcv.")
    st.markdown("## 3.BMW works on ohc only.")
    st.markdown("## 4.Always ohcv costs higher and a few use it in their cars like Mercedes-Benz and Nissan.")
    st.markdown("## 5.A cheaper car uses och, and it's common used in all")


# In[205]:


st.markdown("---")


# In[206]:


st.markdown("### 5.Relation between make and engine size according to engine type ")


# In[207]:


button40 = st.button("Relation between make and engine size according to engine type")

if button40:
    fig = plt.figure(figsize=(15,11))
    sns.swarmplot(data=data,x='make',y='engine-size',hue='engine-type')
    plt.xticks(rotation=90)
    st.pyplot(fig)
    
    


# In[208]:


st.markdown("---")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




