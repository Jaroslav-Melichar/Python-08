import turtle 
t = turtle.Turtle()
t.shape('turtle')
print("jeden čtverec a přes něj bude čtverec na kosočtverec")
for cycle in range(4):
    t.forward(100)
    t.left(90)
print("kosočtverec")
for cycle in range(4):
    t.forward(50)
    t.left(135)