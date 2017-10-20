class Node:
	#constructor for the node class
	def __init__(self,val):
		self.left=None
		self.right=None
		self.val=val
#method to insert into our binary tree
def insert(root,item):
	#if the root is 
	if(root==None):
		root=Node(item)
		return
	else:
		if(root.val>item):
			if(root.left!=None):
				insert(root.left,item)
			else:
				root.left=Node(item)
		elif(root.val<item):
			if(root.right!=None):
				insert(root.right,item)
			else:
				root.right=Node(item)
#method to print our tree in in order fashion
def inOrder(root):
	if(root==None):
		return
	else:
		inOrder(root.left)
		print(root.val)
		#print(root.val, end=" ") for printing in one line
		inOrder(root.right)
#main function
def main():
	#menu driver
	print("Start inserting into the binary search tree")
	print("===================================================")
	print("Enter the root node:")
	tempRoot=input()
	root=Node(tempRoot)
	print("Do you want to enter more ?(Y for yes,n for No)")
	choice=input()
	if (choice=='Y' or choice=='y'):
		while True:
			print("Enter the item to insert:")
			item=input()
			insert(root,item)
			print("Item successfully inserted")
			print("==========================")
			print("Do you want to enter more ?(Y for yes,n for No)")
			choice=input()
			print("==========================")
			if(choice=='N'or choice=='n'):	
				break

	else:
		print("==========================")
		print("Thank You")
		print("==========================")
	print("Your tree is:")
	inOrder(root,0)
	print("==========================")		

main()
