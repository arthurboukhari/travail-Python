class carre:
	def __init__(self, cote, perimeter, area):
		self.cote = cote
		self.perimeter = self.cote*4
		self.area = self.cote * self.cote
		

if __name__ == "__main__":
	a=int(input())
	t = carre(a,0,0)
	print(t.cote)
	print(t.perimeter)
	print(t.area)
	print("Le carré à un côté d'une longueur de", t.cote, "une aire de", t.area ,"cm² et un périmètre de", t.perimeter ,"cm².")
	print()



class carre2:
	def __init__(self, cote2, perimeter2, area2):
		self.cote2 = cote2
		self.perimeter2 = self.cote2*4
		self.area2 = self.cote2 * self.cote2
		

if __name__ == "__main__":
	a=int(input())
	r = carre2(a,0,0)
	print(r.cote2)
	print(r.perimeter2)
	print(r.area2)
	print("Le carré à un côté d'une longueur de", r.cote2, "une aire de", r.area2 ,"cm² et un périmètre de", r.perimeter2 ,"cm².")

print(t.perimeter + r.perimeter2)

if t.perimeter < r.perimeter2:
	print("True")
else:
	print("False")