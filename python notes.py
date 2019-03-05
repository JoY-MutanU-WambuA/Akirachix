Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> c='dog'
>>> d='cat'
>>> e=a/3
>>> a
10
>>> b
20
>>> c
'dog'
>>> d
'cat'
>>> e
3.3333333333333335
>>> f=str(a)
>>> f
'10'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(c)
<class 'str'>
>>> type(d)
<class 'str'>
>>> type(e)
<class 'float'>
>>> type(f)
<class 'str'>
>>> print('hello akirachix')
hello akirachix
>>> print('Hello Akirachix.\n class of 2019.')
Hello Akirachix.
 class of 2019.
>>> print('Hello Akirachix.\t class of 2019.')
Hello Akirachix.	 class of 2019.
>>> print('Hello Akirachix.\b class of 2019.')
Hello Akirachix. class of 2019.
>>> first='joy'
>>> last='mutanu'
>>> greeting='Hello,{} {}'.format(first,last)
>>> print(greeting)
Hello,joy mutanu
>>> code='ABC123'
>>> amount=1000
>>> recipient='07210000'
>>> print('code' confirmed! 'Hi,{} {}'.format(first,last)\n you have sent ksh 'amount' to 'recipient'
	  
SyntaxError: invalid syntax
>>> print('code' confirmed! 'Hi,{} {}'.format(first,last)\n you have sent ksh 'amount' to 'recipient'
	  
SyntaxError: invalid syntax
>>> print('code' 'confirmed!' 'Hi,{} {}'.format(first,last)\n you have sent ksh 'amount' to 'recipient'
	  
SyntaxError: unexpected character after line continuation character
>>> print('code' confirmed! 'Hi,{} {}'.format(first,last)\n you have sent ksh 'amount' to 'recipient')
	  
SyntaxError: invalid syntax
>>> 
