
def first_target_element_index(targets, xs) -> int:
	for i, x in enumerate(xs):
		if type(x) is not int:
			raise TypeError(f'Encountered unexpected type {type(x)}, expected int') 
		if x in targets:
			print(f'X IS ==> {x}\nI IS --> {i}')
			return i
	return -1