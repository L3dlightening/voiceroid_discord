# error when import
import pywinauto

def search_child_byname(name, uiaElementInfo):
    for childElement in uiaElementInfo.children():
        if childElement.name == name:
            return childElement
    return False

def launch_voiceroid():
    parentUIAElemet = pywinauto.uia_element_info.UIAElementInfo()
    voiceroid2 = search_child_byname("VOICEROID2", parentUIAElemet)
    if voiceroid2 == True:
        print("voiceroid there!")
    elif voiceroid2 == False:
        print("no voiceroid here...")


launch_voiceroid()