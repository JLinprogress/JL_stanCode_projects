"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    global NUM_LIVES
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    while 0 < NUM_LIVES <= 3:
        # Pause
        pause(FRAME_RATE)
        # Update
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        # Check
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            graphics.set_dx_1()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        if graphics.ball.y > graphics.window.height:
            NUM_LIVES -= 1
            graphics.reset_ball()

        objects = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        if objects is not None:
            if objects is graphics.paddle:
                graphics.set_dx()
                if graphics.get_dy() > 0:
                    graphics.set_dy()
            else:
                graphics.set_dx()
                graphics.set_dy()
                graphics.window.remove(objects)
        else:
            objects = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
            if objects is not None:
                if objects is graphics.paddle:
                    graphics.set_dx()
                    if graphics.get_dy() > 0:
                        graphics.set_dy()
                else:
                    graphics.set_dx()
                    graphics.set_dy()
                    graphics.window.remove(objects)
            else:
                objects = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
                if objects is not None:
                    if objects is graphics.paddle:
                        graphics.set_dx()
                        if graphics.get_dy() > 0:
                            graphics.set_dy()
                    else:
                        graphics.set_dx()
                        graphics.set_dy()
                        graphics.window.remove(objects)
                else:
                    objects = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)
                    if objects is not None:
                        if objects is graphics.paddle:
                            graphics.set_dx()
                            if graphics.get_dy() > 0:
                                graphics.set_dy()
                        else:
                            graphics.set_dx()
                            graphics.set_dy()
                            graphics.window.remove(objects)


if __name__ == '__main__':
    main()
