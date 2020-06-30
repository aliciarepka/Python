#!/usr/bin/env python
# coding: utf-8

# # **Python Training Exercises/HW Problems**

# ## Problem 1
# ### You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# In[21]:


def case_swap(string):
    
    return string.swapcase()


# In[22]:


'''
Don't modify this cell at all!! This cell is for you to run and check if your answer to Problem 1 is correct
'''
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def testProblem1():
    assert case_swap(ascii_lowercase) == ascii_uppercase, "Your function is returning the incorrect output"
    assert case_swap(ascii_uppercase) == ascii_lowercase, "Your function is returning the incorrect output"
    assert case_swap('aBcDeF') == 'AbCdEf', "Your function is returning the incorrect output"
    assert case_swap('hey guys!') == 'HEY GUYS!', "Your function is returning the incorrect output"
    assert case_swap('STEM-AWAY') == 'stem-away', "Your function is returning the incorrect output"
    assert case_swap(digits) == digits, "Your function is returning the incorrect output"
    assert case_swap(punctuation) == punctuation, "Your function is returning the incorrect output"
    
    print('Your function has passed all of the tests!')

testProblem1()


# ## Problem 2
# ### Return the number of even integers in the given array.

# In[11]:


def even_ints(nums):
    evens = 0
    for x in range(0, len(nums)):
        if(nums[x] % 2 is 0):
            evens += 1  
    return evens


# In[12]:


'''
Don't modify this cell at all!! This cell is for you to run and check if your answer to Problem 2 is correct
'''
def testProblem2():
    assert even_ints([2, 1, 2, 3, 4]) == 3, "Your function is returning the incorrect output"
    assert even_ints([2, 2, 0]) == 3, "Your function is returning the incorrect output"
    assert even_ints([1, 3, 5]) == 0, "Your function is returning the incorrect output"
    assert even_ints([]) == 0, "Your function is returning the incorrect output"
    assert even_ints([11, 9, 0, 1]) == 1, "Your function is returning the incorrect output"
    assert even_ints([2, 11, 9, 0]) == 2, "Your function is returning the incorrect output"
    assert even_ints([2]) == 1, "Your function is returning the incorrect output"
    assert even_ints([2, 5, 12]) == 2, "Your function is returning the incorrect output"
    
    print('Your function has passed all of the tests!')

testProblem2()


# ## Problem 3
# ### Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# In[19]:


def two_neighbors(nums):
    neighbors = False
    for i in range(0, (len(nums)-1)):
        if((nums[i] == 2) and (nums[i+1] == 2)):
            neighbors = True   
    return neighbors


# In[20]:


'''
Don't modify this cell at all!! This cell is for you to run and check if your answer to Problem 3 is correct
'''
def testProblem3():
    assert two_neighbors([1, 2, 2]) == True, "Your function is returning the incorrect output"
    assert two_neighbors([2, 0, 2]) == False, "Your function is returning the incorrect output"
    assert two_neighbors([4, 5, 6]) == False, "Your function is returning the incorrect output"
    assert two_neighbors([2, 2, 2]) == True, "Your function is returning the incorrect output"
    
    print('Your function has passed all of the tests!')
    
testProblem3()


# ## Problem 4
# ### Write a function in Python that implements the following logic: The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an integer *temperature* and a Boolean *isSummer*, return *True* if the squirrels play and *False* otherwise.

# In[30]:


def squirrelPlay(temperature, isSummer):
    play = False
    
    if((isSummer == False) and (temperature <= 90) and (temperature >= 60)):
        play = True
    if((isSummer == True) and (temperature <= 100) and (temperature >= 60)):
        play = True
    
    return play


# In[31]:


'''
Don't modify this cell at all!! This cell is for you to run and check if your answer to Problem 4 is correct
'''
def testProblem4():
    assert squirrelPlay(70, False) == True, "Your function is returning the incorrect output"
    assert squirrelPlay(95, False) == False, "Your function is returning the incorrect output"
    assert squirrelPlay(95, True) == True, "Your function is returning the incorrect output"
    assert squirrelPlay(90, False) == True, "Your function is returning the incorrect output"
    assert squirrelPlay(90, True) == True, "Your function is returning the incorrect output"
    assert squirrelPlay(50, False) == False, "Your function is returning the incorrect output"
    assert squirrelPlay(50, True) == False, "Your function is returning the incorrect output"
    assert squirrelPlay(100, False) == False, "Your function is returning the incorrect output"
    assert squirrelPlay(100, True) == True, "Your function is returning the incorrect output"
    assert squirrelPlay(105, True) == False, "Your function is returning the incorrect output"
    assert squirrelPlay(59, False) == False, "Your function is returning the incorrect output"
    assert squirrelPlay(59, True) == False, "Your function is returning the incorrect output"
    assert squirrelPlay(60, False) == True, "Your function is returning the incorrect output"

    
    print('Your function has passed all of the tests!')
    
testProblem4()


# ## Problem 5
# ### Given a string, consider the prefix string made of the first *N* chars of the string. Does that prefix string appear somewhere else in the string? Assume that the string is not empty and that *N* is in the range *1..str.length()*.

