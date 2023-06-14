#Ted Ruigrok van der Werven 1058308

import string
# DO NOT CHANGE THIS FUNCTION
# load_data() reads the input file containing all the given information of books
# The result is collected in the list_of_book_isbn: a list of tuples
input_data_file = 'books_isbn_02.csv'
list_of_book_isbn = []
def load_data():
    try:
        with open(input_data_file , 'r') as books_file_obj:
            files_content = books_file_obj.readlines()
        for item in files_content:
            book_name_isbn = item.split(',')
            book_name, book_isbn = book_name_isbn[0], book_name_isbn[1].removesuffix('\n')
            list_of_book_isbn.append((book_name, book_isbn))
    except:
        print('Exception openning file')
    return files_content
load_data()

# Implement your solution starting from next line

#example input. This short list can substitute for the csv that is imported by the code above:
# [('BookDot1','ISBN .-85375-390-4'),('Book1','ISBN 1-32597-135-9'),('Book2','ISBN 0-04709-135-'),('Book3','ISBN 3-65716-957-1'),('Book4','ISBN 8-54978-631-6'),('Book5','ISBN 8-90889-677-5'),('Book6','ISBN -81176-015-X'),('Book7','ISBN 7-59718-740-8'),('Book8','ISBN 8-6010-193-4'),('Book9','ISBN 5-55962-893-X'),('Book10','ISBN 0-58902-807-X')]
#list_of_book_isbn=[('Book10','ISBN 9-4.092-048-8'),('Book20','ISBN 8-42767-203-9'),('Book03','ISBN 0-06.02-006-1'),('Book04','ISBN 7-68568-296-6'),('Book01','ISBN 1-32597-135-9'),('Book02','ISBN 0-04709-135-'),('Book13','ISBN 3-65716-957-1'),('Book15','ISBN 0-81199-131-8'),('Book19','ISBN 0-24363-745-4'),('Book11','ISBN 5-.3927-749-11'),('Book14','ISBN 8-54978-631-6'),('Book05','ISBN 8-90889-677-5'),('Book16','ISBN -81176-015-X'),('Book17','ISBN 7-59718-740-8'),('Book08','ISBN 8-6010-193-4'),('Book06','ISBN .-96790-789-4'),('Book07','ISBN 2-77421-159-X'),('Book18','ISBN 6-71603-10.-4'),('Book09','ISBN 5-55962-893-X')]
#convert tuple of input current_ISBN_Str numbers to list:
list_of_book_without_tuples = []
for t in list_of_book_isbn:
    for x in t:
        list_of_book_without_tuples.append(x)
#create two new lists, one with book1,book2 ect, and a list with current_ISBN_Str's only:
raw_book_nr_list=list_of_book_without_tuples[::2]
#output: ['book1','book2', ect.]
raw_current_ISBN_Str_list= list_of_book_without_tuples[1::2]
#output: ['current_ISBN_Str 1-32597-135-9', 'current_ISBN_Str 0-04709-135-',ect]
# Cleaning up the ISBN numbers:
#remove 'current_ISBN_Str ' and hyphens from each string in the list:
for i in range(len(raw_current_ISBN_Str_list)):
    raw_current_ISBN_Str_list[i] = raw_current_ISBN_Str_list[i].replace('ISBN ', '')
    raw_current_ISBN_Str_list[i] = raw_current_ISBN_Str_list[i].replace('-', '')    
#Output: ['860101934', '555962893X',ect]
clean_isbn_list = raw_current_ISBN_Str_list

#Entering for-loop for interating through the ISBN number:

#f is iterator for current_book
f=0
#initializing two lists: one for output book1,book2 and other with strings of error description. They will be zipped together later, resulting in final output list
output_A = []
output_B = []

