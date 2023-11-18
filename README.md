# Circular-Linked-List-Implementation-in-Python
This Python implementation provides a Circular Linked List class (cll) with methods for insertion, deletion, and display operations. It's designed for efficiently managing dynamic data structures.

Features:
Insertion:

insert_first(data): Insert an element at the beginning.
insert_last(data): Insert an element at the end.
insert_after(target, data): Insert an element after a specified target.
Deletion:

delete_first(): Delete the first element.
delete_last(): Delete the last element.
delete_data(data): Delete the node with the specified data.
Display:

display(): Print the elements of the Circular Linked List.
Usage:
python
Copy code
# Example usage:
mylist = cll()
mylist.insert_first(5)
mylist.insert_last(10)
mylist.insert_last(20)
mylist.insert_after(10, 15)
mylist.delete_first()
mylist.delete_last()
mylist.delete_data(10)
mylist.display()
Feel free to fork, clone, and contribute! 🚀
