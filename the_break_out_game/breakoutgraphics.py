"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
CLICK_COUNTER = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width)/2, y= self.window.height - PADDLE_OFFSET - PADDLE_HEIGHT)
        # Center a filled ball in the graphical window
        self.ball = GOval(width=BALL_RADIUS * 2, height=BALL_RADIUS * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=(self.window.height - self.ball.height) / 2 )

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.ini_ball)

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT)
                self.brick.filled = True
                if j == 0 or j == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif j == 2 or j == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j == 4 or j == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j == 6 or j == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, x=0 + (BRICK_WIDTH + BRICK_SPACING) * i, y=BRICK_OFFSET + (BRICK_HEIGHT + BRICK_SPACING) * j)

    def move_paddle(self, mouse):
        self.paddle.x = mouse.x - self.paddle.x / 2
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if self.paddle.x <= 0:
            self.paddle.x = 0

    def ini_ball(self, mouse):
        global CLICK_COUNTER
        CLICK_COUNTER += 1
        if CLICK_COUNTER == 1:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx *= 1

    def set_dy(self):
        self.__dy *= -1

    def set_dx_1(self):
        self.__dx *= -1

    def reset_ball(self):
        global CLICK_COUNTER
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=(self.window.height - self.ball.height) / 2)
        self.__dx = 0
        self.__dy = 0
        CLICK_COUNTER = 0

    def get_color(self):
        return self.brick.fill_color

    def add_dx(self):
        self.__dx += 5

    def add_dy(self):
        self.__dy += 5
