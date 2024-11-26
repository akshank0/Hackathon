class TreeNode:
    __slots__ = ['data', 'left', 'right']
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class AdvancedTreeConstructor:
    @staticmethod
    def detect_input_format(input_data):
        if not input_data:
            return None
        
        if isinstance(input_data, list) and (-1 in input_data or -999 in input_data):
            return "level_order"
        
        if isinstance(input_data, str) and set(input_data) & set('()'):
            return "parenthesis"
        
        return "pre_order"

    @classmethod
    def build_tree(cls, input_data, method=None):
        if method is None:
            method = cls.detect_input_format(input_data)
        
        construction_methods = {
            "level_order": cls.build_from_level_order,
            "pre_order": cls.build_from_pre_order,
            "parenthesis": cls.build_from_parenthesis,
            "post_order": cls.build_from_post_order
        }
        
        constructor = construction_methods.get(method)
        if constructor:
            return constructor(input_data)
        raise ValueError(f"Unsupported construction method: {method}")

    @staticmethod
    def build_from_level_order(level_order, null_marker=-1):
        if not level_order or level_order[0] == null_marker:
            return None
        
        root = TreeNode(level_order[0])
        queue = [root]
        i = 1
        
        while queue and i < len(level_order):
            current = queue.pop(0)
            
            if i < len(level_order) and level_order[i] != null_marker:
                current.left = TreeNode(level_order[i])
                queue.append(current.left)
            i += 1
            
            if i < len(level_order) and level_order[i] != null_marker:
                current.right = TreeNode(level_order[i])
                queue.append(current.right)
            i += 1
        
        return root

    @staticmethod
    def build_from_parenthesis(s):
        def parse_tree():
            nonlocal i
            
            start = i
            while i < len(s) and (s[i].isdigit() or s[i] == '-'):
                i += 1
            
            node = TreeNode(int(s[start:i]))
            
            if i < len(s) and s[i] == '(':
                i += 1
                node.left = parse_tree()
                i += 1
            
            if i < len(s) and s[i] == '(':
                i += 1
                node.right = parse_tree()
                i += 1
            
            return node
        
        i = 0
        return parse_tree() if s else None

    @staticmethod
    def build_from_pre_order(pre_order):
        def build_recursive(index):
            if index[0] >= len(pre_order):
                return None
            
            root = TreeNode(pre_order[index[0]])
            index[0] += 1
            
            root.left = build_recursive(index)
            root.right = build_recursive(index)
            
            return root
        
        return build_recursive([0]) if pre_order else None

    @staticmethod
    def build_from_post_order(post_order):
        def build_recursive(index):
            if index[0] < 0:
                return None
            
            root = TreeNode(post_order[index[0]])
            index[0] -= 1
            
            root.right = build_recursive(index)
            root.left = build_recursive(index)
            
            return root
        
        index = [len(post_order) - 1]
        return build_recursive(index) if post_order else None

    @staticmethod
    def max_depth(root):
        if not root:
            return 0
        
        left_depth = AdvancedTreeConstructor.max_depth(root.left)
        right_depth = AdvancedTreeConstructor.max_depth(root.right)
        
        return 1 + (left_depth if left_depth > right_depth else right_depth)