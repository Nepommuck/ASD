class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# deleates max val and returns: (new_first, found_max)
def get_max(first):
    if first is None:
        return None, None
    wart = Node(None, first)
    mx = wart # because wart.next is first candidate for max
    k = mx
    while k.next is not None:
        if k.next.val > mx.next.val:
            mx = k
        k = k.next
    k = mx
    mx = mx.next
    k.next = mx.next
    return wart.next, mx


def insert(first, item):
    wart = Node(None, first)
    k = wart
    while k.next is not None and k.next.val < item.val:
        k = k.next
    item.next = k.next
    k.next = item
    return wart.next


def insertion_sort(first):
    if first is None or first.next is None:
        return first

    wart = Node(None, first)
    prev = wart.next
    k = prev.next
    while k is not None:
        fol = k.next
        prev.next = fol
        wart.next = insert(wart.next, k)
        k = fol
        while prev.next is not k:
            prev = prev.next
    return wart.next


def selection_sort(first):
    wart = Node(None, first)
    k = wart
    while k.next.next is not None:
        k.next, i = get_max(k.next)
        i.next = k.next
        k.next = i

        k = k.next
        # show(wart)
    return wart.next
