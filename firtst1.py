class TreeNode:
    """
    Efficient tree node implementation with memory optimization.
    
    Attributes:
    - data: Node's value
    - left: Left child reference
    - right: Right child reference
    
    Space Complexity: O(1) per node
    """
    __slots__ = ['data', 'left', 'right']
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LevelOrderTreeConstructor:
    """
    Specialized Level-Order Tree Construction Utility
    
    Key Features:
    - Handles various null node representations
    - Optimized tree construction
    - Flexible input parsing
    """
    
    @staticmethod
    def build_tree(level_order, null_markers=None):
        """
        Robust level-order tree construction method.
        
        Time Complexity: O(n)
        Space Complexity: O(w), where w is max tree width
        
        Args:
        - level_order: List representing level-order traversal
        - null_markers: Optional custom null value representations
        
        Returns:
        TreeNode: Root of constructed tree
        """
        # Default null markers if not provided
        if null_markers is None:
            null_markers = {-1, -999, None}
        
        # Quick early exit for empty or invalid input
        if not level_order or all(x in null_markers for x in level_order):
            return None
        
        # Remove leading null markers
        while level_order and level_order[0] in null_markers:
            level_order.pop(0)
        
        # Create root node
        root = TreeNode(level_order[0])
        
        # Queue for level-order construction
        queue = [root]
        
        # Input parsing index
        i = 1
        
        while queue and i < len(level_order):
            # Current node being processed
            current = queue.pop(0)
            
            # Left child construction
            if i < len(level_order) and level_order[i] not in null_markers:
                current.left = TreeNode(level_order[i])
                queue.append(current.left)
            i += 1
            
            # Right child construction
            if i < len(level_order) and level_order[i] not in null_markers:
                current.right = TreeNode(level_order[i])
                queue.append(current.right)
            i += 1
        
        return root
    
    @staticmethod
    def max_depth(root):
        """
        Calculates maximum tree depth with tail-recursive optimization.
        
        Time Complexity: O(n)
        Space Complexity: O(h), where h is tree height
        
        Returns tree height considering depth starts from 1
        
        Args:
        - root: Root node of the tree
        
        Returns:
        int: Maximum depth of the tree
        """
        if not root:
            return 0
        
        # Optimized depth calculation avoiding max() function
        left_depth = LevelOrderTreeConstructor.max_depth(root.left)
        right_depth = LevelOrderTreeConstructor.max_depth(root.right)
        
        return 1 + (left_depth if left_depth > right_depth else right_depth)
    
    @staticmethod
    def is_balanced_tree(root):
        """
        Check if tree is height-balanced.
        
        A height-balanced tree is defined as:
        - The left and right subtrees of every node differ in height by no more than 1
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        
        Args:
        - root: Root node of the tree
        
        Returns:
        bool: True if tree is balanced, False otherwise
        """
        def check_height(node):
            """
            Inner function to calculate height and check balance simultaneously.
            
            Returns:
            - Tuple (is_balanced, height)
            """
            if not node:
                return True, 0
            
            left_balanced, left_height = check_height(node.left)
            right_balanced, right_height = check_height(node.right)
            
            # Check current node's balance
            height_diff = abs(left_height - right_height)
            current_balanced = (
                left_balanced and 
                right_balanced and 
                height_diff <= 1
            )
            
            return current_balanced, 1 + max(left_height, right_height)
        
        balanced, _ = check_height(root)
        return balanced

# Utility functions for competitive programming
def tree_diameter(root):
    """
    Calculate tree's diameter (longest path between any two nodes).
    
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Args:
    - root: Root node of the tree
    
    Returns:
    int: Tree's diameter
    """
    def diameter_helper(node):
        """
        Calculate diameter and height simultaneously.
        
        Returns:
        - Tuple (diameter, height)
        """
        if not node:
            return 0, 0
        
        left_diameter, left_height = diameter_helper(node.left)
        right_diameter, right_height = diameter_helper(node.right)
        
        # Current node's diameter possibilities
        current_diameter = max(
            left_diameter,
            right_diameter,
            left_height + right_height + 1
        )
        
        return current_diameter, 1 + max(left_height, right_height)
    
    return diameter_helper(root)[0]

