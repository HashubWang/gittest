from appJar import gui
import youdaodictComputerSearch as yd


win =gui("有道词典查询")

win.addEntry("word", 0,1)
win.addLabel("wordsearch","请输入要查询的单词",0,0)
win.addEmptyLabel("Result",1,0,2)
win.setLabelRelief("Result", win.GROOVE)
win.setLabelAlign("Result", win.NW)
win.addEmptyLabel("Resultcp")

win.setFocus("word")


def search(name):
    if name == "重置":
        win.clearEntry("word")

    elif name == "退出":
        win.stop()

    elif name == "查询":
        win.clearLabel("Resultcp")
        findword=win.getEntry("word")
        res = yd.Build(findword)
        finalres = yd.Basic_Search(res)
        finalrescp = yd.Advanced_Search(res)

        message = ""
        for i in finalres:
            message += str(i) +"\n"

        win.setLabel("Result", message)

        message = ""

        if finalrescp is None:
            pass

        else:
            for i in finalrescp:
                message += str(i) +"\n"
                win.setLabel("Resultcp", "计算机科学技术：\n\n"+message)


win.addButtons(["查询", "重置", "退出"], search)

def pressEnterSearch():
    # same as line24-line45
    win.clearLabel("Resultcp")
    findword = win.getEntry("word")
    res = yd.Build(findword)
    finalres = yd.Basic_Search(res)
    finalrescp = yd.Advanced_Search(res)

    message = ""
    for i in finalres:
        message += str(i) + "\n"

    win.setLabel("Result", message)

    message = ""

    if finalrescp is None:
        pass

    else:
        for i in finalrescp:
            message += str(i) + "\n"
            win.setLabel("Resultcp", "计算机科学技术：\n\n" + message)


def keyPress(key):
    if key == "<Return>":
        pressEnterSearch()


win.bindKey("<Return>", keyPress)


win.go()








