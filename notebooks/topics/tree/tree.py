"""
Definition for a binary tree node.
"""

import itertools
import logging
import collections
import itertools
import json
from typing import Optional

logger = logging.getLogger()


class TreeNode:
    """Binary Tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"N({self.val})"

    def insert(self, node):
        if node.val < self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        elif node.val > self.val:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        else:  # node.val == self.val:
            raise ValueError(f"Duplicate: {node.val}")

    @classmethod
    def from_iterable(cls, it):
        it = next(it)
        root = cls(next(it))
        for value in it:
            root.insert(cls(value))
        return root


def breadth_first_build(seq):
    def _build(value):
        if value is None:
            return None
        return TreeNode(value)

    if not seq:
        return None

    if not seq:
        return None

    sides = itertools.cycle(["left", "right"])
    seq = iter(seq)
    root = _build(next(seq))
    que = [root]

    for side, value in zip(sides, seq):
        node = _build(value)
        setattr(que[0], side, node)
        if node:
            que.append(node)
        if side == "right":
            que.pop(0)

    return root


def deserialize(text: str) -> Optional[TreeNode]:
    seq = json.loads(text)
    return breadth_first_build(seq)


def serialize(root: Optional[TreeNode]) -> str:
    queue = collections.deque()
    if root is not None:
        queue.append(root)

    out = []
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # Remove trailing nulls
    while out[-1] is None:
        out.pop()
    return json.dumps(out, separators=(",", ":"))


def pre_order_iter(root: Optional[TreeNode]):
    if root is None:
        return
    yield root
    yield from pre_order_iter(root.left)
    yield from pre_order_iter(root.right)


def breadth_first_iter(node: TreeNode, level: int = 0):
    queue = collections.deque([(node, level)])
    while queue:
        node, level = queue.popleft()
        if node is None:
            continue
        yield node, level
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))


def inorder_iter(node: Optional[TreeNode]):
    if node is None:
        return
    yield from inorder_iter(node.left)
    yield node
    yield from inorder_iter(node.right)


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_depth = max_depth(root.left) + 1
    right_depth = max_depth(root.right) + 1
    return max(left_depth, right_depth)


def compare_trees(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    """Return True if the trees have the same structure and values."""
    que = collections.deque()
    que.appendleft((t1, t2))

    while que:
        node1, node2 = que.pop()

        if node1 is None and node2 is None:
            # both are None: they are the same
            continue
        elif node1 is None or node2 is None:
            logger.debug(
                f"Trees differ because one of the nodes is None: {node1=}, {node2=}"
            )
            return False

        if node1.val != node2.val:
            logger.debug(
                f"Trees differ because values are different: {node1=}, {node2=}"
            )
            return False

        que.append((node1.left, node2.left))
        que.append((node1.right, node2.right))

    return True


def dfs(root: Optional[TreeNode]):
    stack = collections.deque()  # queue of (node, parent, level)
    stack.append((root, None, 0))
    done = {None}  # is this node processed?

    while stack:
        node, parent, level = stack.pop()
        if node in done:
            continue

        if node.left in done and node.right in done:
            yield node, parent, level
            done.add(node)
        else:
            stack.append((node, parent, level))
            stack.append((node.right, node, level + 1))
            stack.append((node.left, node, level + 1))


def verify_binary_search_tree(root: Optional[TreeNode]) -> bool:
    values = [node.val for node in inorder_iter(root)]
    logger.info("verify_binary_search_tree, values = %r", values)
    left, right = itertools.tee(values)
    next(right)
    for prev, cur in zip(left, right):
        if prev >= cur:
            logger.info("Tree is not a valid BST due to these values: %r and %r", prev, cur)
            return False
    return True

