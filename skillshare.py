#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    "username": "chadboyce@gmail.com",
    "password": "crakr0x1128"
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.skillshare.com/classes/Calligraphy-Essentials-From-First-Script-to-Final-Flourish/1829141067/00'])