class Node(object):
 
    def __init__(self, data, next):
        self.data = data
        self.next = next
 
 
class SingleList(object):
 
    head = None
    tail = None
    num_elements = 0
 
    def show(self):
        print "Showing list data (len=%s):" % self.num_elements
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None
 
    def insert(self, i, node_value):
        """Insert object `node_value` before index i. Raise IndexError if i is out of range."""
        node = Node(node_value, None)
        if i < 0 or i > self.num_elements:
            raise IndexError("Insert index is out of range.")
        if i == 0:
            node.next = self.head
            self.head = node
        else:
            current_node = self.head
            for j in xrange(i - 1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
        self.num_elements += 1

    def pop(self, i):
        if i < 0 or i >= self.num_elements:
            raise IndexError("Pop index is out of range.")
        if i == 0:
            result = self.head.data
            self.head = self.head.next
        else:
            current_node = self.head
            for j in xrange(i - 1):
                current_node = current_node.next
            result = current_node.data
            current_node.next = current_node.next.next
        self.num_elements -= 1
        return result

    def append(self, data):
        self.insert(self.num_elements, data)
 
    def remove(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
 
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
        self.num_elements -= 1

    def index(self, node_value):
        i = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_value:
                return i
            else:
                current_node = current_node.next
                i += 1
        raise Exception("Node value (%s) is not found." % node_value)

    def __len__(self):
        return self.num_elements


if __name__ == '__main__':
    s = SingleList()
    s.append(31)
    s.append(2)
    s.append(3)
    s.append(4)
    s.insert(0, 99)
    s.insert(5, 100)
    s.show()

    n = s.pop(0)
    print "popped node is", n
    s.show()

    s.remove(31)
    s.remove(3)
    s.remove(2)
    s.show()

    print "4 is at", s.index(4)
    print "100 is at", s.index(100)
