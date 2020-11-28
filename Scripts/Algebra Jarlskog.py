# -*- coding: utf-8 -*-



import complex_multiplicator as cpx




U_ABC = [ [         ["+c13c12"]             ,           ["+c13s12"]             ,           ["+s13e^i-1"]        ],
         
          [["-c12s13s23e^i+1","-c23s12"]    ,   ["-s12s13s23e^i+1","+c23s12"]   ,           ["+s23c13"]           ],
          
          [["-c12c23s13e^i+1","+s12s23"]    ,   ["-s12c23s13e^i+1","-c12s23"]   ,           ["+c23c13"]           ]  ]

U_ACB = [ [         ["+c13c12"]             ,             ["+s12"]               ,         ["+c12c13e^i-1"]       ],
         
          [["-c23s12c13","-s13s23e^i+1"]    ,            ["+c12c23"]            ,  ["+c13s23","-c23s12s13e^i-1"]  ],
          
          [         ["fill"]                ,             ["fill"]              ,              ["fill"]           ]  ]
U_BCA = [ [         ["+c13c12"]             ,   ["+c23c13s12","-s23s13e^i-1"]   ,   ["+s23c13s12","+c23s13e^i-1"] ],
         
          [         ["-s12"]                ,            ["+c12c23"]            ,           ["+c12s23"]           ],
          
          [         ["fill"]                ,             ["fill"]              ,              ["fill"]           ]  ]

Ja = cpx.multiply_composite(U_BCA[0][0] , cpx.conjugate(U_BCA[1][0]))
Ja = cpx.reorder(Ja)
Ja = cpx.collapse_conjugates(Ja)
Ja = cpx.collapse_similar(Ja)

Jb = cpx.multiply_composite(cpx.conjugate(U_BCA[0][1]) , U_BCA[1][1])
Jb = cpx.reorder(Jb)
Jb = cpx.collapse_conjugates(Jb)
Jb = cpx.collapse_similar(Jb)


J = cpx.multiply_composite(Ja,Jb)
J = cpx.reorder(J)
J = cpx.collapse_conjugates(J)
J = cpx.collapse_similar(J)
J = cpx.compress(J)

print(J)