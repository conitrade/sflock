# Copyright (C) 2016-2018 Jurriaan Bremer.
# Copyright (C) 2018 Hatching B.V.
# This file is part of SFlock - http://www.sflock.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

import io
import os.path
import zipfile

from sflock.abstracts import File
from sflock.unpack import PdfFile, ZipFile

def f(filename):
    return File.from_path(os.path.join("tests", "files", filename))

def test_pdf_embedded():
    assert f("pdf_docm.pdf").magic.startswith("PDF document")
    m = PdfFile(f("pdf_docm.pdf"))
    assert m.handles() is True
    assert m.f.selected
    files = list(m.unpack())
    assert m.f.extension == "pdf"

    assert len(files) == 1
    assert not files[0].filepath
    assert files[0].filename == "Q6TCWXPS.docm"
    assert files[0].filesize == 55494
    assert files[0].extension == "docm"
    assert files[0].selected
    assert len(files[0].children) == 18

def test_pdf_magic():
    m = PdfFile(File(contents=f("pdf_docm.pdf").contents))
    assert m.handles() is True

def test_pdf_is_embedded():
    buf = io.BytesIO()
    z = zipfile.ZipFile(buf, "w")
    z.write("tests/files/pdf_docm.pdf")
    z.close()
    m = ZipFile(File(contents=buf.getvalue()))
    files = list(m.unpack())
    assert len(files) == 1
    assert files[0].extension == "pdf"
    assert len(files[0].children) == 1
    assert files[0].children[0].extension == "docm"

def test_bypass_minimized():
    m = PdfFile(f("bypass_minimized.pdf"))
    files = list(m.unpack())
    assert len(files) == 1
    assert files[0].filename == "test.txt"
    # TODO Fix actually reading the contents of this file correctly (which is
    # a peepdf issue, AFAICT).

def test_garbage():
    m = PdfFile(f("garbage.bin"))
    assert m.handles() is False
    assert m.f.selected
    assert not m.unpack()
