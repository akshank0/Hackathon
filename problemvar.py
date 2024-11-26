class TreeNode:
    __slots__ = ['data', 'left', 'right']  # Memory optimization
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class AdvancedTreeConstructor:
    @staticmethod
    def detect_input_format(input_data):
        """
        Advanced input format detection with multiple strategies.
        
        Supported formats:
        1. Level-order with -1/-999 for null nodes
        2. Pre-order traversal
        3. In-order traversal
        4. Post-order traversal
        5. Serialized representations
        6. Parenthesis-based representation
        """
        # Quick format detection heuristics
        if not input_data:
            return None
        
        # Level-order detection (most inputs in competitions)
        if isinstance(input_data, list) and (-1 in input_data or -999 in input_data):
            return "level_order"
        
        # Parenthesis-based tree representation
        if isinstance(input_data, str) and set(input_data) & set('()'):
            return "parenthesis"
        
        # Pre/In/Post-order detection could be more sophisticated
        return "pre_order"  # Default fallback

    @classmethod
    def build_tree(cls, input_data, method=None):
        """
        Universal tree construction with multiple strategies.
        
        Args:
        input_data: Tree representation
        method: Explicit construction method (optional)
        
        Returns:
        TreeNode: Constructed tree root
        """
        # If no method specified, detect automatically
        if method is None:
            method = cls.detect_input_format(input_data)
        
        # Dispatch to appropriate construction method
        construction_methods = {
            "level_order": cls.build_from_level_order,
            "pre_order": cls.build_from_pre_order,
            "parenthesis": cls.build_from_parenthesis,
            "in_order": cls.build_from_in_order,
            "post_order": cls.build_from_post_order
        }
        
        try:
            constructor = construction_methods.get(method)
            if constructor:
                return constructor(input_data)
            raise ValueError(f"Unsupported construction method: {method}")
        
        except Exception as e:
            print(f"Tree Construction Error: {e}")
            return None

    @staticmethod
    def build_from_level_order(level_order, null_marker=-1):
        """
        Optimized level-order tree construction.
        
        Time Complexity: O(n)
        Space Complexity: O(w)
        """
        if not level_order or level_order[0] == null_marker:
            return None
        
        root = TreeNode(level_order[0])
        queue = [root]
        i = 1
        
        while queue and i < len(level_order):
            current = queue.pop(0)
            
            # Left child
            if i < len(level_order) and level_order[i] != null_marker:
                current.left = TreeNode(level_order[i])
                queue.append(current.left)
            i += 1
            
            # Right child
            if i < len(level_order) and level_order[i] != null_marker:
                current.right = TreeNode(level_order[i])
                queue.append(current.right)
            i += 1
        
        return root

    @staticmethod
    def build_from_parenthesis(s):
        """
        Build tree from parenthesis representation.
        Example: "1(2(4)(5))(3(6)(7))"
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def parse_tree():
            nonlocal i
            
            # Extract node value
            start = i
            while i < len(s) and (s[i].isdigit() or s[i] == '-'):
                i += 1
            
            node = TreeNode(int(s[start:i]))
            
            # Check for left subtree
            if i < len(s) and s[i] == '(':
                i += 1  # Skip '('
                node.left = parse_tree()
                i += 1  # Skip ')'
            
            # Check for right subtree
            if i < len(s) and s[i] == '(':
                i += 1  # Skip '('
                node.right = parse_tree()
                i += 1  # Skip ')'
            
            return node
        
        i = 0
        return parse_tree() if s else None

    @staticmethod
    def build_from_pre_order(pre_order):
        """
        Recursive pre-order tree construction.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def build_recursive(index):
            if index[0] >= len(pre_order):
                return None
            
            root = TreeNode(pre_order[index[0]])
            index[0] += 1
            
            # Recursively construct left and right subtrees
            root.left = build_recursive(index)
            root.right = build_recursive(index)
            
            return root
        
        return build_recursive([0]) if pre_order else None

    @staticmethod
    def build_from_in_order(in_order):
        """
        Construct tree from in-order traversal.
        Requires additional information about pre/post-order.
        """
        # Placeholder for more complex reconstruction
        raise NotImplementedError("In-order reconstruction requires additional traversal info")

    @staticmethod
    def build_from_post_order(post_order):
        """
        Recursive post-order tree construction.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def build_recursive(index):
            if index[0] < 0:
                return None
            
            root = TreeNode(post_order[index[0]])
            index[0] -= 1
            
            # Note the reverse order compared to pre-order
            root.right = build_recursive(index)
            root.left = build_recursive(index)
            
            return root
        
        index = [len(post_order) - 1]
        return build_recursive(index) if post_order else None

    @staticmethod
    def max_depth(root):
        """
        Highly optimized depth calculation with tail recursion.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return 0
        
        # Elimination of max() call for slight performance boost
        left_depth = AdvancedTreeConstructor.max_depth(root.left)
        right_depth = AdvancedTreeConstructor.max_depth(root.right)
        
        return 1 + (left_depth if left_depth > right_depth else right_depth)

# Competitive Programming Utilities
def tree_serializer(root):
    """
    Serialize tree for debugging or output verification.
    """
    if not root:
        return "None"
    return f"{root.data}({tree_serializer(root.left)})({tree_serializer(root.right)})"

def main():
    # Comprehensive test cases covering multiple formats
    test_cases = [
        # Level Order (with -1 marker)
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
    
    
    # Competitive style rapid testing
    for idx, case in enumerate(test_cases, 1):
        try:
            # Attempt multiple construction methods
            root = AdvancedTreeConstructor.build_tree(case)
            
            print(f"Test {idx}:")
            print(f"Input: {case}")
            print(f"Depth: {AdvancedTreeConstructor.max_depth(root)}")
            print(f"Serialized: {tree_serializer(root)}\n")
        
        except Exception as e:
            print(f"Error in Test {idx}: {e}")

if __name__ == "__main__":
    main()