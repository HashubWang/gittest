from appJar import gui

app=gui("Login")
app.addLabel("lb1","Login Window")
app.setBg("green")
app.setFg("white")
app.setFont(16)

app.addLabelEntry("Username")
app.addSecretLabelEntry("Password")
def press(name):
    if name == "Cancel":
        app.stop()
        app.setStatusbar("Cancel")
    elif name == "Reset":
        app.setStatusbar("Reset")
        app.clearEntry("Username")
        app.clearEntry("Password")
        app.setFocus("Username")
    elif name == "Submit":
        app.setStatusbar("Submit")
        username = app.getEntry("Username")
        password = app.getEntry("Password")
        if username=="wang" and password == "password":
            app.infoBox("Success", "Valid password")
        else:
            app.errorBox("Error", "Invalid password")

app.addButtons(["Submit", "Reset", "Cancel"],press)
app.addStatusbar()
app.setStatusbar("New status ...")
app.go()