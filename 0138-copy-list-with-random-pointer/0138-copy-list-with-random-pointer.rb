def copyRandomList(head)
    return nil if head.nil?

    map = {}

    # Step 1: Create all new nodes
    current = head

    while current
        map[current] = Node.new(current.val)
        current = current.next
    end

    # Step 2: Connect next and random pointers
    current = head

    while current
        copy = map[current]

        copy.next = map[current.next] if current.next
        copy.random = map[current.random] if current.random

        current = current.next
    end

    return map[head]
end