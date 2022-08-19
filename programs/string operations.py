Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="rgukt"
>>> x.upper()
'RGUKT'
>>> x.lower()
'rgukt'
>>> x.capitalize()
'Rgukt'
>>> x.isupper()
False
>>> x.find('a')
-1
>>> x.find('k')
3
>>> x[1:4]
'guk'
>>> x[-1:-3]
''
>>> y="sklm"
>>> x+y
'rguktsklm'
>>> x.join(y)
'srguktkrguktlrguktm'
>>> y.join(x)
'rsklmgsklmusklmksklmt'
>>> len(x)
5
>>> len(x+y)
9
>>> a="10"
>>> b="20"
>>> int(a)+int(b)
30
>>> a="data science with python"
>>> a.title()
'Data Science With Python'
>>> a.upper()
'DATA SCIENCE WITH PYTHON'
>>> print(a)
data science with python
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> a.replace('a','w')
'dwtw science with python'
>>> a.isalnum()
False
>>> a.isdigit()
False
>>> a.casefold()
'data science with python'
>>> a.encode()
b'data science with python'
>>> a.center('a')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.center('a')
TypeError: 'str' object cannot be interpreted as an integer
>>>a*2

