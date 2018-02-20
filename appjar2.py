from appJar import gui
app = gui("Lights!")
app.addImage("Light","bulb_on.gif")

def press(name):
    if name=="Exit":
        app.stop()
    elif name=="On":
        app.setImage("Light","bulb_on.gif")
        app.disableButton("On")
        app.enableButton("Off")

    elif name=="Off":
        app.setImage("Light","bulb_off.gif")
        app.disableButton("Off")
        app.enableButton("On")


app.addButtons(["On","Off"],press)
app.addButton("Exit",press)


app.go()