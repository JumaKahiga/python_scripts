#!/usr/bin/env python

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if not self.start_node:
            return 'List is empty'
        else:
            n = self.start_node

        while n:
            print(n.item, "")
            n = n.next

    def append_item(self, new_node):
        current = self.start_node

        if self.start_node:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.start_node = new_node

    def get_position(self, position):
        counter = 1
        current = self.start_node
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.start_node
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.start_node
            self.start_node = new_element

    def delete(self, value):
        current = self.start_node
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.start_node = current.next

    def insert_first(self, new_element):
        new_element.next = self.start_node
        self.start_node = new_element

    def delete_first(self):
        if self.start_node:
            deleted_element = self.start_node
            temp = deleted_element.next
            self.start_node = temp
            return deleted_element
        else:
            return None


class Stack:
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()

node = Node(2)
node2 = Node(3)
my_list = LinkedList()

# print(my_list.append_item(node))
# print(my_list.append_item(node2))
# print(my_list.start_node.item)


def solution(A):
    # write your code in Python 3.6
    integers_list = set([1,2,3,4,5,6,7,8,9])
    print(type(integers_list))
    
    my_list = set(A) - (set(A) - integers_list)
    a_list = (integers_list.difference(my_list))
    
    return min(a_list)

A = [1, 3, 6, 4, 1, 2, 15, 100]
print(solution(A))