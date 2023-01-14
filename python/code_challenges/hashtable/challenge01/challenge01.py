def TwoSumBST( root, k):

        def helper(root, hashSet):

            if root == None:
                return False

            complement = k - root.value

            if complement in hashSet: 
                return True

            hashSet.add(root.value)

            return helper(root.left, hashSet) or helper(root.right, hashSet)
        
        return helper(root, set())