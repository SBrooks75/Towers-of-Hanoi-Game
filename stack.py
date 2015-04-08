ass Stack:
    def __init__(self):
            self.items = []   
	        def isEmpty(self):
		        return self.items == []
			    def push(self,item):
			            self.items.append(item)   
				        def pop(self):  #Note the overloading of pop()
					        return self.items.pop() #pops the last item
						    # pop() will cause an error if the stack is empty before
						        # attempting to pop. 
							    def peek(self):
							            return self.items[len(self.items) -1]
								        def size(self):
									        return len(self.items)
