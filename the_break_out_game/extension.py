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
score = 0
score_label = GLabel(f'Your Score: {score}')
live = 3
live_label = GLabel(f'♡♡♡')


def main():
    global NUM_LIVES, score, score_label, live
    graphics = BreakoutGraphics()
    score_label.font = '-25'
    graphics.window.add(score_label, x=5, y=graphics.window.height)
    live_label.font = '-25'
    graphics.window.add(live_label, x=graphics.window.width - live_label.width, y=graphics.window.height)

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
            live -= 1
            if live == 2:
                live_label.text = '♡♡'
            elif live == 1:
                live_label.text = '♡'
            else:
                live_label.text = 'YOU\'RE DEAD'
                live_label.font = '-60'
                graphics.window.add(live_label, x=(graphics.window.width - live_label.width) / 2, y=graphics.window.height / 2 + 80)

        objects = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        if objects is not None:
            if objects is graphics.paddle:
                graphics.set_dx()
                if graphics.get_dy() > 0:
                    graphics.set_dy()
            elif objects is score_label or objects is live_label:
                pass
            else:
                graphics.set_dx()
                graphics.set_dy()
                graphics.window.remove(objects)
                score += 1
                score_label.text = 'Your Score:' + str(score)
        else:
            objects = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
            if objects is not None:
                if objects is graphics.paddle:
                    graphics.set_dx()
                    if graphics.get_dy() > 0:
                        graphics.set_dy()
                elif objects is score_label or objects is live_label:
                    pass
                else:
                    graphics.set_dx()
                    graphics.set_dy()
                    graphics.window.remove(objects)
                    score += 1
                    score_label.text = 'Your Score:' + str(score)
            else:
                objects = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
                if objects is not None:
                    if objects is graphics.paddle:
                        graphics.set_dx()
                        if graphics.get_dy() > 0:
                            graphics.set_dy()
                    elif objects is score_label or objects is live_label:
                        pass
                    else:
                        graphics.set_dx()
                        graphics.set_dy()
                        graphics.window.remove(objects)
                        score += 1
                        score_label.text = 'Your Score:' + str(score)
                else:
                    objects = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)
                    if objects is not None:
                        if objects is graphics.paddle:
                            graphics.set_dx()
                            if graphics.get_dy() > 0:
                                graphics.set_dy()
                        elif objects is score_label or objects is live_label:
                            pass
                        else:
                            graphics.set_dx()
                            graphics.set_dy()
                            graphics.window.remove(objects)
                            score += 1
                            score_label.text = 'Your Score:' + str(score)


if __name__ == '__main__':
    main()
