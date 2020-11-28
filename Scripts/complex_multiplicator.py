# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:54:09 2020

@author: andre
"""

#A program to calculate the algebra of the PMNS formalism

#This will be useful for grouping up powers at the end
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches







#we first define our terms and operations

Parameters = ["c23","c13","c12","s23","s13","s12"]
Complex_phase = "e^i"


#we multiply simple terms (no sums in them)
def multiply_mono(a,b):
    
    string1 = a
    string2 = b
    C1 = string1.find(Complex_phase)
    C2 = string2.find(Complex_phase)

    if C1 != -1 and C2 != -1:
        val1 = int(string1[C1+3:C1+5])
        val2 = int(string2[C2+3:C2+5])
        complex_total = val1 + val2
        string1 = string1[:C1]+string1[C1+5:]
        
        if complex_total == 0:
            string2 = string2[:C2]+string2[C2+5:]
            
        elif complex_total > 0:
            string2 = string2[:C2+3] + "+" + str(complex_total) + string2[C2+5:]

        else:
            string2 = string2[:C2+3] + str(complex_total) + string2[C2+5:]
    
    sign1 = string1[0]
    sign2 = string2[0]
    
    if sign1 == sign2:
        string1 = "+" + string1[1:]
        string2 = string2[1:]
        
    else:
        string1 = "-" + string1[1:]
        string2 = string2[1:]        
        

    return(string1 + string2)


#multiply compound terms (with sums in them)
def multiply_composite(a,b):
    list1 = a
    list2 = b
    product = []
    for term1 in list1:
        for term2 in list2:
            product.append(multiply_mono(term1,term2))

    return(product)            
        

#elevate things to powers if needed    
def compress(lst):
    global Parameters
    ret = []
    
    for a in lst:
        my_str = a
        for item in Parameters:
            instances = sorted(list(find_all(my_str,item)),reverse=True)
            power = len(instances)
            if power <= 1:
                continue
            else:
                for i in instances:
                    my_str = my_str[:i] + my_str[i+3:]
                my_str =  my_str[0] + item + "^(" + str(power) +")" + my_str[1:]
        ret.append(my_str)
    return(ret)


#conjugate an index of the PMNS matrix
def conjugate(lst):
    ret = []
    for a in lst:
        my_str = a
        C1 = my_str.find(Complex_phase)
        if C1 != -1:
            val1 = int(my_str[C1+3:C1+5])
            val1 = -1*val1
            
            if val1 < 0:
                my_str = my_str[:C1+3] + str(val1) + my_str[C1+5:]
            else:
                my_str = my_str[:C1+3] + "+" + str(val1) + my_str[C1+5:]
    
        ret.append(my_str)
    return(ret)


#reorder an index of the PMNS matrix according to our list above
def reorder(lst):
    global Parameters
    ret = []
    for a in lst:
        my_str = a
        count = 0
        for item in Parameters:
            instances = sorted(list(find_all(my_str,item)),reverse=True)
            for index in instances:
                my_str = my_str[3*count:index] + my_str[index+3:] + item

        ret.append(my_str)
    return(ret)



#collapse sum of conjugates
def collapse_conjugates(lst):
    ret = lst
    dels=[]

    for i in range(len(lst)):
        for j in range(len(lst)):
            a = lst[i]
            b = lst[j]
            if i > j:
                C1 = a.find(Complex_phase)
                C2 = b.find(Complex_phase)
                if C1 == C2 and C1 != -1 and int(a[C1+3:C1+5]) == -int(b[C2+3:C2+5]):
                    if a[:C1+3] + a[C1+5:] == b[:C2+3] + b[C2+5:]:
                        double = a[0] + "2"+ a[1:C1] + a[C1+5:] + "_COS" + a[C1+4:C1+5] + "d"
                        dels.append(i)
                        dels.append(j)
                        ret.append(double)
    for i in sorted(dels,reverse=True):
        del ret[i]                    
    return(ret)



#group additives
def collapse_similar(lst):
    ret = lst
    dels=[]

    for i in range(len(lst)):
        for j in range(len(lst)):
            a = lst[i]
            b = lst[j]
            if i > j:
                if a == b:
                    double = a[0] + "2" + a[1:]
                    dels.append(i)
                    dels.append(j)
                    ret.append(double)
                elif a[1:] == b[1:]:
                    dels.append(i)
                    dels.append(j)
                    
    for i in sorted(dels,reverse=True):
        del ret[i]                    
    return(ret)

a = ["-c12s13s23e^i+1","+c23s12"]
b = ["-e^i-1"]
c = "-c12s13s23c12s23s23e^i+1"

#print(reorder(a))
#print(compress(reorder(multiply_composite(a,conjugate(a)))))
#print(conjugate(a))


