#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This project is to generate your very own qrcode 
using python module call segno. Segno is an italian 
word for sign. it is Pure Python QR Code generator 
with no dependencies.
"""

import segno

#The content of the qr code in this case is a linkedin page
qrcode =segno.make_qr("https://docs.google.com/document/d/1-yucJhkfZ-AVrVqho_Z52cZpcIyDBlPTM_u6wt6K0zA/edit?usp=sharing")

#This is a class, where you can instantiate and specify the size, fill color, back color
qrcode.save(
    "qrcode.png",
    scale=5,
    border=0,
    dark= "#efa69d"
    )





