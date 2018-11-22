
# coding: utf-8

# In[1]:


from selenium import webdriver
import os
import json
import io


# In[3]:


#define common variables
data_path='./Data/'
data_files=os.listdir(data_path)

data_files

with io.open(data_path+data_files[2],'r',encoding='utf-8-sig') as file1:
    x=json.load(file1)

keys=list(x.keys())

temp=x[keys[4]]


# In[4]:


file_keys={}
browser=webdriver.PhantomJS()


# In[5]:


def save_screenshots(file_n,x):
    browser.get(x)
    browser.save_screenshot('data/{0}.png'.format(file_n))


# In[ ]:


if __name__=='__main__':
    for i,j in enumerate(temp):
        if i>=1164:
            save_screenshots(i,j['href'])
            file_keys[i]=j['href']
            print('{0} saved'.format(i))
    browser.quit()
    with open('data_run.json', 'w') as fp:
        json.dump(file_keys, fp)
    print('json saved')