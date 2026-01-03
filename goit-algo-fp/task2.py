import turtle

def draw_tree(t, length, level):
    if level == 0:
        return

    # Малюємо гілку
    t.forward(length)
    
    # Поворот направо
    t.right(45)
    draw_tree(t, length * 0.7, level - 1)
    
    # Поворот наліво
    t.left(90)
    draw_tree(t, length * 0.7, level - 1)
    
    # Повертаємось у вихідну точку
    t.right(45)
    t.backward(length)

level = int(input("Введіть рівень рекурсії: "))

t = turtle.Turtle()
t.speed(0) 
t.left(90)
t.up()
t.goto(0, -200)
t.down()
t.color("brown")

draw_tree(t, 100, level)

turtle.exitonclick()