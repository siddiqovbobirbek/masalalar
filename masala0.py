# import math
 
# def move(list1):
#   list1.sort()
# list1 = [11, -21, 4, 6, -12, 45, 66, -93]
# move(list1)
# for e in list1:
#     if e>0:
#         print(e, end = "  \n") 

# for num in list1:
#     if num < 0:
#       print(num, end=" ")


# import turtle
# import colorsys
# t=turtle.Turtle()
# s=turtle.Screen()
# s.bgcolor("black")
# t.speed(10000)
# n=36
# h=0
# for i in range(160):
#     c=colorsys.hsv_to_rgb(h,1,0.9)
#     h+=1/n
#     t.color(c)
#     t.left(145)
#     for j in range(5):
#         t.forward(300)
#         t.left(150)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 2
# del my_list[n - 1::n]
# print(my_list) 

# Linked list implementation in Python


# class Node:
#     # Creating a node
#     def __init__(self, item):
#         self.item = item
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None


# if __name__ == '__main__':

#     linked_list = LinkedList()

#     # Assign item values
#     linked_list.head = Node(1)
#     second = Node(2)
#     third = Node(3)

#     # Connect nodes
#     linked_list.head.next = second
#     second.next = third

#     # Print the linked list item
#     while linked_list.head != None:
#         print(linked_list.head.item, end=" ")
#         linked_list.head = linked_list.head.next



import random
 
rand_list=[]
m=10
for i in range(m):
    rand_list.append(random.randint(0,9))
print(rand_list)
n = 2
del rand_list[n - 1::n]
print("Har ikkinchi element o'chgandan keyin: \n", rand_list)