for current_ISBN_Str in clean_isbn_list:
    #iterate through list of books to prepare output list entry:
    current_book = raw_book_nr_list[f]
    f+=1
    #The boolean missingDigits must be initialized first. Not sure why. Maybe it is not a global variable if it is initialized in the if-statement below.
    missingDigits =bool
    checkSumMatches = bool
    #For the special x checksum case, we are going to check the individual current_ISBN_Str string first (input from here: '555962893X'):
    if current_ISBN_Str[-1]=='X' and len(current_ISBN_Str[0:-1])==9:
        gpt= current_ISBN_Str[0:-1]
        specialCaseX = True
        missingDigits = False
        #control number is in this case 10(hence the X)
        cno=10
    elif current_ISBN_Str[-1]=='X' and len(current_ISBN_Str[0:-1])!=9:
        missingDigits = True
        specialCaseX =  True
    # From here is for all standard cases where check digit is not X. get the first 9 digits of current_ISBN_Str to calculate checksum gpt

    elif '.' in current_ISBN_Str:
        #gptp is the string of ISBN digits without control digit at the end (but it has a dot)
        gptp = current_ISBN_Str[:-1]
        #get the control digit:
        if current_ISBN_Str[-1]=='X':
            cno=10
            specialCaseX=True
        else:
            cno = int(current_ISBN_Str[-1])
            specialCaseX=False
        #get index of the dot:
        DotIndex=current_ISBN_Str.index('.')
        #get the multiplication factor corresponding to that DotIndex:
        if DotIndex==0:
            MisDigfactor=10
        if DotIndex==1:
            MisDigfactor=9
        if DotIndex==2:
            MisDigfactor=8
        if DotIndex==3:
            MisDigfactor=7
        if DotIndex==4:
            MisDigfactor=6
        if DotIndex==5:
            MisDigfactor=5
        if DotIndex==6:
            MisDigfactor=4
        if DotIndex==7:
            MisDigfactor=3
        if DotIndex==8:
            MisDigfactor=2
        #now we need the test sum, according to formula gpt[0]*10+...gpt[9]*2, except we are going to skip the step of the DotIndex:
        i=0
        j=10
        partial_sum = 0
        for i in range(0,9):
            if i==DotIndex:
                j-=1
                i+=1
            else:
                partial_sum = partial_sum+int(gptp[i])*j
                j-=1
                i+=1
        MissDig=0
        while MissDig<=9:
            test_sum=MisDigfactor*MissDig+partial_sum
            DotCaseRemainder=test_sum%11
            if 11-DotCaseRemainder==cno:
                MissDigStr=str(MissDig)
                current_ISBN_Str=current_ISBN_Str.replace('.',MissDigStr)
                missingDigits=False
                gpt=int(current_ISBN_Str)
                break
            else:
                MissDig+=1
                

    else:# From here is for all standard cases where check digit is not X. get the first 9 digits of current_ISBN_Str to calculate checksum gpt
        specialCaseX = False
        gpt = current_ISBN_Str[:-1]
        #check for missing digits. gpt needs to be 9 digits long. I also add an OR to check if entire current_ISBN_Str has cardinality of 11:
        if len(gpt)!=9 or len(current_ISBN_Str)!=10:
            missingDigits = True
        else:
            missingDigits = False        


    #From here on, only continuing for cases where there are no missing digits. In this if-statement, verifying if the checksum matches:
    if missingDigits == False:
        gpt = current_ISBN_Str[:-1]
        #Assuming no digits are missing fromcurrent_ISBN_Str. calculating sum of 9 digits
        #according to formula gpt[0]*10+...gpt[9]*2. Adding variables i and j so that the formula is
        #represented by gpt[i]*j
        i=0
        j=10
        sum = 0
        for i in range(0,9):
            sum = sum+int(gpt[i])*j
            j-=1
            i+=1
        #get control number from current_ISBN_Str string (last digit):
        if specialCaseX == False:
            cno = int(current_ISBN_Str[-1])
        #perform checksum calculation:
        remainder = sum%11
        if 11-remainder==cno:
            checkSumMatches=True
        else:
            checkSumMatches=False

    elif missingDigits:
        output_A.append(current_book)
        output_B.append('Missing Digits')
#output_A: ['Book1', 'Book3', 'Book4']
#output_B: ['Wrong Check Number', 'Missing Digits', 'Missing Digits']
    if checkSumMatches == False:
        output_A.append(current_book)
        output_B.append('Wrong Check Number')

#zip the lists above together into final output_list:
output_list = list(zip(output_A,output_B))
#output: [('Book1', 'Wrong Check Number'), ('Book3', 'Missing Digits'), ('Book4', 'Missing Digits')]
print(output_list)

print()