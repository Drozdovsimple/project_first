import turtle as tl

tl.shape('turtle')
tl.color('red', 'yellow')
tl.begin_fill()
for step in range(6):
    tl.forward(50)
    tl.right(60)
tl.end_fill()
tl.done()

