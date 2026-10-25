"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

class BreakoutGraphics constructs 4 objects: bricks, ball paddle, and window
and 5 methods hover_paddle, trigger_ball, create_brick, check_collisions, and reset

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, ball_size=BALL_RADIUS * 2,
                 paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self._window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._window.add(self._paddle, x=(self._window.width - self._paddle.width) / 2,
                         y=self._window.height - self._paddle.height - paddle_offset)
        self._paddle.color = 'black'
        self._paddle.filled = True
        self._paddle.fill_color = 'black'
        # Center a filled ball in the graphical window
        self._ball = GOval(ball_size, ball_size)
        self._window.add(self._ball, x=(self._window.width - self._ball.width) / 2,
                         y=(self._window.height - self._ball.height) / 2)
        self._ball.filled = True
        self._ball.fill_color = 'black'
        self._ball_size = ball_size
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.hover_paddle)
        onmouseclicked(self.trigger_ball)
        # Draw bricks
        self._brick_width = brick_width
        self._brick_height = brick_height
        self.create_brick()
        self._num_of_bricks = brick_rows * brick_cols
        # Create a score
        self._score = 0

    """
    Move the paddle when the mouse hovers
    """

    def hover_paddle(self, mouse):
        if mouse.x - (PADDLE_WIDTH / 2) < 0:  # leftmost of the paddle
            self._paddle.x = 0
        elif (mouse.x + PADDLE_WIDTH / 2) > self._window.width:  # rightmost of the paddle
            self._paddle.x = self._window.width - PADDLE_WIDTH
        else:
            self._paddle.x = mouse.x - (PADDLE_WIDTH / 2)

    """
    Trigger the ball to move on mouse click when the ball is at the starting position
    Randomize horizontal movements via dx.
    """

    def trigger_ball(self, mouse):
        if self.__dy == 0:  # When the ball is at the starting position and not moving
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = self.__dx * -1
            self.__dy = INITIAL_Y_SPEED

    # Create, arrange and color multiple bricks based on BRICK_ROWS and BRICK_COLS
    def create_brick(self):
        brick_y = BRICK_OFFSET  # 50
        for i in range(BRICK_ROWS):  # i: 0, 1, 2, 3, ... , 9
            brick_x = 0
            for j in range(BRICK_COLS):  # j: 0, 1, 2, 3, ..., 9
                brick = GRect(self._brick_width, self._brick_height)
                self._window.add(brick, x=brick_x, y=brick_y)
                brick_x += (self._brick_width + BRICK_SPACING)  # row 1: (0, 50), (45, 50), (90, 50), ...(405, 50)
                brick.filled = True
                if i // 2 % 5 == 0:
                    brick.color = 'red'
                    brick.fill_color = 'red'
                elif i // 2 % 5 == 1:
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                elif i // 2 % 5 == 2:
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                elif i // 2 % 5 == 3:
                    brick.color = 'green'
                    brick.fill_color = 'green'
                else:
                    brick.color = 'blue'
                    brick.fill_color = 'blue'
            brick_y += (self._brick_height + BRICK_SPACING)  # row 2: (0, 70), (45, 70), (90, 70), ...(405, 70)

    """
    As the ball moves, check if the vertex of the ball hit the paddle or any bricks. 
    If the ball hits the paddle, change dy to -dy.
    If the ball hits a brick, change dy to -dy and remove the brick.
    """

    def check_collisions(self):
        vertex_1 = self._window.get_object_at(self._ball.x, self._ball.y)
        vertex_2 = self._window.get_object_at(self._ball.x + self._ball_size, self._ball.y)
        vertex_3 = self._window.get_object_at(self._ball.x, self._ball.y + self._ball_size)
        vertex_4 = self._window.get_object_at(self._ball.x + self._ball_size, self._ball.y + self._ball_size)
        for vertex in (vertex_1, vertex_2, vertex_3, vertex_4):
            if vertex is not None:
                if vertex is self._paddle:
                    if self.__dy > 0:
                        self.__dy = self.__dy * -1
                else:
                    self.__dy = self.__dy * -1
                    self._window.remove(vertex)
                    self._score += 1
                break

    """
    Reset the ball at the center of the window when the ball hits the bottom of the window.
    """

    def reset(self):
        self._ball.x = (self._window.width - self._ball.width) / 2
        self._ball.y = (self._window.height - self._ball.height) / 2
        self.__dx = 0
        self.__dy = 0

    @property
    def ball(self):
        return self._ball

    @property
    def window(self):
        return self._window

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    @property
    def score(self):
        return self._score

    @property
    def num_of_bricks(self):
        return self._num_of_bricks

    @dx.setter
    def dx(self, new_dx):
        self.__dx = new_dx

    @dy.setter
    def dy(self, new_dy):
        self.__dy = new_dy