# In[35]:


def prefixAgain(str, n):
    if(str[0:n] in str[n:]):
        return True
    return False


# In[36]:


'''
Don't modify this cell at all!! This cell is for you to run and check if your answer to Problem 5 is correct
'''
def testProblem5():
    assert prefixAgain("abXYabc", 1) == True, "Your function is returning the incorrect output"
    assert prefixAgain("abXYabc", 2)  == True, "Your function is returning the incorrect output"
    assert prefixAgain("abXYabc", 3) == False, "Your function is returning the incorrect output"
    assert prefixAgain("xyzxyxyxy", 2) == True, "Your function is returning the incorrect output"
    assert prefixAgain("xyzxyxyxy", 3) == False, "Your function is returning the incorrect output"
    assert prefixAgain("Hi12345Hi6789Hi10", 1) == True, "Your function is returning the incorrect output"
    assert prefixAgain("Hi12345Hi6789Hi10", 2) == True, "Your function is returning the incorrect output"
    assert prefixAgain("Hi12345Hi6789Hi10", 4) == False, "Your function is returning the incorrect output"
    assert prefixAgain("Hi12345Hi6789Hi10", 3) == True, "Your function is returning the incorrect output"
    assert prefixAgain("a", 1) == False, "Your function is returning the incorrect output"
    assert prefixAgain("aa", 1) == True, "Your function is returning the incorrect output"
    assert prefixAgain("ab", 1) == False, "Your function is returning the incorrect output"

    
    print('Your function has passed all of the tests!')
    
testProblem5()


# ## Problem 6
# 1. Download the CSV file from the following website: https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data.
# 2. Create a Pandas Dataframe of the dataset and display the first 10 rows of the Pandas Dataframe.
# 3. Filter through the dataset and clean it.
# 4. Create a Pandas Dataframe of the dataset after cleaning it and display the first 10 rows of the Pandas Dataframe.
# 5. Use ***seaborn*** and plot *2* different graphs using the preprocessed dataset.

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read file
nyc = pd.read_csv("AB_NYC_2019.csv")
# Create dataframe
nyc_df = pd.DataFrame(nyc)

# Clean
# Get rid of nas
nyc_df.dropna()
# Start indexing at 1
nyc_df.index += 1

# First 10 rows
nyc_df.head(10)
plt.show()

# Plots
sns.barplot(x = "room_type", y = "price", data = nyc_df)
plt.show()
sns.stripplot( x = "price", y = "neighbourhood_group", data = nyc_df)
plt.show()


# ## Problem 7
# 1. Choose a dataset of your choice from the following website: https://corgis-edu.github.io/corgis/json/.
# 2. Create a Pandas Dataframe of your preferred dataset in JSON format using the dataset's link (don't download the dataset) and display the first 10 rows of the Pandas Dataframe.
# 3. Use ***matplotlib*** and plot *5* different graphs.

# In[62]:


import requests
import pandas as pd
import json

energy_dict = pd.read_json('https://corgis-edu.github.io/corgis/datasets/json/energy/energy.json')
energy_df = pd.DataFrame(energy)
energy_df.head(10)

plot_dict = {}

for data in energy_dict:
    if energy_dict['State'] not in plot_dict:
        plot_dict[data['State']] = []
        plot_dict[data['State']].append(data['Consumption'])

#plt.bar(x = energy["State"], height = energy["Consumption"])


# ## Problem 8
# ### You are given a positive integer *N*.
# ### Your task is to print a palindromic triangle of size *N*.
# ### 
# ### For example, a palindromic triangle of size *5* is:
# ### 
# ## 1
# ## 121
# ## 12321
# ## 1234321
# ## 123454321
# ### 
# ### Note: You can't use string-related functions and you can only use one for-loop

# In[35]:


def pal_tri(n):
    nums = []
    backnums = []
    for x in range(1, n+1):
        backnums = nums[0:x]
        backnums.reverse()
        nums.append(x)
        print(nums, backnums)
    return
pal_tri(5)


# ## Problem 9
# ### Given two lists. Create a third list by picking an odd-index element from the first list and even index elements from second.

# In[25]:


def list_3(list_1, list_2):
    list_3 = []
    for x in range(0, len(list_1)):
        if (x % 2 is 0):
            list_3.append(list_1[x])
    for y in range(0, len(list_2)):
        if((y + 1) % 2 is 0):
            list_3.append(list_2[y])
            
    return list_3


# ## Problem 10
# ### Given a list, count the occurrence of each element and create a dictionary to show the count of each element.

# In[47]:


def list_to_dict(l):
    dictionary = {}
    for x in range(0, len(l)):
        if l[x] not in dictionary:
            dictionary[l[x]] = 0
        dictionary[l[x]] += 1   
    
    return dictionary

list_to_dict([2, 4, "Hi", "Hi", "Hi", "hi", 4])


# ## Problem 11
# ### Given two lists, convert them into a dictionary. The first list will represent the "keys", and the second list will represent the "values"

# In[45]:


