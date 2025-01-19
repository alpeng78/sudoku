e= None

inn=[   [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e],
       [e,e,e,e,e,e,e,e,e]]

for row in range(9):
    for column in range(9):
       inn[row][column]=input(f"{row+1},{column+1}: ")
       if inn[row][column] == 'e' is False:
           int(inn[row][column])

pos_matr=inn

def check(list):
   success=True

   for row in range(len(list)):
       for num in range(1, 10):
           if list[row].count(num) > 1:
               success = False
          
   vert_lis=[]
   for column in range(len(list)):
       for row in range(len(list)):
           vert_lis.append(list[row][column])
       vert_lis=[]
       for num in range(1, 10):
           if vert_lis.count(num) > 1:
               success = False

   square=[]
   ir=range(0,9,3)
   ic=range(0,9,3)
   for r in ir:
       for c in ic:
           for i in range(3):
               row = r + i
               for j in range(3):
                   col = j + c
                   square.append(list[row][col])
                   for num in range(1, 10):
                       if square.count(num) > 1:
                           success = False
           square=[]

   if success == True:
       return True
   else:
       return False

def mount(inn,row,column):
   if inn[row][column] == None or isinstance(inn[row][column], list):
       pos=[1,2,3,4,5,6,7,8,9]


       for num in range(1, 10): 
           if inn[row].count(num) >= 1:
               if pos.count(num) > 0:
                   pos.remove(num)
  
       vert_lis=[]
       for i in range(len(inn)):
           vert_lis.append(inn[i][column])
           for num in range(1, 10):
               if vert_lis.count(num) >= 1:
                   if pos.count(num) > 0:
                       pos.remove(num)
                                       
       if row < 3:
           ir=0
       elif row < 6:
           ir=3
       elif row > 5:
           ir=6
      
       if column < 3:
           ic=0
       elif column < 6:
           ic=3
       elif column > 5:
           ic=6
      
       trow=row
       tcol=column
       square=[]
       for i in range(3):
                   trow = ir + i
                   for j in range(3):
                       tcol = j + ic
                       square.append(inn[trow][tcol])
                       for num in range(1, 10):
                           if square.count(num) >= 1:
                               if pos.count(num) > 0:
                                   pos.remove(num)
                                  
       return pos
   else:
       return inn[row][column]

def possibility_matrix(inn):
   min_len = 10
   min_len_list = []

   for row in range(9):
       for column in range(9):
           pos = mount(inn,row,column)
           pos_matr[row][column]=pos
           if isinstance(pos, list):
               if len(pos) < min_len:
                   min_len = len(pos)
                   min_len_list = [[row,column]]
               elif len(pos) == min_len:
                   min_len_list += [[row,column]]

   return min_len, min_len_list

def check_for_list(matr,no):
     for row in range(9):
       for column in range(9):
               if isinstance(matr[row][column], list):
                   if len(matr[row][column]) == no:
                       return True

def fill_matr(matr):
   while check_for_list(matr,1):
       for row in range(9):
           for column in range(9):
               if isinstance(matr[row][column], list):
                   if len(matr[row][column]) == 1:
                       matr[row][column] = matr[row][column][0]
       min_len, min_len_list = possibility_matrix(matr)
 
   for row in range(9):
       for column in range(9):
           if isinstance(matr[row][column], list):
               if check(matr) == True:
                   return "unsolved (wip)"
               else:
                   return "error"
   if check(matr) == False:
       return "error"
   elif check(matr):
       return "solved"
  
if (check(inn)) == False:
   print("ERROR")
   exit()

min_len, min_len_list = possibility_matrix(inn)

can_dict=dict()

for t in min_len_list:
   r=t[0]
   c=t[1]
   can_dict[(r,c)] = pos_matr[r][c]

test_matr=pos_matr

print(fill_matr(pos_matr))

for i in pos_matr:
    print(i)

print(check(pos_matr))
