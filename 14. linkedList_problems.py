class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
	    
class LinkedList:
    def __init__(self, head=None):
        if isinstance(head, (int, float)):
            self.head = Node(head)
            self.length = 1
        elif isinstance(head, list) and head != []:
            self.head = Node(head[0])
            self.convertListToLinkedList(head[1:])
            self.length = len(head)
        else:
            self.head = None
            self.length = 0

    def convertListToLinkedList(self, lst):
        current = self.head
        for i in range(len(lst)):
            current.next = Node(lst[i])
            current = current.next
            

    def appendToTail(self, element):
        current = self.head
        self.length += 1
        if current:            
            while current.next:
                current = current.next
            current.next = Node(element)
        else:
            self.head = Node(element)

    def appendToHead(self, element):
        current = self.head
        self.length += 1
        if current:
            newHead = Node(element)
            newHead.next = self.head
            self.head = newHead
        else:
            self.head = Node(element)

    def deleteNodes(self, value):
        """delete multiple nodes that equals a given value."""
        current = self.head
        self.length -= 1
        if current.value == value:
            self.head = current.next
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
            current = current.next

    def deleteNode(self, value):
        """delete a node that equals a given value."""
        current = self.head
        self.length -= 1
        if current.value == value:
            self.head = current.next
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                break
            current = current.next

    def deleteMiddleNode(self, node):
        """delete a node in the middle given the node."""
        if node is None or node.next is None:
            return 
        next_node = node.next
        node.value = next_node.value     
        node.next = next_node.next

    def printLinkedList(self):
        current = self.head
        while current is not None:
            print(current.value, end = " ")
            current = current.next
        print()

            
    # O(n^2) double loop method
    def removeDuplicates(self):  
        root = self.head
        while root:
            preshoot = root
            shoot = root.next
            while shoot:
                if root.value == shoot.value:
                    preshoot.next = shoot.next
                    shoot = shoot.next
                    self.length -= 1
                else:
                    preshoot = shoot
                    shoot = shoot.next            
            root = root.next

    # O(n) hash set method
    def removeDuplicates(self):
        """Remove duplicate elements from linked list."""
        rear = self.head
        front = rear.next
        hashset = set()
        hashset.add(rear.value)
        while front:
            if front.value in hashset:
                rear.next = front.next
                self.length -= 1
            else:
                hashset.add(front.value)
                rear = front
            front = front.next

    def subList(self, k):
        """Returns elements from the kth index to last."""
        current = self.head
        index = 0
        while current:
            if index >= k:
                print(current.value, end=" ")
            current = current.next
            index += 1
        print()


    def partition(self, k):
        """Partition linked around value k.
           All nodes less than k come before all nodes
           greater than or equal to k
        """
        current = self.head
        head = current
        tail = current
        while current:
            nextNode = current.next
            if current.value < k:
                current.next = head
                head = current
            else:
                tail.next = current
                tail = current
            current = nextNode
        tail.next = None
        self.head = head

    def indexFromLast(self, k):
        """Return kth element starting from last.

           assuming 0-based index
        """
        index = self.length - k - 1
        current = self.head
        counter = 0
        while counter < index:
            current = current.next
            counter += 1
        return current.value

    def getAsNumReversed(self):
        """Return the digits in the linked list as one reversed number."""
        current = self.head
        num = 0
        digit = 1
        while current:
            num += digit * current.value
            current = current.next
            digit *= 10
        return num

    def getAsNum(self):
        """Return the digits in the linked list as one number."""
        current = self.head
        num = 0
        digit = pow(10, self.length-1)
        while current:
            num += digit * current.value
            current = current.next
            digit //= 10
        return num

    def reverse(self):
        """Reverse a linked list."""
        root = self.head
        nodeList = []
        while root:
            nodeList.append(root.value)
            root = root.next
        self.head = None
        for value in nodeList:
            self.appendToHead(value)
        return self
        
def sumLinkedLists(head1, head2):
    num1 = head1.getAsNum()
    num2 = head2.getAsNum()

    num3 = head1.getAsNumReversed()
    num4 = head2.getAsNumReversed()
    return f'The sum of {num1} and {num2} = {num1 + num2}\nThe sum of {num3} and {num4} = {num3 + num4}'

def sumLinkedLists(head1, head2):
    result = 0
    digit = 1
    sumListRev = LinkedList()
    while head1 and head2:
        unit, tenth = (head1.value + head2.value)%10, (head1.value + head2.value)//10
        result += digit * unit
        sumListRev.appendToTail(unit)
        head1 = head1.next
        head2 = head2.next
        digit *= 10
        if head1:
            head1.value += tenth
        elif head2:
            head2.value += tenth
        else:
            result += digit * tenth
            sumListRev.appendToTail(tenth)

    while head1:
        result += digit * head1.value
        sumListRev.appendToTail(head1.value)
        head1 = head1.next

    while head2:
        result += digit * head2.value
        sumListRev.appendToTail(head2.value)
        head2 = head2.next
            
    print("Linked List in reverse order")
    sumListRev.printLinkedList()
    print("Linked List in digit order")
    sumList = sumListRev.reverse()
    sumList.printLinkedList()
    print("Int result")
    return result

ll = LinkedList()
ll.appendToTail(1)
ll.appendToTail(4)
ll.appendToTail(1)
ll.appendToTail(3)
ll.deleteNode(4)
ll.appendToTail(1)
ll.appendToTail(7)
ll.appendToTail(8)
ll.appendToTail(9)
ll.appendToTail(1)
ll.appendToTail(3)
ll.appendToTail(4)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.printLinkedList()
##ll.removeDuplicates()
##ll.printLinkedList()
##ll.subList(2)
##print(ll.indexFromLast(4))
##ll.partition(4)
##ll.printLinkedList()

ll.appendToHead(5)
ll.printLinkedList()
ll.reverse()
ll.printLinkedList()

print("Sum List")
linkedList1 = LinkedList(1)
linkedList1.appendToTail(7)
linkedList1.appendToTail(1)
linkedList1.appendToTail(6)
linkedList1.reverse()

linkedList2 = LinkedList(5)
linkedList2.appendToTail(9)
linkedList2.appendToTail(2)
linkedList2.reverse()

linkedList3 = LinkedList([1,9,7,8])
linkedList3.reverse()
linkedList4 = LinkedList([6,8,5])
linkedList4.reverse()

print(sumLinkedLists(linkedList3.head, linkedList4.head))


