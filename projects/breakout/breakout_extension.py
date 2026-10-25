"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Pre-condition: 3 objects: bricks, ball and paddle.
Users hover the mouse to move paddles
When the ball hits the paddle, it will bounce back
When the ball hits the brick, it will disappear
Post-condition:
when all the bricks disappear, end the game
when the ball misses the paddle for 3 times or above, end the game
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball = graphics.ball
    window = graphics.window
    live = NUM_LIVES
    num_of_bricks = graphics.num_of_bricks
    # Add the animation loop here!
    while True:
        if live == 0 or graphics.score == num_of_bricks:
            break
        else:
            # update
            graphics.check_collisions()
            ball.move(graphics.dx, graphics.dy)
            graphics.move_item()
            # check
            if ball.x <= 0 or ball.x + ball.width >= window.width:
                graphics.dx = -graphics.dx
            if ball.y <= 0:
                graphics.dy = -graphics.dy
            if ball.y + ball.height >= window.height:
                graphics.reset()
                live -= 1
        # pause
        pause(FRAME_RATE)
    if live == 0:
        graphics.lose()
    else:
        graphics.win()


if __name__ == '__main__':
    main()
