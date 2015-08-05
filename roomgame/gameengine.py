#coding:utf-8

class gameengine(object):
	"""game engine"""
	def __init__(self,roomsmap):
		self.roomsmap = roomsmap
		print "game engine init"
	def start(self):
		print "game engine start"
		self.roomsmap.next_room()

class room(object):
	"""room object"""
	def enter(self):
		print "room parent"
		exit(1)



class fail(room):
	def enter(self):
		print "you do not run after the girl"
		exit(1)

class comeacross(room):
	"""docstring for comeacross"""
	def enter(self):
		print "first you come across a girl who is beautiful,are you brave to have a date with her? "
		
		inputstring = raw_input("yes or no\n")
		if inputstring == "yes":
			return "date"
		else:
			return "fail"	


class date(room):
	"""docstring for comeacross"""
	def enter(self):
		print "after you come across you and date with her,can you invite her to watch a movie?"
		
		inputstring = raw_input("yes or no\n")
		if inputstring == "yes":
			return "movie"
		else:
			return "fail"

class movie(room):
	"""docstring for comeacross"""
	def enter(self):
		print "after movie,what should you do"
		
		inputstring = raw_input("dinner or home\n")
		if inputstring == "dinner":
			return "dinner"
		else:
			return "fail"


class dinner(room):
	"""docstring for comeacross"""
	def enter(self):
		print "after dinner,what should you do"
		
		inputstring = raw_input("send her home or go your home\n")
		if inputstring == "send her home":
			return "sendhome"
		else:
			return "fail"

class sendhome(room):
	"""docstring for comeacross"""
	def enter(self):
		print "after send her home,she is satisfied of you,and the result is fine"
		exit(1)


class roomsmap(object):
	rooms = {
		"comeacross":comeacross(),
		"date":date(),
		"movie":movie(),
		"dinner":dinner(),
		"sendhome":sendhome(),
	}

	"""game rooms"""
	def __init__(self, start_room):
		self.start_room = start_room
		print "you enter a new room"

	def next_room(self):
		while self.next_room!="fail":
			self.next_room = roomsmap.rooms.get(self.start_room).enter()
			self.start_room = self.next_room
		fail().enter()