class Dict(dict):
	def init(self, **kw):
		super().__init__(**kw)
		
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			pass
			#raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
			
	def __setattr__(self, key, value):
		self[key] = value

'''		
d = Dict(a=1, b=2)
print(d['a'])
print(d.a)
d.k = 156
print(d.k)
'''