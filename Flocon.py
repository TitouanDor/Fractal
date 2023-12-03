import turtle as Carol

def L(long : int, ordre : int) -> None:
    
    if ordre == 0:
        Carol.forward(long)
    else:
        L(long/3, ordre - 1)
        Carol.left(60)
        L(long/3, ordre - 1)
        Carol.right(120)
        L(long/3, ordre - 1)
        Carol.left(60)
        L(long/3, ordre - 1)

def flocon(long : int, unite : int, fois = 3) -> None:
    if fois == 0: return None
    else: 
        L(long, unite)
        Carol.right(120)
        flocon(long, unite, fois - 1)

def flocon_x_cote(long : int, unite : int, cote : int, nb_foix = 0) -> None:
    angle = 360/cote
    if (cote - nb_foix) == 0: return None
    else: 
        L(long, unite)
        Carol.right(angle)
        flocon_x_cote(long, unite, cote, nb_foix + 1)
    




Carol.pendown()
Carol.speed(0)
flocon_x_cote(150, 3, 10)
Carol.hideturtle()
a = input()