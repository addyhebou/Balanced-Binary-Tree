def is_height_balanced(bin_tree):
    if bin_tree is None:
        raise Exception("Tree is empty")
    return is_height_balanced_recurse(bin_tree.root)[0]
    def is_height_balanced_recurse(bin_tree):
        if (bin_tree.left is None and bin_tree.right is None): #trying to access the node here.
            return (True,1)
        elif (bin_tree.left is None and bin_tree.right is not None):
            height = is_height_balanced_recurse(bin_tree.right)
            if height[1] > 1:
                return (False, height[1]+1)
            else:
                return (height[0], height[1]+1)
        elif (bin_tree.right is None and bin_tree.left is not None):
            height = is_height_balanced_recurse(bin_tree.left)
            if height[1] > 1:
                return (False, height[1]+1)
            else:
                return (height[0], height[1]+1)
        else:
            height = is_height_balanced_recurse(bin_tree.right)
            height2 = is_height_balanced_recurse(bin_tree.left)
            comparison = abs(height[1] - height2[1])
            if comparison > 1:
                if height > height2:
                    return (False,height[1]+1)
                else:
                    return (False,height2[1]+1)
            else:
                if height[0] == False or height2[0] == False:
                    if height > height2:
                        return (False,height[1]+1)
                    else:
                        return (False,height2[1]+1)
                else:
                    if height > height2:
                        return (height[0],height[1]+1)
                    else:
                        return (height2[0],height2[1]+1)
