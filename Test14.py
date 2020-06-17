import time


import matplotlib.pyplot as plt
import libpipong


fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = libpipong.Game(ax)

# Désactive les raccourcis par défaut.
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# reset du fond d'écran.
def handle_redraw(event):
    animation.background = None


# bootstrap après le premier dessin
def start_anim(event):
    canvas.mpl_disconnect(start_anim.cid)

    def local_draw():
        if animation.ax.get_renderer_cache():
            animation.draw(None)
    start_anim.timer.add_callback(local_draw)
    start_anim.timer.start()
    canvas.mpl_connect('draw_event', handle_redraw)


start_anim.cid = canvas.mpl_connect('draw_event', start_anim)
start_anim.timer = animation.canvas.new_timer()
start_anim.timer.interval = 1

tstart = time.time()

plt.show()
print('FPS: %f' % (animation.cnt/(time.time() - tstart)))
