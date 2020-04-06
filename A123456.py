# Example AI Player Subclass

from aiplayer import AIPlayer


class A123456(AIPlayer):
	def __init__(self):
		MysuperClass.__init__(self)

class A20424772(A123456):
	def __init__(self):
		super(A20424772, self).__init__()
    """ Super Player
    """
    def __init__(self):
        AIPlayer.__init__(self, "A123456", "x", 4)

		
		""" 
""" class MySubClass(MySuperClass):
    def __init__(self):
        MySuperClass.__init__(self)

# Better initialize using Parent (less redundant).
#
class MySubClassBetter(MySuperClass):
    def __init__(self):
        super(MySubClassBetter, self).__init__()
       