class ListNode:
    def __init__(self,key = 0 , next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode() for i in range(1000)]    

    def add(self, key: int) -> None:
        cur = self.hashset[key % len(self.hashset)] 
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key) 


    def remove(self, key: int) -> None:
        cur = self.hashset[key % len(self.hashset)] 
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next
        return 
    def contains(self, key: int) -> bool:
        cur = self.hashset[key % len(self.hashset)] 
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)