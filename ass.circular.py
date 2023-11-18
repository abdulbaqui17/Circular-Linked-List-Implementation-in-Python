class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class cll:
    def __init__(self):
        self.last=None
    
    def insert_first(self,data):
        n=node(data)
        if self.last==None:
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            
    
    def insert_last(self,data):
        n=node(data)
        if self.last==None:
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
            
    def insert_after(self,target,data):
        if self.last==None:
            return
        n=node(data)
        current=self.last.next
        while True:
            if current.data==target:
                n.next=current.next
                current.next=n 
                if current is self.last:
                    self.last=n
                break
            current=current.next
            if current is self.last.next:
                break
            
    def delete_first(self):
        self.last.next=self.last.next.next
    
    def delete_last(self):
        current=self.last.next
        if current is self.last:  # If there is only one element
            self.last = None
        while True:
            current=current.next
            if current.next is self.last:
                current.next=current.next.next
                self.last=current
                break
    
    def delete_data(self, data):
        if self.last is None:
            return None

        current = self.last
        while True:
            if current.next.data == data:
                if current.next is self.last.next:#just removed element was last
                    current.next = current.next.next
                    self.last = current            #point current as self.last
                    if current.next == self.last.next:  # Check if there's only one element left
                        self.last = None
                    break
                elif current.next == self.last:  # Check if the last element is the one to be deleted
                    self.last = current    
                break
            current = current.next
            if current.next is self.last.next:
                break

    def display(self):
        if self.last is None:
            print("List is empty.")
            return

        current = self.last.next
        while True:
            print(current.data)
            current = current.next
            if current is self.last.next:
                break

 

mylist=cll()
mylist.insert_first(5)
mylist.insert_last(10)
mylist.insert_last(20)
mylist.insert_after(10,15)
mylist.delete_first()
mylist.delete_last()
mylist.delete_data(10)
mylist.display()