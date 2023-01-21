import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'a+') as file:
        timestamp = os.path.getatime(filename)

        # Convert the timestamp into readable format, then into a string
        time = datetime.datetime.fromtimestamp(timestamp)
        time = str(time)

        # Return just the date portion
        # Hint: how many charcters are in "yyyy-mm-dd"?

        return("{:.10s}".format(time))

print(file_date("newfile.txt"))