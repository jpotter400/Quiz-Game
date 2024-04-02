#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to my computer quiz!")


# In[2]:


playing = input("Would you like to play my game? ")


# In[19]:


print("Sweet! Let's play!")
score = 0


# In[20]:


answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


# In[21]:


answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


# In[22]:


answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


# In[23]:


answer = input("What does PSU stand for? ")
if answer == "power supply":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


# In[24]:


print("You got " + str(score) + " Questions Correct!")


# In[29]:


print("You scored a " + str((score / 4) * 100) + "%.")



# In[ ]:





# In[ ]:




