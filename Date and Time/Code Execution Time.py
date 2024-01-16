# Program that deals with code execution time using date time module

# Importing modules
import datetime

# Start time
start_time = datetime.datetime.now()
# Loop iteration used for calculation
for i in range(0, 100000000):
    pass
# End time
end_time = datetime.datetime.now()

duration = end_time - start_time
print('Execution Time: ', duration)

