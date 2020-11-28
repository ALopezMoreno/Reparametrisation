# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:43:42 2020

@author: andre
"""

#We find expressions for the transition probabilities P_mumu and P_mue
#in terms of various parametrisations, using the complex_multiplicator
import complex_multiplicator as cpx




U_ABC = [ [         ["+c13c12"]             ,           ["+c13s12"]             ,           ["+s13e^i-1"]        ],
         
          [["-c12s13s23e^i+1","-c23s12"]    ,   ["-s12s13s23e^i+1","+c23s12"]   ,           ["+s23c13"]           ],
          
          [["-c12c23s13e^i+1","+s12s23"]    ,   ["-s12c23s13e^i+1","-c12s23"]   ,           ["+c23c13"]           ]  ]
          



U_BCA = [ [         ["+c13c12"]             ,   ["+c23c13s12","-s23s13e^i-1"]   ,   ["+s23c13s12","+c23s13e^i-1"] ],
         
          [         ["-s12"]                ,            ["+c12c23"]            ,           ["+c12s23"]           ],
          
          [         ["fill"]                ,             ["fill"]              ,              ["fill"]           ]  ]



U_ACB = [ [         ["+c13c12"]             ,             ["+s12"]               ,         ["+c12c13e^i-1"]       ],
         
          [["-c23s12c13","-s13s23e^i+1"]    ,            ["+c12c23"]            ,  ["+c13s23","-c23s12s13e^i-1"]  ],
          
          [         ["fill"]                ,             ["fill"]              ,              ["fill"]           ]  ]


#P_mue(IJK) = 1-4(T1*SM21 + T2*SM31 + T3*SM32)
#We calculate T1, T2, T3 as we know the expressions for SMij


T1a = cpx.multiply_composite(cpx.conjugate(U_BCA[1][1]) , U_BCA[0][1])
T1a = cpx.reorder(T1a)
T1a = cpx.collapse_conjugates(T1a)
T1a = cpx.collapse_similar(T1a)

T1b = cpx.multiply_composite(U_BCA[1][0] , cpx.conjugate(U_BCA[0][0]))
T1b = cpx.reorder(T1b)
T1b = cpx.collapse_conjugates(T1b)
T1b = cpx.collapse_similar(T1b)

T1 = cpx.multiply_composite(T1a,T1b)
T1 = cpx.reorder(T1)
T1 = cpx.collapse_conjugates(T1)
T1 = cpx.collapse_similar(T1)
T1 = cpx.compress(T1)


T2a = cpx.multiply_composite(cpx.conjugate(U_BCA[1][2]) , U_BCA[0][2])
T2a = cpx.reorder(T2a)
T2a = cpx.collapse_conjugates(T2a)
T2a = cpx.collapse_similar(T2a)

T2b = cpx.multiply_composite(U_BCA[1][0] , cpx.conjugate(U_BCA[0][0]))
T2b = cpx.reorder(T2b)
T2b = cpx.collapse_conjugates(T2b)
T2b = cpx.collapse_similar(T2b)

T2 = cpx.multiply_composite(T2a,T2b)
T2 = cpx.reorder(T2)
T2 = cpx.collapse_conjugates(T2)
T2 = cpx.collapse_similar(T2)
T2 = cpx.compress(T2)


T3a = cpx.multiply_composite(cpx.conjugate(U_BCA[1][2]) , U_BCA[0][2])
T3a = cpx.reorder(T3a)
T3a = cpx.collapse_conjugates(T3a)
T3a = cpx.collapse_similar(T3a)

T3b = cpx.multiply_composite(U_BCA[1][1] , cpx.conjugate(U_BCA[0][1]))
T3b = cpx.reorder(T3b)
T3b = cpx.collapse_conjugates(T3b)
T3b = cpx.collapse_similar(T3b)

T3 = cpx.multiply_composite(T3a,T3b)
T3 = cpx.reorder(T3)
T3 = cpx.collapse_conjugates(T3)
T3 = cpx.collapse_similar(T3)
T3 = cpx.compress(T3)



print("T1 = ")
print(T1)

print("T2 = ")
print(T2)

print("T3 = ")
print(T3)
