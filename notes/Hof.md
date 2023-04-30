# command- line
* python3 -i script.py : -i interactive 
* python3 assert a > b, 'message'
* 

# 补充内容
# Fibonacci 
 0, 1, 1, 2, .。。 在0之前可以补一个1

# Hof 
## assert
```python
  def area(r, const):
      assert r > 0, 'A length must be positive'
	  return .. 

```
## functions as return values
* locally defined functions 

* Funcitons defined within other function bodies are bound to names in a local frame 
* it can refer to names in the enclosing function
```python 
def make_adder(n):
    def adder(k):
        return n + k
    return adder
```
### Functions are first-class
* funcitons can be manipulated as values in python
### Higher-order Function
* a function taht takes a funtion as an argument value or returns a function as a return value 
