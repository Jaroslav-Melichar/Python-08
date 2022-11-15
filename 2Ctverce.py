import turtle 
t = turtle.Turtle()
t.shape('turtle')
print("čtverec ve čtverci")
for cycle in range(4):
    t.forward(100)
    t.left(90)
    for cycle in range(4):
        t.forward(50)
        t.left(90)  