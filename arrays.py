
import pdb

def find_duplicates(n_list):
  """Find duplicated number in a integer list

  Args:
      n_list (list): interger list where we will find duplicated values
  """
  duplicated_values =[]
  for i in range(len(n_list)):
    if n_list[abs(n_list[i])] < 0:
      duplicated_values.append(-1*n_list[abs(n_list[i])])
    else:
      n_list[abs(n_list[i])] =  -1*n_list[abs(n_list[i])]
  if len(duplicated_values)==0:
    return False
  else:
    return duplicated_values

def anagram(word1, word2):
  """Checks if two words are anagrams

  Args:
      word1 (string): Word number 1
      word2 (string): Word number 2 to check if it's anagram of word 1
  """
  l_w1 = list(word1)
  l_w2 = list(word2)
  for i in l_w1:
    for j in l_w2:
      if i == j:
        l_w1_c.remove(i)
        l_w2_c.remove(j)
        break;
  if len(l_w2_c) == 0 & len(l_w1_c) == 0:
    return True
  else:
    False
        
 
def integer_reversing(integer):
  """Reverse a given integer

  Args:
      integer ([type]): [description]
  """
  reverse_int = 0
  
  while (integer/10) >0:
   print(integer)
   unit = int(integer%10)
   reverse_int = reverse_int *10 + unit
   integer = int(integer/10)
   
 
  return reverse_int
   
  
  

def reverse_array(array):
  """This function reverse the order of a given array

  Args:
      array (list): Some awesome array
  """
  s_start =  0
  s_end = len(array) -1
  while s_start < s_end:
    #swapping operation
    array[s_start], array[s_end] =  array[s_end], array[s_start]
    s_start +=1
    s_end -= 1
  return array

def check_palindrome(palindrome):
  """Checks if the passed palindrome string is a palindrome word i.e
  if the the word can be readed from left to right and from right to left

  Args:
      palindrome ([type]): [description]
  """
  s_start = 0
  s_end = len(palindrome)-1
  while palindrome[s_start] == palindrome[s_end]:
    s_start += 1
    s_end -= 1
    if s_start >= s_end:
      return True
  return False

if __name__ == '__main__':
    

  array = [1,2,3,4,5]
  inclusive_start = 1
  exclusive_end = 3

  #! All the elements inside the array can be access using their index.
  #! If we wnat to get the first element we always need to start with 0
  #! Arrays in python allow us to use different type of elements inside the array.
  seleceted_elements  = array[inclusive_start: exclusive_end]
  print(seleceted_elements)

  #! In this case we should note that inclusive_start == 1 will include the element with index number 1 in our array
  #! when we use the : operator to select a range of elements inside the array. On the other hand the element
  #! linked to exclusive_end will not be added in this range so array[3] == 4 will no be part of  seleceted_elements  

  #* linear search O(N) we need to iterate trough all the elements in order to find the max number in array

  max = array[0] #? Linear Search -> O(N) operation  
  for i in range(len(array)):
    if array[i] > max:
      max = array[i]
  #! There are no real arrays in python since everything inside python is a 

  array_reverse = reverse_array(array)
  palindrome = "abcdcba"
  
  print(check_palindrome(palindrome))
  print(check_palindrome('not a palindrome'))

      

  reverse_int = integer_reversing(4321)
  t1 = find_duplicates([1,2,3,4,0])
  t2 = find_duplicates([1,2,3,4,4])