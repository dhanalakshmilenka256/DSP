Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4]
>>> print(l)
[1, 2, 3, 4]
>>> print(l[2])
3
>>> print(l[1:3])
[2, 3]
>>> print([:3])
SyntaxError: invalid syntax
>>> print(l[:3])
[1, 2, 3]
>>> print(l[1:])
[2, 3, 4]
>>> type(l)
<class 'list'>
>>> help(l)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> l1=l+[5,6,7]
>>> l1
[1, 2, 3, 4, 5, 6, 7]
>>> l[0]=100
>>> l
[100, 2, 3, 4]
>>> l1
[1, 2, 3, 4, 5, 6, 7]
>>> l=l1
>>> l
[1, 2, 3, 4, 5, 6, 7]
>>> l[0]=100
>>> l
[100, 2, 3, 4, 5, 6, 7]
>>> print(l)
[100, 2, 3, 4, 5, 6, 7]
>>> len(l)
7
>>> l[1:4]=(123,45,76)
>>> l
[100, 123, 45, 76, 5, 6, 7]
>>> l.insert(3,789)
>>> l
[100, 123, 45, 789, 76, 5, 6, 7]
>>> l.extend([44,55,66])
>>> l
[100, 123, 45, 789, 76, 5, 6, 7, 44, 55, 66]
>>> l.append([3,45,6])
>>> l
[100, 123, 45, 789, 76, 5, 6, 7, 44, 55, 66, [3, 45, 6]]
>>> del(l[9])
>>> l
[100, 123, 45, 789, 76, 5, 6, 7, 44, 66, [3, 45, 6]]
>>> l.pop()
[3, 45, 6]
>>> l
[100, 123, 45, 789, 76, 5, 6, 7, 44, 66]
>>> l.remove(44)
>>> l
[100, 123, 45, 789, 76, 5, 6, 7, 66]
>>> del(l[-3])
>>> l
[100, 123, 45, 789, 76, 5, 7, 66]
>>> l.sort()
>>> l
[5, 7, 45, 66, 76, 100, 123, 789]
>>> l.sort(reverse=True)
>>> l
[789, 123, 100, 76, 66, 45, 7, 5]
>>> l.reverse()
>>> l
[5, 7, 45, 66, 76, 100, 123, 789]
>>> l[o]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l[o]
NameError: name 'o' is not defined
>>> l[0]
5
>>> l[-1]
789
>>> l.reverse()
>>> l[0]
789
>>> l[-1]
5
>>> l1=l
>>> l1[4]=100
>>> l
[789, 123, 100, 76, 100, 45, 7, 5]
>>> l1
[789, 123, 100, 76, 100, 45, 7, 5]
>>> l2=l1.copy()
>>> l2
[789, 123, 100, 76, 100, 45, 7, 5]
>>> l2[0]=90
>>> l2
[90, 123, 100, 76, 100, 45, 7, 5]
>>> l1
[789, 123, 100, 76, 100, 45, 7, 5]
>>> l
[789, 123, 100, 76, 100, 45, 7, 5]
>>> l.replace(76,80)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    l.replace(76,80)
AttributeError: 'list' object has no attribute 'replace'
>>> l.count(100)
2
>>> 
