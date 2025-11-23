class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def __str__(self):
        out = []
        curr = self
        while curr:
            out.append(curr.val)
            curr = curr.next
        return " -> ".join(out)


def reverse_list(head):
    curr = head
    prev = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

if __name__ == "__main__":
    print("="*10 + "test 00"+ "="*10)
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    
    print(print(reverse_list(a)))

    print("="*10 + "test 01"+ "="*10)
    x = Node("x")
    y = Node("y")

    x.next = y

    # x -> y

    print(reverse_list(x)) # y -> x

    #test_02
    print("="*10 + "test 02"+ "="*10)
    p = Node("p")
    # p
    print(reverse_list(p)) # p

