# -*- coding: utf-8 -*-

"""

创建XML
"""
from xml.dom.minidom import Document
class write_xml(Document):
  def __init__(self):
    Document.__init__(self)
  def set_tag(self,tag):
    self.tag = tag
    self.tag1 = self.createElement(self.tag)
    self.appendChild(self.tag1)
    self.maincard = self.createElement("card")
    self.maincard.setAttribute("id", "main")
    self.maincard.setAttribute("id2","main2")
    self.tag1.appendChild(self.maincard)
    self.paragraph1 = self.createElement("p")
    self.maincard.appendChild(self.paragraph1)
    self.ptext = self.createTextNode("This is a test!")
    self.paragraph1.appendChild(self.ptext)
  def display(self):
    print (self.toprettyxml(indent="  "))
wx = write_xml()
wx.set_tag('test2')
wx.display()