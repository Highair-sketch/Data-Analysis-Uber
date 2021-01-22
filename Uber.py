#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# # Load CSV file into memory

# In[4]:


data = pandas.read_csv('./Desktop/uber-raw-data-apr14.csv')


# In[13]:


data.tail()


# ## Convert datetime and add some useful columns

# In[11]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[10]:


data.tail()


# In[12]:


def get_dom(dt):
    return dt.day


data['dom'] = data['Date/Time'].map(get_dom)


# In[53]:


def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)

data.tail()


# In[41]:


## Analysis


# In[42]:


##analyze the Day of Month


# In[15]:


hist(data.dom, bins = 30, rwidth= .8, range = (0.5,30.5))
xlabel('date of the month')
ylabel('frequency')
title('Frequency by Day of Month - Uber - Apr 2014')


# In[16]:


def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date 


# In[17]:


bar(range(1,31), by_date)


# In[19]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[72]:


figure(figsize = (10,10))
bar(range(1,31), by_date_sorted)
xticks(range(1,31),by_date_sorted.index)
xlabel('date of the month')
ylabel('frequency')
title('Frequency by Day of Month - Uber - Apr 2014')
("")


# # analyze the hour

# In[55]:


hist(data.hour, bins = 24, range =(.5,24))
("")


# In[26]:


##analyze the weekday


# In[59]:


hist(data.weekday, bins = 7 , range = (-.5,6.5), rwidth = .8, color= 'g',alpha = .4)
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())
("")


# # # cross analysis(hour, dow)
# # dow = day of week

# In[56]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[57]:


seaborn.heatmap(by_cross)


# # by latitude and longitude

# In[61]:


hist(data['Lat'], bins = 100,range = (40.5,41))
("")


# In[63]:


hist(data['Lon'], bins = 100 , range = (-74.1,-73.9));


# In[66]:


hist(data['Lon'], bins = 100, range = (-74.1,-73.9), color = 'g',alpha = .5, label = 'longitude')
grid()
legend(loc = 'upper left')
twiny()
hist(data['Lat'], bins = 100, range= (40.5,41), color = 'r', alpha = .5, label = 'latitude')
legend(loc = 'best')
("")


# In[71]:


figure(figsize =( 30,30))
plot(data['Lon'],data['Lat'],'.',ms = 1, alpha = .5)
xlim(-74.2,-73.7)
ylim(40.7,41)


# In[ ]:




