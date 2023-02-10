# Write your code here :-)
smile = Actor("smile")
smile.pos = 100, 50

WIDTH = 500

HEIGHT = smile.height + 30


def draw():
    screen.fill((255, 0, 0))
    smile.draw()


def update():
    smile.left + smile.left + 2
    if smile.left > WIDTH:
        smile.right = 0


def on_mouse_down(pos):
    if smile.collidepoint(pos):
        print("YIPP!")
    else:
        print("You missed me!")
    if smile.collidepoint(pos):
        sounds.hit.play()
        smile.image = "smile clicked"
