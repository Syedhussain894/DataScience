# Name: Syed Hussain
# Title: Crash Reducer Eval

# The DataSet files were too large to submit to github, therefore, 
# it is advised that in order to test the code, download the datasets from the website link before testing


# Import panda, matplot and pandadsql
import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt


# Read files
file = pd.read_csv('Crashes.csv', low_memory=False)
file2 = pd.read_csv('Reducer.csv', low_memory=False)

# Covert borough columns to string
file['BOROUGH'] = file['BOROUGH'].astype(str)
file2['Borough'] = file2['Borough'].astype(str)



# FILE 1 -----------------------

# This File displays all the speed reducers and crashes per boroughs and displays the crash/reducer ratio
# It can be seen that Manhattan has the highest Crash per reducer ratio out of all the boroughs


# Both queries select crash and reducers from each file ordered by borough
file_1_Query = 'SELECT BOROUGH, COUNT(*) AS CrashCount FROM file GROUP BY BOROUGH'
file_1_Query2 = 'SELECT Borough, COUNT(*) AS ReducerCount FROM file2 GROUP BY Borough'
file_1 = psql.sqldf(file_1_Query)
file_12 = psql.sqldf(file_1_Query2)

# Creates seperate column for the data analyzed above
file_1['ReducerCount'] = file_12['ReducerCount']

# calculates ratio
file_1['Crash/Reducer Ratio'] = file_1['CrashCount'] / file_1['ReducerCount']

# write to file
file_1.to_csv('file1.csv', index = False)


# display above data
df = pd.DataFrame({'#Crashes': file_1['CrashCount'],
                   '#Reducers': file_1['ReducerCount'], 'Borough': file_1['BOROUGH']})

df.plot(x="Borough", y=["#Crashes", "#Reducers"], kind="bar", stacked=True)
plt.show()

plt.bar(file_1['BOROUGH'],file_1['Crash/Reducer Ratio'])
plt.xlabel('Borough')
plt.ylabel('Ratio')
plt.show()


# File 1 End -----------------------------



# File 2 Start -----------------------------

# This File displays the number of reducers and crashers per street/ave and displays the Crash / reducer ratio per street in every borough


# Query selects crash and reducers from file1
file_2_Query = 'SELECT BOROUGH, [ON STREET NAME], COUNT([ON STREET NAME]) AS [#Crashes] FROM file GROUP BY [ON STREET NAME]'
file_2 = psql.sqldf(file_2_Query)


# Query creates dataframe from file 2 with all crashes ordered by street
file_2_Query2 = 'SELECT r.Borough, [OnStreet], COUNT(OnStreet) AS [#Reducers] FROM file2 r LEFT JOIN file_2 c WHERE c.[ON STREET NAME] = r.OnStreet GROUP BY OnStreet'
file_22 = psql.sqldf(file_2_Query2)

# query combines both files to create a dataframe with all reducers orderd by street
file_2_Query3 = 'SELECT c.BOROUGH, [ON STREET NAME], COUNT([ON STREET NAME]) AS [#Crashes] FROM file c LEFT JOIN file2 r WHERE r.OnStreet = c.[ON STREET NAME] GROUP BY [ON STREET NAME]'
file_23 = psql.sqldf(file_2_Query3)

file_22['#Crashes'] = file_23['#Crashes']

# calculates ratio
file_22['Crash/Reducer Ratio'] = file_22['#Crashes'] / file_22['#Reducers']

# write to file
file_22.to_csv('file2.csv', index = False)



# plt.bar(file_22['OnStreet'],file_22['Crash/Reducer Ratio'])
# plt.xlabel('Street')
# plt.ylabel('Ratio')
# plt.show()

# File 2 End ---------------------------------



# File 2 Print ---------------------------------------------



# creates a dataframe with borough and crash/reducer ratio to find above avg street collisions
file_2of22 = pd.DataFrame()
file_2of22['Borough'] = file_22['Borough']
file_2of22['Crash/Reducer Ratio'] = file_22['Crash/Reducer Ratio']

# creates a dataframe with borough and crash/reducer ratio to find below avg street collisions
file_3of22 = pd.DataFrame()
file_3of22['Borough'] = file_22['Borough']
file_3of22['Crash/Reducer Ratio'] = file_22['Crash/Reducer Ratio']

# Finds above and below avg collisions per street, respectivily
file_2of22 = file_22.loc[file_22['Crash/Reducer Ratio'] > file_22['Crash/Reducer Ratio'].mean()]
file_3of22 = file_22.loc[file_22['Crash/Reducer Ratio'] < file_22['Crash/Reducer Ratio'].mean()]


# First print statement displays ALL the streets that need more reducers because of above average crash rate
# Second print statement displays ALL the streets that dont need more reducers because of below average crash rate

print("\n\n These are all the street that need more speed Reducers due to an above average rate of car crashes")
print(file_2of22)

print("\n\n These are all the street that have a successfull amount of speed Reducers due to below average rate of car crashes")
print(file_3of22)



# File 2 Print End ---------------------------------------------




# File 3 Start ----------------------------------------

# This File displays the streetName, Lat and Lon of all the reducers that have caused accidents

# Ths query selects all locations exactly, where there are reducers and have crashes in order to see which reducers are successful or unsuccessful
file_3_Query = 'SELECT c.BOROUGH, [ON STREET NAME], LATITUDE, LONGITUDE FROM file c INNER JOIN file2 r WHERE r.FromLatitude = c.LATITUDE AND r.FromLongitude = c.LONGITUDE GROUP BY [ON STREET NAME]'
file_3 = psql.sqldf(file_3_Query)

# write to file
file_3.to_csv('file3.csv', index = False)



# File 3 End ----------------------------------------


