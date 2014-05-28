from LL import * 
def Solution():
	
	def hasCycle(self, node):
		SLOW = node
		FAST = node
		while 1:
			FAST = FAST.next 
			if FAST == None:
				print 'No Cycle'
				break
			FAST = FAST.next
			if FAST == None:
				print 'No Cycle'
				break
			SLOW = SLOW.next
			if SLOW == FAST:
				return 'Cycle Confirmed'
				break
