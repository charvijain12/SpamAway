#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[32]:


#Loading the data
df = pd.read_csv("mail_data.csv")

#Replacing NULL values with NULL string
df1 = df.where( (pd.notnull(df) ),'')


# In[33]:


df1.head()


# In[34]:


df1.shape


# In[35]:


#Coding the Ham mails to False and Spam mails to True
df1.loc[df1['Category'] == 'spam', 'Category'] = 1
df1.loc[df1['Category'] == 'ham', 'Category'] = 0


# In[36]:


df1.head()


# In[37]:


x = df1['Message']
y = df1['Category']


# In[38]:


#Train and Test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)


# In[39]:


print(x.shape, x_train.shape, x_test.shape)


# In[40]:


print(y_train)


# In[41]:


#Transforming text to readable data for Logistic Regression Model
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase='True')

x_train_features = feature_extraction.fit_transform(x_train)
x_test_features = feature_extraction.transform(x_test)

y_train = y_train.astype('int')
y_test = y_test.astype('int')


# In[42]:


print(x_train_features)


# In[43]:


lr = LogisticRegression()


# In[44]:


lr.fit(x_train_features, y_train)


# In[45]:


prediction_training = lr.predict(x_train_features)
accuracy_training = accuracy_score(y_train, prediction_training)


# In[46]:


print("Accuracy of the model on training data = ",accuracy_training)


# In[47]:


prediction_test = lr.predict(x_test_features)
accuracy_test = accuracy_score(y_test, prediction_test)


# In[48]:


print("Accuracy of the model on test data = ",accuracy_test)


# In[52]:


mail_check = [" 07732584351 - Rodger Burns - MSG = We tried to call you re your reply to our sms for a free nokia mobile + free camcorder. Please call now 08000930705 for delivery tomorrow "]
mail_check_features = feature_extraction.transform(mail_check)

predict_mail = lr.predict(mail_check_features)


# In[53]:


if (predict_mail[0] == 1):
    print("Spam mail (True)")
else:
    print("Ham Mail (False)")

