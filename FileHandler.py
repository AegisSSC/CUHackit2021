import datetime
import os

# This function reads a file and creats a map to compare the values. 
# if the file can't be opened it exits 
# It will then read the date_time. 
#It will parse over the file, pulling out whats needed and creating a dictionary and returning it 
def Read_from_File(output):
    try: 
        f = open(output,'r')
    except:
        print("File does not exist exiting")
        exit()
    # Date Time will hold the Date and the time and File_dict will be filled with the tings
    Date_time = f.readline() 
    File_dict = {} 
    for line in f: 
        numbers = []
        title = ""
        split = line.split(",",1)
        # File_dict[split[0]] = split[1]
        title = ''.join(c for c in split[0] if c.isalnum())
        for word in split[1].split(): 
            if '[' in word:
                word = ''.join([c for c in word if c in '1234567890.'])
                numbers.append(word)
            else:
                word = ''.join([c for c in word if c in '1234567890.'])
                numbers.append(word)
        File_dict[title] = numbers
    #Perform the conversion: If has brackets. Remove and make int. if not make float. 

    f.close()
    return File_dict

# Add the current date and time as line 1 to the top of date. 
# Write would function in the same way WAHOOOOO 

#This function will take in a dicitonary that conatined the audio data from a playlist 
#It will then write try to open the output file for writing. If it does not it exist it will create it 
# It will then write the current date and time of the call 
# It then writes the information to the file. 
def Write_to_file(Database_Information,output):
        try:
            f = open(output,'a')
        except:
            f = open(output,'x')
        #If the file is empty 
        if os.stat(output).st_size == 0:
            f.write(str(datetime.datetime.now()) + '\n')
        for item in Database_Information.items():
            f.write(str(item) + '\n')
        f.close()