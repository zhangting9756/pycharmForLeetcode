# -*- coding: UTF-8 -*-
import numpy as np


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def _str_(self):
        val = '{%d: %d}' % (self.key, self.value)
        return val

    def _repr_(self):
        val = '{%d: %d}' % (self.key, self.value)
        return val


class DoubleLinkedList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    # 从头部添加
    def _add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1

    # 从尾部添加
    def _add_tail(self, node):
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.next = None
            self.tail.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None

    # 从尾部删除
    def _del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            self.tail = node.prev
            self.tail.next = node
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # 从头部删除
    def _del_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # 任意结点删除
    def _remove(self, node):
        # 如果node=None，默认删除尾部结点
        if not node:
            node = self.tail
        if node == self.tail:
            self._del_tail()
        elif node == self.head:
            self._del_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node

        # 弹出头部结点

    def pop(self):
        return self._del_head()

    # 添加结点
    def append(self, node):
        return self._add_tail(node)

        # 往头部添加结点

    def append_front(self, node):
        return self._add_head(node)

    # 删除结点
    def remove(self, node):
        return self._remove(node)

    def print(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '=>'
        print(line)


if __name__ == '__main__':
    l = DoubleLinkedList()
    nodes = []
    for i in range(10):
        node = Node(i, i)
        nodes.append(node)
    l.append(nodes[0])
    l.print()
    l.append(nodes[1])
    l.print()
    l.pop()
    l.print()
    l.append(nodes[2])
    l.print()
    l.append_front(nodes[3])
    l.print()
    l.append(nodes[4])
    l.print()
    l.remove(nodes[2])
    l.print()



