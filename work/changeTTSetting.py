from xml.etree import ElementTree as et

xmlfile = r"C:\Users\Public\Documents\AlliedStar\ScanPro\preferences.xml"

def changeTTSetting(mykey, flag):
    tree = et.parse(xmlfile)
    root = tree.getroot()
    for child in root.iter("option"):
        if child.attrib['key'] == mykey:
            child.attrib['value'] = flag
    tree.write(xmlfile)


changeTTSetting("ENABLE_TT_LICENSE_CHECK", "false")
