#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from location_name_formatter import LocationNameFormatter


# In[2]:


name_formatter = LocationNameFormatter()


# In[3]:


before_format = "Chittagong"
formatted_string = name_formatter.formatter(before_format)
print(formatted_string)


# In[ ]:




