# rows =5 
# for i in range (1,rows+1):
#     res=""    
#     for spc in range(1,rows-i+1):
#         res+=" "
#     for j in range(i):
#         res+="*"+" "
#     print(res)        
# row=5
# for i in range (rows,0,-1):
#     res=""  
#     for space in range (1,rows-i+1):
#        res+=" "
#     for j in range (i):
#        res+="*"+ " "
#     print(res)       


# rows =5
# for i in range(1,2*rows):
#    spaces=rows-i if i<=rows else i-rows
#    cols=i if i<=rows else rows*2-i
#    print((" "*spaces)+("* "*cols))
    
    
    
    
# rows = 5
# for i in range(1,rows*2):
#     spaces= i-1 if i<=rows else 2*rows-i
#     cols= rows-i+1 if i<=rows else i-rows+1
#     print((" "*spaces)+("* "*cols))



# rows = 5
# code = 97
# for i in range (1,2*rows):
#     res=""
#     spaces= rows-i if i<=rows else i-rows
#     cols=i if i<=rows else rows*2-i
#     res=( " "*spaces)
#     for j in range(cols):
#         res+= chr(code)+" "
#         code+=1
#     print(res)    