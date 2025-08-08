# rows=5
# for i in range (1,rows+1):
#     res=""
#     for spaces  in range(1,rows-i+1):
#          res+=" "   
#     for j in range (1,i+1):
#         res+="*"+" " 
#     print(res)        
    
    
# rows = 5
# for i in range(rows,0,-1):
#     res=""   
#     for spaces in range (1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" " 
#     print(res)  


# rows = 4
# num=1
# for i in range (1,rows+1):
#     res=""   
#     for space in range (1,rows-i+1):
#         res=" "
#     for j in range (1,i+1):
#         res+= str(num) + " "   
#         num+=1  
#     print(res)      


# rows = int(input("enter a value: "))
# num=1
# for i in range (1,rows+1):
#     res =""       
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range (1,i+1):
#         if num<10:
#           res+= "0"+ str(num) + " "
#           num+=1  
#         else:
#             res+=str(num)+" "
#             num+=1
#     print(res)       



# rows=5
# asc=97
# for i in range (1,rows+1):
#     res=""
#     for space in range(1,rows-i+1):
#         res=" "
#     for j in range (1,i+1):
#         res+= chr(asc)+" "    
#         asc+=1
#     print(res)


        

# # Print H
# for row in range(5):
#     for col in range(5):
#         if col == 0 or col == 4 or row == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print()  

# # Print E
# for row in range(5):
#     for col in range(5):
#         if col == 0 or row == 0 or row == 2 or row == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print()  

# # Print N
# for row in range(5):
#     for col in range(5):
#         if col == 0 or col == 4 or row == col:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# # Print Z
# for row in range(5):
#     for col in range(5):
#         if row == 0 or row == 4 or row + col == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print()  

# # Print Y
# for row in range(5):
#     for col in range(5):
#         if (row <= 2 and (row == col or row + col == 4)) or (row >= 2 and col == 2 and row >= 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print()  

# # Print M
# for row in range(5):
#     for col in range(5):
#         if col == 0 or col == 4 or (row == col and row <= 2) or (row + col == 4 and row <= 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# if i == 0 or i == rows - 1:
#     print("*")  
# elif j == cols // 2:
#     print("*")  
# else:
#     print(" ")
