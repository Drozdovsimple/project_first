import turtle as tl

tl.shape('turtle')
tl.color('red', 'yellow')
tl.begin_fill()
for step in range(6):
    for i in range(3):
        tl.forward(30)
        tl.left(120)
    tl.forward(50)
    tl.right(60)
tl.end_fill()
tl.done()

