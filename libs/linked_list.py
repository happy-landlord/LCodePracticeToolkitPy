class ListNode:
    """
    定义一个单向链表的节点。
    """
    def __init__(self, val=0, next=None):
        self.val = val      # 节点的值
        self.next = next    # 指向下一个节点的指针

class LinkedList:
    """
    提供对链表的初始化、构造、打印功能。
    """
    def __init__(self, values=None):
        """
        使用一个可选的数组来初始化链表。
        :param values: 列表或 None（默认创建空链表）
        """
        self.head = None
        if values:
            self.head = self._build_list(values)

    def _build_list(self, values):
        """
        内部方法：通过数组构造链表。
        :param values: 输入的数组
        :return: 链表的头节点
        """
        dummy = ListNode(0)
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    def to_list(self):
        """
        将链表转换为数组，方便调试。
        :return: 一个数组，包含链表中的值。
        """
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def print_list(self):
        """
        打印链表的所有节点值。
        """
        current = self.head
        output = []
        while current:
            output.append(str(current.val))
            current = current.next
        print(" -> ".join(output) + " -> None")

    def add_cycle(self, pos):
        """
        在链表中创建环，方便测试环相关的题目。
        :param pos: 环的入口索引（从 0 开始），-1 表示不创建环
        """
        if pos == -1:
            return
        cycle_entry = None
        current = self.head
        index = 0
        while current.next:
            if index == pos:
                cycle_entry = current
            current = current.next
            index += 1
        current.next = cycle_entry  # 连接成环
