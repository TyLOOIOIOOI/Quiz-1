''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv

Grade = open ("students.csv", "r")

outfile = open ("processedStudents.csv", "w")

Grade_file = csv.reader(Grade, delimiter= ',')

outfile.close()

# create a file object to open the file in read mode
##def main(): 
    #studentgrade = open('students.csv', 'r')

    #file_contents = studentgrade.read()
    #print(file_contents)

#main()


# create a csv object from the file object


#skip the header row


#create an outfile object for the pocessed record



#create a new dictionary named 'student_dict'

student_dict = []

Key= student_dict["stud_id"]
Value= student_dict[gpa]


#use a loop to iterate through each row of the file

    #check if the GPA is below 3.0. If so, write the record to the outfile

for stud_id <= 3:


    
for key,value in student_dict():
    print(key)
    print(value)



    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    





#print the entire dictionary


#Print the student id 
print(stud_id)

#print out the corresponding GPA from the dictionary



#close the outfile
outfile.close()








