import collections

def treelevelprint(tree):

  nodes = collections.deque([tree])

  currentCount, nextCount = 1, 0

  while len(nodes) != 0:

    currentNode = nodes.popleft()

    currentCount-=1

    print (currentNode.val)

    if currentNode.left:

      nodes.append(currentNode.left)

      nextCount+=1

    if currentNode.right:

      nodes.append(currentNode.right)

      nextCount+=1

    if currentCount == 0:

      print ('\n')

      currentCount, nextCount = nextCount, currentCount  