def trimBST(tree, minval, maxval):

  if not tree:

    return None

  tree.left = trimBST(tree.left, minval, maxval)

  tree.right = trimBST(tree.right, minval, maxval)

  if minval<=tree.val<=maxval:

    return tree

  if tree.val<minval:

    return tree.right

  if tree.val>maxval:

    return tree.left