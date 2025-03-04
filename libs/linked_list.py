# libs/linked_list.py

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
        while current.next:
            if index == pos:
                cycle_entry = current
            current = current.next
            index += 1
        current.next = cycle_entry  # 形成环

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
# 自动补丁逻辑：转换测试用例中的列表为链表
#######################

def patch_test_cases():
    """
    遍历 sys.modules 中的所有模块，如果模块中定义了 test_cases，
    则自动将其中 'list1' 和 'list2'（如果为列表）转换为链表（ListNode）。
    """
    import sys
    for module in sys.modules.values():
        # 模块必须有 test_cases 属性，且 test_cases 为列表
        if hasattr(module, 'test_cases'):
            test_cases = getattr(module, 'test_cases')
            if isinstance(test_cases, list):
                for test in test_cases:
                    for key in ['list1', 'list2']:
                        if key in test and isinstance(test[key], list):
                            test[key] = ListNode.from_list(test[key])

        if hasattr(module, 'test_cases') and isinstance(module.test_cases, list):
            for test in module.test_cases:
                # Convert "head" to linked list
                if "head" in test and isinstance(test["head"], list):
                    linked_list = LinkedList(test["head"])
                    test["head"] = linked_list.head
                    # Apply cycle if "pos" exists and is valid
                    if "pos" in test and test["pos"] != -1:
                        linked_list.add_cycle(test["pos"])


# 在模块加载时自动调用补丁逻辑，确保测试用例的输入都转换成链表
patch_test_cases()