# Competitive programming template-like usage
def main():
    # Test cases covering various scenarios
    test_cases = [
        [3, 1, 2, -1, -1, -1, -1],  # Input 1
        [3, -1, 1, 2, -1, -1, -1],  # Input 2
        [2, -1, -1],  # Input 3
        [27, 16, 33, 14, 15, -1, -1, 17, 34, 10, 37, 21, -1, -1, 44, 13, -1, 22, 38, 45, 11, 31, -1, -1, -1, -1, -1, -1, 47, -1, 20, -1, -1, -1, 43, 39, -1, -1, -1, -1, -1, 36, -1, -1, -1],  # Input 4
        [41, 45, 37, 33, 21, 28, 4, 1, -1, 8, -1, 32, 10, 19, -1, -1, -1, -1, 35, -1, 46, 3, 34, -1, 30, 16, -1, 14, -1, 24, -1, 17, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1],  # Input 5
        [28, -1, 4, 42, 40, 39, 2, 24, 41, -1, -1, -1, -1, -1, 17, 15, 37, 45, 18, -1, 33, 43, 35, -1, -1, 23, -1, -1, -1, -1, -1, -1, 30, 12, -1, -1, -1, -1, 47, 7, -1, -1, 32, -1, -1],  # Input 6
        [9, 36, 1, -1, 43, 2, 44, -1, 33, 27, 23, 29, 39, -1, -1, -1, -1, -1, -1, 20, 16, 42, -1, -1, 10, 21, 22, 3, -1, 34, -1, -1, -1, -1, -1, -1, -1, -1, 15, 7, -1, -1, 11, -1, -1],  # Input 7
        [25, 36, 40, -1, 29, 44, 46, 24, 7, 28, 27, 8, 17, -1, 13, -1, 12, 32, 35, 11, -1, -1, -1, -1, -1, 3, -1, -1, -1, 9, -1, -1, -1, 33, -1, -1, 15, -1, -1, -1, -1, 42, -1, -1, -1],  # Input 8
        [12, 9, 26, 21, 2, 1, 19, 8, 37, -1, -1, -1, 47, 27, 17, 4, -1, 16, -1, -1, -1, 42, -1, 3, 44, 5, 7, -1, -1, -1, 30, -1, -1, -1, -1, 41, -1, -1, -1, 13, -1, -1, -1, -1, -1],  # Input 9
        [31, -1, 32, 1, 21, 5, -1, -1, -1, 30, 33, 22, 26, -1, -1, -1, -1, 11, -1, -1, -1],  # Input 10
        [4, 43, 77, 9, 60, 49, 45, 40, 39, -1, 26, 71, -1, 22, 10, -1, 31, 12, -1, 1, 56, 41, 74, 7, 88, 92, -1, -1, 70, 48, 11, -1, -1, 66, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, 91, 3, 32, 65, 20, 73, 44, -1, -1, -1, 90, -1, 5, -1, -1, -1, 2, 50, 51, 76, 93, 59, 84, 85, 46, 69, -1, -1, 87, -1, 38, 14, -1, -1, 89, 17, 34, -1, -1, -1, -1, -1, -1, 36, -1, 82, 8, 16, -1, 79, -1, 13, -1, 63, 33, -1, 75, -1, -1, -1, -1, -1, -1, -1, 28, 94, 35, 80, -1, -1, -1, -1, -1, -1, -1, 27, -1, 58, -1, -1, -1, -1, -1, -1, 78, -1, -1, -1, 30, -1, -1, -1, -1, -1],  # Input 11
        [3, 49, 61, 30, 20, 53, 48, -1, 13, 15, 60, -1, -1, 25, -1, -1, 1, 51, 50, 38, 24, -1, -1, 58, 43, -1, -1, -1, -1, -1, -1, 37, 31, 9, 64, 26, 17, 36, 67, -1, -1, 59, -1, -1, -1, 57, 55, -1, -1, 22, 42, -1, -1, 11, -1, -1, -1, -1, 6, -1, 10, 21, 45, -1, -1, -1, 7, -1, -1, 32, 66, -1, -1, -1, -1, -1, 40, -1, -1, 23, 4, -1, 27, -1, -1, -1, -1],
        [70, 36, 58, 30, 68, 55, 41, 90, 32, 93, 31, 67, 10, -1, -1, -1, 39, 22, 52, 29, 6, -1, 17, 75, -1, 76, -1, 82, 88, 54, -1, 77, 65, -1, 57, 60, 4, -1, -1, 69, -1, 7, 94, 53, 14, 48, -1, 87, 24, 5, 80, 2, 79, -1, -1, -1, -1, 43, 18, -1, -1, 25, -1, -1, 44, -1, -1, 13, 16, 91, -1, 1, 96, -1, -1, 15, 56, -1, -1, 37, -1, -1, 9, 74, -1, -1, -1, -1, -1, -1, -1, -1, -1, 34, -1, -1, 63, 61, 40, -1, 81, 92, -1, 89, 38, -1, 23, -1, 97, -1, -1, 47, -1, -1, -1, -1, -1, 59, 8, -1, -1, -1, -1, -1, 73, 28, -1, 45, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1],
        [16, 95, 34, 29, 6, 68, 67, 86, 45, 14, 27, 87, 31, -1, 51, -1, 1, 5, 36, 12, 38, -1, -1, -1, 91, -1, 3, -1, 85, -1, 21, -1, 63, 83, -1, 76, 78, 10, -1, 26, -1, 57, -1, 56, 23, -1, 89, -1, -1, 80, 13, -1, 53, -1, 93, 81, 20, 62, -1, -1, -1, 41, 64, 77, -1, -1, 71, 55, -1, -1, 8, -1, 59, 74, -1, 4, 33, 37, 79, -1, 46, 82, 52, 50, -1, -1, -1, 44, -1, -1, 39, -1, -1, 70, -1, -1, -1, -1, -1, -1, -1, -1, 30, 49, -1, 60, -1, 73, 25, 84, 32, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 66, 17, -1, -1, -1, -1, -1, -1, -1, -1, 58, 65, -1, -1, -1, -1, -1, -1, -1, -1]
    ]
    
    for case in test_cases:
        try:
            # Tree construction
            root = LevelOrderTreeConstructor.build_tree(case.copy())
            
            # Tree analysis
            print(f"Input: {case}")
            print(f"Depth: {LevelOrderTreeConstructor.max_depth(root)}")
            print(f"Balanced: {LevelOrderTreeConstructor.is_balanced_tree(root)}")
            print(f"Diameter: {tree_diameter(root)}\n")
        
        except Exception as e:
            print(f"Error processing case {case}: {e}")

# Uncomment for testing
if __name__ == "__main__":
    main()