def dict_maker(keys, values):
    if len(keys) == len(values):
        new_dict = {}
        for x in range(0, len(keys)):
            new_dict.update({keys[x]: values[x]})
    return new_dict

print(dict_maker(["A", "B", "C", "D"], [1, 32, 5, 7]))


# ## Problem 12
# ### Merge 2 dictionaries into 1 dictionary

# In[56]:


def dict_merger(d1, d2):
    d1.update(d2)
    return d1


# ## Problem 13
# ### Using *numpy*, create a 4 by 2 integer array and print its attributes (the shape of the array and the array dimensions)

# In[55]:


import numpy as np

array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print("Shape:", array.shape)
print("Number of Dimensions:", array.ndim)
print("Size:", array.itemsize)


# # Problem 14 - Problem 25

# ## Problem 14
# #### Create a Pandas Dataframe using the CSV file provided at this link: https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv
# #### Also, display the first 20 rows of the dataframe
# #### Note: Don't download the CSV File, and you can use either *matplotlib* or *seaborn* for these problems

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sales = pd.read_csv("https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv")
sales_df = pd.DataFrame(sales)
sales_df[0:20]


# ## Problem 15
# ### Using a line plot, plot the Month (x-axis) against the Total Profit (y-axis)

# In[67]:


plt.scatter("month_number", "total_profit", data = sales_df)
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()


# ## Problem 16
# ### Using a line plot, plot the Month (x-axis) against the Total Profit (y-axis) with the following style properties:
# * Dotted Red Line
# * The width of the line graph should be 3
# * Legend should be placed at the bottom right section of the graph
# * Add a label for the x-axis
# * Add a label for the y-axis
# * Add a title
# * Add a yellow circular marker at each point on the graph

# In[36]:


plt.plot("month_number", "total_profit", data = sales_df, 
         color = 'red', linestyle = "--", linewidth = 3, 
         marker = "o", markerfacecolor = "yellow")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit vs. Month")
plt.legend(loc = "lower right")
plt.show()


# ## Problem 17
# ### Display the number of units sold per month for each product using multiline plots (must be on the same figure). Make sure that the plot for each product is a different color, and add a legend, title, and axis labels to the graph as well.

# In[37]:


# Make a seperate plot for each product, each with a different color
plt.plot("month_number", "facecream", data = sales_df, 
         color = "red")
plt.plot("month_number", "facewash", data = sales_df, 
         color = "orange")
plt.plot("month_number", "toothpaste", data = sales_df, 
         color = "yellow")
plt.plot("month_number", "bathingsoap", data = sales_df, 
         color = "green")
plt.plot("month_number", "shampoo", data = sales_df, 
         color = "blue")
plt.plot("month_number", "moisturizer", data = sales_df, 
         color = "purple")
# Add a legend in the upper left corner
plt.legend(loc = "upper left")
# Title and labels
plt.title("Units Sold per Month by Product")
plt.xlabel("Month")
plt.ylabel("Units Sold")
# Show all of the plots 
#(Facewash cannot be seen because the sales are equal to moisturizer, which is on top and darker)
plt.show()


# ## Problem 18
# ### Plot the toothpaste sales data of each month using a scatter plot. Also, add a grid on the plot, the gridline style should be "-".

# In[42]:


# Scatterplot
plt.scatter(x = "month_number", y = "toothpaste", data = sales_df)
plt.grid(color = "gray", linestyle = "-")


# ## Problem 19
# ### Plot the product sales data of face cream and facewash using a bar chart on the same plot.

# In[3]:


plt.bar(x = "Facecream", height = sales_df["facecream"], color = "red")
plt.bar(x = "Facewash", height = sales_df["facewash"], color = "blue")
plt.show()


# ## Problem 20
# ### Plot the total profit of each month using a histogram

# In[5]:


plt.hist(sales_df["total_profit"])
plt.title("Total Profit")


# ## Problem 21
# ### Calculate the total sales data for last year for each product and show it using a pie chart. Make sure that the percentage of each slice on the pie chart is visible on the chart itself, and add a legend as well.

# In[34]:


# Calculate total yearly sales for each product
total_facewash = sum(sales_df["facewash"])
total_facecream = sum(sales_df["facecream"])
total_toothpaste = sum(sales_df["toothpaste"])
total_bathingsoap = sum(sales_df["bathingsoap"])
total_shampoo = sum(sales_df["shampoo"])
total_moisturizer = sum(sales_df["moisturizer"])
# Array for totals
totals = [total_facewash, total_facecream, total_toothpaste, total_bathingsoap, total_shampoo, total_moisturizer]

# Array for labels
labs = ["Facewash", "Facecream", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"]

# Make plot
plt.pie(totals, labels = labs, autopct = "%1.1f%%", radius = 3)
plt.legend(loc = "upper left")


# ## Problem 22
# ### Plot all of the product sales data using a stack plot.

# In[16]:


plt.stackplot(sales_df["month_number"], 
              sales_df["facecream"], 
              sales_df["facewash"],
              sales_df["toothpaste"],
              sales_df["bathingsoap"],
              sales_df["shampoo"],
              sales_df["moisturizer"],
              sales_df["total_units"],
              sales_df["total_profit"])

