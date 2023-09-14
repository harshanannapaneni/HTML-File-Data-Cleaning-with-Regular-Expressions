# Importing regular expression module using import keyword
import re
import time as t

# Recording start time
start_time = t.time()

# Creating a file pointer and getting the raw data using the file_ptr and closing the file

file_ptr = open("index.html","r")
raw_data= file_ptr.read()
file_ptr.close()

# Defining the pattern we are trying to search for and removing them using sub method of regex and by making flag as multiline to remove all the occurances.

pattern = "^\d+\)"
filtered_data = re.sub(pattern,'',raw_data,flags=re.MULTILINE)
print(filtered_data)

# Making the filter_data back into the html file
file_ptr = open("index_1.html",'w')
file_ptr.write(filtered_data)
file_ptr.close()

# Calculating total execution time of program
execution_time = t.time()-start_time  

print(execution_time)