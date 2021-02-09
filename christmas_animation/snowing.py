import arcade
import random

width = 600
height = 400

# create all the snowflakes
snowflakes = []
for i in range(100):
    snowflake_x = random.randint(0, width)
    snowflake_y = random.randint(0, height)
    snowflakes.append([snowflake_x, snowflake_y])


def draw_our_snowflakes(deltatime):
    # global snowflake_y
    arcade.start_render()

    for snowflake in snowflakes:
        # take out the x and y coordinates
        snowflake_x = snowflake[0]
        snowflake_y = snowflake[1]
        # draw the snowflake
        arcade.draw_circle_filled(snowflake_x, snowflake_y, 3, arcade.color.WHITE, 5)
        # move the snowflake
        snowflake[1] -= 0.5
        if snowflake[1] < 0:
            snowflake[1] = height

    arcade.finish_render()


arcade.open_window(width, height, "Snowfall animation")
arcade.set_background_color(arcade.color.BLACK)
arcade.schedule(draw_our_snowflakes, 1 / 60)
arcade.run()

