import re
import pyperclip

trackers = pyperclip.paste()
fetch_trackers = re.findall("(.*\/\/.*)", trackers)

with open("./trackers.txt", "a+") as tf:
    tf.write("\n".join(fetch_trackers))

print(trackers)