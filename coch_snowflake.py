import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_snowflake(order, size):
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    t.hideturtle()
    window.mainloop()

def main():
    level_of_recursion = int(input("Enter the level of recursion for the Koch snowflake: "))
    size = 300  # Розмір можна налаштувати
    draw_snowflake(level_of_recursion, size)

if __name__ == "__main__":
    main()
