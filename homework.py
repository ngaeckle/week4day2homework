class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, node):
        #set the current head to the next node
        node.next = self.head
        #now the head is open so set the passed in node as the head
        self.head = node

    def add_last(self, node):
        #if there is no head set the the passed in node as the head
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        #get to the last node and set its next node to the passed in node
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                #set the new nodes next node = to the next node of the target node
                new_node.next = node.next
                #set the target nodes next node = to the passed in node , which places it next in the list
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                #once the target node is found, set the passed in node = previous nodes next node, and set the passed in nodes next node = the target node
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                #literally just forget about the target node by setting the previous nodes next node = to the target nodes next node, which just makes everthing forget about the target node
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

