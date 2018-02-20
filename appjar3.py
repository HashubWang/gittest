from appJar import gui
import random
import re
app = gui("Magic 8-Ball")
answers=["Can't tell you now","It is certain","Ask again later",
         "Yes","Don't count on it ","Doubtful", "No chance"]

app.setResizable(False)
app.setFont(18)
app.addEntry("Question")
L = ["who","what"]
def shake():
    if len(app.getEntry("Question"))==0:
        app.errorBox("Error","你必须问一个问题")
            
    else:
        answer=random.choice(answers)
        app.setLabel("Answer",answer)

def clear(btn):
    app.clearEntry("Question")
    app.clearLabel("Answer")

app.addButtons(["Shake","Clear"],[shake, clear])
app.addImage("8ball", "8ball.gif")
app.addEmptyLabel("Answer")
app.setLabelBg("Answer","yellow")
app.setFocus("Question")

app.go()