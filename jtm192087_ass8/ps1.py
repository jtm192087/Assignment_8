#!/usr/bin/python3
#program for adding parity bit and parity check	
        

data=input("please enter a binary string\n")
print (len(data))
count=0
for i in range(len(data)):                  #counting no. of one's in the string
    if (data[i] == '1'):
        count+=1


print("count is:",count)
if count%2 == 0:                                         #to add parity bit at the end of the binary data if no. one,s is even
	data=data+'1'
	print("The parity corrected data is:  ",data)      #print corrected  data
else:
	data=data+'0'
	print("The parity corrected data is:  ",data)

string2=data.replace("010","0100")                      #replacing the '010' substring by '0100'
print("The bit stuffing data is:   ",string2)

list = "0101"
string3 = string2 + list
print ("Transmitted data : ",string3)                #adding 0101 at the end