# Implementing Basic Autograd Operations

# Special thanks to Andrej Karpathy for making a video about this, 
# if you haven't already check out his videos on 
# YouTube https://youtu.be/VMj-3S1tku0?si=gjlnFP4o3JRN9dTg. 
# Write a Python class similar to the provided 'Value' class that 
# implements the basic autograd operations: addition, multiplication, and ReLU activation. 
# The class should handle scalar values and should correctly compute gradients for these 
# operations through automatic differentiation.


class Value:
	def __init__(self, data, _children=(), _op=''):
		self.data = data
		self.grad = 0
		self._backward = lambda: None
		self._prev = set(_children)
		self._op = _op
	def __repr__(self):
		return f"Value(data={self.data}, grad={self.grad})"

	def __add__(self, other):
		 # Implement addition here
		out_add = self.data
		return out_add 

	def __mul__(self, other):
		# Implement multiplication here
		out_mul = self.data
		return out_mul

	def relu(self):
		# Implement ReLU here
		out_relu = self.data
		return out_relu

	def backward(self):
		# Implement backward pass here
		out_bck = self.grad
		return out_bck
	


# Example usage:
if __name__ == "__main__":
	a = Value(2)
	b = Value(-3)
	c = Value(10)
	d = a + b * c
	e = d.relu()
	e.backward()
	print(a, b, c, d, e)


#Expected result: Value(data=2, grad=0) Value(data=-3, grad=0) Value(data=10, grad=0)

