class Node:
    def __init__(self, key = -1, val = -1):
        self.val = val
        self.key = key
        self.backward = None
        self.forward = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.keyPointerLookup = {}
        self.capacity = capacity
        self.end = Node()
        self.head.forward = self.end
        self.end.backward = self.head

    def get(self, key: int) -> int:
        keyPointerLookup = self.keyPointerLookup
        headNode = self.head
        if key not in keyPointerLookup:
            return -1

        currNode = keyPointerLookup[key]
        if currNode == headNode.forward:
            return currNode.val

        prevNode = currNode.backward
        nextNode = currNode.forward

        prevNode.forward = nextNode
        nextNode.backward = prevNode

        firstNode = headNode.forward
        currNode.forward = firstNode
        currNode.backward = headNode

        firstNode.backward = currNode
        headNode.forward = currNode
        return currNode.val

        
    def put(self, key: int, value: int) -> None:
        headNode = self.head
        endNode = self.end
        keyPointerLookup = self.keyPointerLookup
        if key in keyPointerLookup:
            currNode = keyPointerLookup[key]
            currNode.val = value

            if currNode == headNode.forward:
                return

            prevNode = currNode.backward
            nextNode = currNode.forward

            prevNode.forward = nextNode
            nextNode.backward = prevNode
      
            firstNode = headNode.forward

            currNode.forward = firstNode
            firstNode.backward = currNode

            headNode.forward = currNode
            currNode.backward = headNode

        else:
            keyPointerLookup[key] = Node(key, value)
            currNode = keyPointerLookup[key]
            nextNode = headNode.forward

            currNode.backward = headNode
            currNode.forward = nextNode

            headNode.forward = currNode
            nextNode.backward = currNode

            if len(keyPointerLookup) > self.capacity:
                lastNode = endNode.backward
                nodeKey = lastNode.key

                prevToLastNode = lastNode.backward
                lastNode.backward = None
                lastNode.forward = None

                prevToLastNode.forward = endNode
                endNode.backward = prevToLastNode

                del keyPointerLookup[nodeKey]
