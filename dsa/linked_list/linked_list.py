class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.link:
            itr = itr.link
            
        itr.link = Node(data, None)
        
    # creates a new linked list with all values within a list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_values_at_end(self, data_list):
        if self.head is None:
            for data in data_list:
                self.insert_at_end(data)
        else:
            itr = self.head
            while itr.link:
                itr = itr.link
            
            for data in data_list:
                itr.link = Node(data, None)
                itr = itr.link
                
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.link
        return count
    
    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(value)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value, itr.link)
                itr.link = node
            itr = itr.link
            count +=1    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.link
            return    
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.link = itr.link.link
                break
            itr = itr.link
            count += 1
        
    def print_list(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        
        itr = self.head
        string = ""
        while itr:
            if itr.link is not None:
                string += str(itr.data) + " --> "
            else:
                string += str(itr.data)
            itr = itr.link
        print(string)
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.insert_at_end(0)
    ll.insert_at_end(-5)
    ll.insert_values_at_end([50, 60, 70])
    ll.remove_at(6)
    ll.insert_at(6, 65)
    ll.print_list()
    print("length:",ll.get_length())
    
# add method to remove node by value
# add method to swap two nodes