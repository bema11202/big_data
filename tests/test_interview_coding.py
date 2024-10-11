# Python code will go here
import os
import sys
import pytest
from PIL.ImImagePlugin import number


# Given a tree with n nodes, rooted at node 0 (nodes are numbered from 0 to n - 1), with values assigned to nodes such that values[i] denotes the  value of node i, find the maximal sum of values along any path starting at some nde u and going oly down the tree. In other words, only consider path u1, u2, u3 ..., uk where each node ui is a child of node ui-1 for 1<1k. For example, given the following three (labeled node number/value):
# 0/5   1/7  2/-10   3/4
# 4/2   5/8   6/0   7/3

# Constraints:
# 1 <= n <= 10^5
# parent[0] = -1
# 0 <= parent[i] <= n - 1 for 1 <= i <= n-1
# -1000 <= values[i] <= 1000
# The tree described is valid, meaning that it represents a real tree structure and the values are valid.

# Calculate the best sum downward three path for each node and return the maximum sum.


@pytest.fixture(scope="module")
def calculate_max_sum():
    """:return:"""
    # Create a dictionary to store the best sum downward three path for each node.
    parent = []
    values = []
    best_sum = {}

    # Calculate the best sum downward three path for each node.
    for node in range(len(parent)):
        if node == 0:
            best_sum[node] = values[node]
        else:
            best_sum[node] = max(values[node] + best_sum[parent[node]], best_sum[node - 1])
            if node - 2 >= 0:
                best_sum[node] = max(best_sum[node], values[node] + best_sum[parent[node - 2]])
    return best_sum[len(parent) - 1]


def test_calculate_max_sum(calculate_max_sum):
    parent = [-1, 0, 0, 1]
    values = [5, 7, -10, 4]
    assert calculate_max_sum(parent, values) == 13
