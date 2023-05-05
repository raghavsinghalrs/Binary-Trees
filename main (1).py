class BST:
  
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None
    
  def insert(self,val):
    if self.val is None:
      self.val = val 
      return

    if self.val>val:
      if self.left:
        self.left.insert(val)
      else:
        self.left = BST(val)
    else:
      if self.right:
        self.right.insert(val)
      else:
        self.right =BST(val)
  def search(self,val):
    if self.val==val:
      print('You got your node!')
      return
    if self.val>val:
      if self.left:
        self.left.search(val)
      else:
        print('Sorry, Data is not exist!')
    else:
      if self.right:
        self.right.search(val)
      else:
        print('Sorry, Data is not exist!')
  """PreOrder Traveral root->left->right"""
  def POT(self):
    print(self.val)
    if self.left:
      self.left.POT()
    if self.right:
      self.right.POT()
root = BST(10)
lst = [20,4,9,5,7,22,3]
for i in lst:
  root.insert(i)
root.POT()