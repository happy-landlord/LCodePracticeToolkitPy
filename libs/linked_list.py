class ListNode:
    """
    Definition for singly-linked list.
    """

    def __new__(cls, val=0, next=None):
        # 如果传入的是列表，则调用 from_list 进行转换，直接返回链表头节点
        if isinstance(val, list):
            return cls.from_list(val)
        return super().__new__(cls)

    def __init__(self, val=0, next=None):
        # 当 __new__ 返回的对象已经设置了 val（例如从列表转换而来），则避免重复初始化
        if hasattr(self, 'val'):
            return
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values):
        """
        根据列表构造链表，并返回头节点。
        :param values: Python list
        :return: ListNode (head)
        """
        dummy = object.__new__(cls)
        dummy.val = 0
        dummy.next = None
        current = dummy
        for x in values:
            node = object.__new__(cls)
            node.val = x
            node.next = None
            current.next = node
            current = node
        return dummy.next

    def to_list(self):
        """
        将链表转换为 Python list。
        :return: 包含链表所有节点值的列表
        """
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

    def to_safe_list(self):
        """
        安全地将链表转换为列表，避免由于链表中存在环而导致无限循环。
        遍历链表时记录每个节点首次出现的索引，如果遇到已访问过的节点，则返回收集到的列表以及循环入口的索引。
        :return: (list_of_values, cycle_index) 如果没有环则 cycle_index 为 None
        """
        result = []
        seen = {}
        current = self
        idx = 0
        while current:
            if id(current) in seen:
                return result, seen[id(current)]
            seen[id(current)] = idx
            result.append(current.val)
            current = current.next
            idx += 1
        return result, None


class LinkedList:
    """
    辅助链表类，提供初始化、打印、转换以及创建环的功能。
    """

    def __init__(self, values=None):
        """
        初始化链表。如果传入的是列表，则自动转换为链表；如果传入的是 ListNode，则直接使用。
        :param values: list 或 ListNode
        """
        if values is None:
            self.head = None
        elif isinstance(values, list):
            self.head = ListNode.from_list(values)
        elif isinstance(values, ListNode):
            self.head = values
        else:
            raise TypeError("Unsupported type for values. Must be list or ListNode.")

    def to_list(self):
        """
        将链表转换为 Python list。
        :return: 包含链表中所有节点值的列表
        """
        if not self.head:
            return []
        return self.head.to_list()

    def print_list(self):
        """
        打印链表所有节点值。
        """
        if not self.head:
            print("Empty list")
            return
        current = self.head
        output = []
        while current:
            output.append(str(current.val))
            current = current.next
        print(" -> ".join(output) + " -> None")

    def add_cycle(self, pos):
        """
        在链表中创建环，用于测试含环问题。
        :param pos: 环入口的索引（从 0 开始），-1 表示不创建环
        """
        if pos == -1 or not self.head:
            return
        cycle_entry = None
        current = self.head
        index = 0
        last = None
        while current:
            if index == pos:
                cycle_entry = current
            last = current
            current = current.next
            index += 1
        if last:
            last.next = cycle_entry  # 形成环

    def has_cycle(self):
        """
        Detect if the linked list has a cycle using Floyd's Tortoise and Hare algorithm.
        :return: True if a cycle exists, False otherwise
        """
        if not self.head or not self.head.next:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


#######################
# 自动补丁逻辑：转换测试用例中的其他列表参数（如 'list1'、'list2'）
#######################

def patch_test_cases():
    """
    遍历 sys.modules 中的所有模块，
    如果模块中定义了 test_cases，则自动将其中 'list1' 和 'list2'（如果为列表）转换为链表（ListNode）。
    注意：这里不转换 head 字段，head 留待 preprocess_test_cases 统一处理。
    """
    import sys
    for module in sys.modules.values():
        if hasattr(module, 'test_cases'):
            test_cases = getattr(module, 'test_cases')
            if isinstance(test_cases, list):
                for test in test_cases:
                    for key in ['list1', 'list2']:
                        if key in test and isinstance(test[key], list):
                            test[key] = ListNode.from_list(test[key])


# 自动调用补丁逻辑
patch_test_cases()
