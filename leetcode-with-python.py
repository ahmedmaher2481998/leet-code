# reference 
# https://leetcode.com/discuss/study-guide/2122306/Python-Cheat-Sheet-for-Leetcode
#  types are detected in run time 
n,m =0,'abc'
n+=1
n-=1
n*=1
n // 1  # divide with no reminder
# null is None
# if n:
  # do things
# and or not
# while condition:
# code
# for i in range(n): range(start,end not including,step)
  # do things
# 5 /2 = 2.5  will return float
# int div 5 // 2 = 2  round down
# fix is int(5/2) rounds to wards zero
# 10 % 3 = 1 , carful when using negative numbers
# -10 % 3 = 2 not normal
# import math
# math.fmod(-10,3) => 1 
# math.floor(3 / 2) rounds down 1
# math.ceil(3 / 2) rounds up 2
# math.sqrt(4) 2
# math.pow(2,3) 8
# flaot('inf') float('-inf)
# ********array/list & strings 
# arr = ['a', 'b', 'c', 'd', 'e', 'f']
# append pop insert(i,value)
# arr[0] = "c"
# arr = [-1] * 5 => [-1,-1,-1,-1,-1] creating array with fixed size # reading from the back last element index = -1 ,arr[-1],arr[-2] and so on 
# sub lists arr[:2] from the start up to but not including the index 2
# arr[0:4] , arr[:] the whole array
# a,b,c,d,e,f = arr
# for i in range(len(arr)):
# for n in arr:
# for i,n in enumerate(arr):
# for n1,n2 in zip(nums1,nums2):
# n1 is from nums1 and n2 is from nums2
# arr.reverse() , arr.sort() in ascending order from small to large 
# or alphabetically order , 
# arr.sort((lambda x:len(x)))
# arr = [i + i  for i in range(5) ]
# if we want to build 4*4 grid of all zeros 
#  ([0] * 4 for i in range(4))
# you can use slicing array syntax with strings 
# but they are immutable
# a ='abc' a[:1]=->'a'
# a[0]='b' won't work because it is mutable
# a ='123' string to convert to int int(a)=>123
# a= 123 to convert to string str(a)=>'123'
# getting ascci value of a letter ord('a') => 97
# ','.join(arr) => a,b,c,d,e,f,g

# ********************* Queue
# from collections import deque
# q = deque()
# q.append(val)
# popleft take fist element
# pop take last element
# appendleft insert at the start of the queue
# when using a queue we want to only use append to insert and pop left to take out elements 
# ******************* HasSet
# no duplicates allowed 
# my_set =  set()
# add
# len(my_set)
# n in my_set => True / False
# my_set.remove(n) 
# set([1,2,3 ])
# set(i   for i in range(5) )

# ***************************HaspMAps / Dictionaries 
# myMap={}
# myMap['key'] = value4 # inserting into a hasp map
# myMap['newKey'] = value4
# myMap['key'] = value2 #updating a key value 
# len(myMap) returns the number of keys
# hash map doesn't allow duplicate keys
#  removing a key from a hasp map
# myMap.pop('key')
# checking if a key is in a hasp map
# 'newKey' in myMap => True 
# we also initialize the hasp map with values
# myMap = {"key": value4, "newKey": value2}
# initializing hashmap with ket,value with iterators
# myMap = {i: i * 2 for i in range(3)}
# myMap = {0:0 , 1:2,2:4}
# iterating over hashmap
# for key in myMAp 
# for val in myMAp.values()
# for key,value in myMAp.items()
# ***************** Tuples 
# tup = (1,2) not mutable 
# can be accessed with indexing 
# mainly used as keys for hash maps and hash sets 
# we can't modify them 
# myMap[(1,2)] = 3  (1,2) in myMap => True 
# my_set.add((1,2)) (1,2) in my_set => True 
# but why ? 
# because lists/arrays aren't hashable
# *************************Heaps 
# by default it's min heaps in python 
# import heapq
# inserting to heap 
# initializes an array as a heap 
# h = []
# adding to the heap => heapq.heappush(value) 
# pop from the heap => heapq.heappop(value) 
# the min value is always at h[0]
# poping till empty 
# for len(h):
  # heapq.heappoop(h)
# python doesn't have max heaps by default
# we can work around that by multiplying by -1 so wen invert the priority of the element 
# but be carful because when we pop to extract values we have to tranform the value to it's original value by mutplying by -1 again 
# we can heapify in O(n) if we have initial values 
# heapq.heapify([1,2,4,5,0,-7,-2]) # converted to min heap 
# to extract from heap in order 
# while h :
  # print(heapq.heappop(h))
# ****************functions 
# def sum(n,m):
  # return n  + m 
# utilize inner functions to get use the scope of the global function 
# def out(a,b):
  # def inner(c,d):
    # return a + b + c + d
  # return inner('c','d')
# we can modify objects but not reassign them
# unless using nonlocal

ar,v = [1,2,3],4
def double(arr,val):
  def helper():
    for i in range(len(arr)):
      arr[i] *= 2 
    # val *= 2 # this will only modify it locally in this function  
  # to modify it out side the scope of the helper function
    nonlocal val 
    val *= 2 # this will modify global
  helper()
  return arr,val
# print(double(ar,v))



# ************Classes in python 
'''
class Name:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def introduce(self):
    return f'Hello, my name is {self.name}. I am {self.age} years old.'
  def birthday(self):
    self.age += 1
  def __str__(self):
    return f'Name: {self.name}, Age: {self.age}

 ahmed = Name('ahmed',25)
 print(ahmed.introduce())
 ahmed.birthday()
 # Printing the object (this calls the __str__ method)
 print(ahmed)

'''