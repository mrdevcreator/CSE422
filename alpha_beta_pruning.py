import random

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def generate_tree(depth, random_points):
    if depth == 0:
        if random_points:
            return TreeNode(random_points.pop(0))
        else:
            return TreeNode()

    node = TreeNode()
    node.left = generate_tree(depth - 1, random_points)
    node.right = generate_tree(depth - 1, random_points)

    return node

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.value is not None:
        return node.value

    if maximizing_player:
        value = float('-inf')
        for child in [node.left, node.right]:
            child_value = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            value = max(value, child_value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in [node.left, node.right]:
            child_value = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            value = min(value, child_value)
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value



user_input = input("Enter your student ID: ").replace('0', '8')
min_point = int(user_input[4])
total_point = int(user_input[-1] + user_input[-2])
max_point = int(total_point * 1.5)
random_points = [random.randrange(min_point,max_point) for _ in range(8)]
print("Generated 8 random points between the minimum and maximum point limits:",random_points)
print("Total points to win:", total_point)

root_node = generate_tree(3, random_points)


achieved_points = alpha_beta_pruning(root_node, 3, float('-inf'), float('inf'), True)
print("Achieved point by applying alpha-beta pruning =", achieved_points)

if achieved_points >= total_point:
    winner = "Optimus Prime"
else:
    winner = "Megatron"

print("The Winner is",winner)
