import subprocess
import webbrowser
from playsound import playsound
import sys
import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation

for i in range(1, 100):
    pos = abs((start_pos - i*90) % 360)
    screen.rotate_to(pos)



url = 'https://www.animecharactersdatabase.com/ux_search.php?tag=loli'
webbrowser.open('https://www.animecharactersdatabase.com/ux_search.php?tag=loli', new=2)
webbrowser.open('https://www.youtube.com/watch?v=B-ELvr9dDkk', new=2)
playsound("sound\\loli.mp3")


