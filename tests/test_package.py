# Copyright (C) 2016 Jurriaan Bremer.
# This file is part of SFlock - http://www.sflock.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from sflock.abstracts import File

def test_package():
    assert File(filename="a.pdf").package == "pdf"
    assert File(filename="a.rtf").package == "doc"
    assert File(filename="a.doc").package == "doc"
    assert File(filename="a.docx").package == "doc"
    assert File(filename="a.docm").package == "doc"
    assert File(filename="a.dot").package == "doc"
    assert File(filename="a.dotx").package == "doc"
    assert File(filename="a.docb").package == "doc"
    assert File(filename="a.mht").package == "doc"
    assert File(filename="a.mso").package == "doc"
    assert File(filename="a.xls").package == "xls"
    assert File(filename="a.xlsx").package == "xls"
    assert File(filename="a.xlm").package == "xls"
    assert File(filename="a.xlsx").package == "xls"
    assert File(filename="a.xlt").package == "xls"
    assert File(filename="a.xltx").package == "xls"
    assert File(filename="a.xlsm").package == "xls"
    assert File(filename="a.xltm").package == "xls"
    assert File(filename="a.xlsb").package == "xls"
    assert File(filename="a.xla").package == "xls"
    assert File(filename="a.xlam").package == "xls"
    assert File(filename="a.xll").package == "xls"
    assert File(filename="a.xlw").package == "xls"
    assert File(filename="a.ppt").package == "ppt"
    assert File(filename="a.pptx").package == "ppt"
    assert File(filename="a.pps").package == "ppt"
    assert File(filename="a.ppsx").package == "ppt"
    assert File(filename="a.pptm").package == "ppt"
    assert File(filename="a.potm").package == "ppt"
    assert File(filename="a.potx").package == "ppt"
    assert File(filename="a.ppsm").package == "ppt"
    assert File(filename="a.pot").package == "ppt"
    assert File(filename="a.ppam").package == "ppt"
    assert File(filename="a.sldx").package == "ppt"
    assert File(filename="a.sldm").package == "ppt"
    assert File(filename="a.pub").package == "pub"
    assert File(filename="a.jar").package == "jar"
    assert File(filename="a.py").package == "python"
    assert File(filename="a.pyc").package == "python"
    assert File(filename="a.pyo").package == "python"
    assert File(filename="a.vbs").package == "vbs"
    assert File(filename="a.js").package == "js"
    assert File(filename="a.jse").package == "js"
    assert File(filename="a.msi").package == "msi"
    assert File(filename="a.ps1").package == "ps1"
    assert File(filename="a.ps1xml").package == "ps1"
    assert File(filename="a.psc1").package == "ps1"
    assert File(filename="a.psm1").package == "ps1"
    assert File(filename="a.wsf").package == "wsf"
    assert File(filename="a.wsc").package == "wsf"
    assert File(filename="a.htm").package == "ie"
    assert File(filename="a.html").package == "ie"
    assert File(filename="a.bat").package == "generic"
    assert File(filename="a.cmd").package == "generic"
    assert File(filename="a.lnk").package == "generic"
    assert File(filename="a.hta").package == "ie"

def test_case():
    assert File(filename="A.PDF").package == "pdf"
    assert File(filename="A.RTF").package == "doc"
    assert File(filename="A.DOC").package == "doc"
    assert File(filename="A.PUB").package == "pub"
    assert File(filename="A.JAR").package == "jar"
