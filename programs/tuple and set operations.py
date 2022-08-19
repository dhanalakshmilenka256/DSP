Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(1,2,3,4)
>>> type(t)
<class 'tuple'>
>>> help(t)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
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
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
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
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> t
(1, 2, 3, 4)
>>> t[0]=10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t[0]=10
TypeError: 'tuple' object does not support item assignment
>>> x=list(t)
>>> type(t)
<class 'tuple'>
>>> type(x)
<class 'list'>
>>> x[0]=80
>>> x
[80, 2, 3, 4]
>>> print(t)
(1, 2, 3, 4)
>>> t=tuple(x)
>>> print(t)
(80, 2, 3, 4)
>>> s1={1,2,3}
>>> s2={3,4,5}
>>> s1
{1, 2, 3}
>>> s2
{3, 4, 5}
>>> type(s1)
<class 'set'>
>>> help(s1)
Help on set object:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
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
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
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
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
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

>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> s1.intersection(s2)
{3}
>>> s1.difference(S2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s1.difference(S2)
NameError: name 'S2' is not defined
>>> s1.difference(s2)
{1, 2}
>>> s1.update({6,7,8})
>>> s1
{1, 2, 3, 6, 7, 8}
>>> s1.difference_update(s2)
>>> s1
{1, 2, 6, 7, 8}
>>> s1.difference(S2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1.difference(S2)
NameError: name 'S2' is not defined
>>> s1.difference(s2)
{1, 2, 6, 7, 8}
>>> 1 in s1
True
>>> 2 not in s2
True
>>> 2 not in s1
False
>>> len(s1)
5
>>> sizeof(s1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sizeof(s1)
NameError: name 'sizeof' is not defined
>>> s1.remove(2)
>>> s1
{1, 6, 7, 8}
>>> s1.add(5)
>>> s1
{1, 5, 6, 7, 8}
>>> s1.discard(6)
>>> s1
{1, 5, 7, 8}
>>> s1.pop()
1
>>> s1
{5, 7, 8}
>>> s1.pop(8)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s1.pop(8)
TypeError: pop() takes no arguments (1 given)
>>> s={1,2,3,5,7,8}
>>> s.issubset(s1)
False
>>> s.issuperset(s1)
True
>>> s1.isdisjoint()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s1.isdisjoint()
TypeError: isdisjoint() takes exactly one argument (0 given)
>>> s3=s1.copy()
>>> s3
{8, 5, 7}
>>> s1.clear()
>>> s1
set()
>>> s1.disjoint(s)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s1.disjoint(s)
AttributeError: 'set' object has no attribute 'disjoint'
>>> s1.isdisjoint(s2)
True
>>> s1.update({1,2,3})
>>> s1.intersection_update(s2)
>>> s1
{3}
>>> s1
{3}
>>> s2
{3, 4, 5}
>>> s
{1, 2, 3, 5, 7, 8}
>>> s1.symmetricdifference(s2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s1.symmetricdifference(s2)
AttributeError: 'set' object has no attribute 'symmetricdifference'
>>> s1.symmetric_difference(s2)
{4, 5}
>>> s2.symmetric_difference(s1)
{4, 5}
>>> t=(1,2,3,4,5)
>>> x=list(t)
>>> x.add(6)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    x.add(6)
AttributeError: 'list' object has no attribute 'add'
>>> t.add(6)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t.add(6)
AttributeError: 'tuple' object has no attribute 'add'
>>> x.insert(6)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x.insert(6)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> x.insert(1,6)
>>> x
[1, 6, 2, 3, 4, 5]
>>> t.count(2)
1
>>> len(t)
5
>>> 1 in t
True
>>> 7 not in t
True
>>> min(t)
1
>>> max(t)
5
>>> sum(t)
15
>>> t.index(2)
1


