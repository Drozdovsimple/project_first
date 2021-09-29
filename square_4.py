import turtle as tl

x = 20
for step in range(5):
    tl.forward(x)
    tl.right(90)
    tl.forward(x)
    tl.right(90)
    tl.forward(x)
    tl.right(90)
    tl.forward(x)
    tl.right(90)
    x += 10
tl.done()
