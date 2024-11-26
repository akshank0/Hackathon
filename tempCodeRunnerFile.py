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