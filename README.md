# LoliFinder
Lolifinder is a free-to-use prank script to use on your friends.
Use this at your on risk as i do not take responsability for any damaged property. ^_^

You can modify the script with your own stuff just change the urls in and the sound.It's that easy!

title: Installation

# Installing LoliFinder

## The Easy Way

You have to first install the requirements to run the python program. To do that you type this command in LoliFinder's root directory:
```bash
pip install -r requirements.txt  
```
Then to run the program you have to type this command in the root directory of LoliFinder:
```bash
python LoliFinder.py
``` 
That's it! You're ready to use LoliFinder. Enjoy!

title: Modifing

# Modifing LoliFinder

You have to first open your favourite code/text editor and then edit this(if you want to change the website your friend is getting redirected to):

```bash
webbrowser.open('yoururldonotforgethttporhttps', new=2)
``` 
To modify the song/sound used when starting the script you have to modify this simple line of code(it has to be mp3 or else it will not work) then add your mp3 in the sound directory that is located in the main directory of LoliFinder:

```bash
playsound("sound\\yoursound.mp3")
```
That's it! You have successfully modified LoliFinder. Enjoy!



