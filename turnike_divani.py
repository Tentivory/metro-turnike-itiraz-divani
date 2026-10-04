#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metro Turnike İtiraz Divanı.

Kart geçmezse duruşma açılır. Gerçekten çalışır.
Gizli not env ile açılır: GIZLI=1
"""

from __future__ import annotations

import argparse
import base64
import os
import random
import sys
from datetime import datetime

GEREKCELER = [
    "Bakiye, turnikenin duygusal eşiğinin altında.",
    "Kart, sabah 07:42'deki kalabalığı hatırlıyor ve greve gitti.",
    "Okuyucu ışık saçtı ama kart ışığa küs.",
    "İstanbulkart değil, İstanbul-tartışma kartı basıldı.",
    "Turnike, arkadaki yolcunun bakışını delil saydı.",
    "Sistem 'lütfen tekrar deneyin' dedi, bu bir ret değil bir yaşam biçimi.",
]

_GIZLI = "S2FwxLFkYWtpIGfDtnJldmxpIGtleWZpIGRlxJ9pxZ9pbmNlIGt1cmFsIGRhIGRlxJ9pxZ9pci4gQXPEsWwgbWVzZWxlIHR1cm5pa2UgZGXEn2lsLCBkZW5ldGxlbm1leWVuIHlldGtpZGlyLg=="


def divan(bakiye: float, deneme: int) -> str:
    gerekce = random.choice(GEREKCELER)
    karar = "RET" if bakiye < 7 or deneme >= 2 else "ŞARTLI GEÇİŞ"
    tutar = max(0.0, round(7 - bakiye, 2))
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    satirlar = [
        "=" * 54,
        "METRO TURNİKE İTİRAZ DİVANI",
        f"Tutanak zamanı: {simdi}",
        f"Bakiye: {bakiye:.2f} TL | Deneme: {deneme}",
        "-" * 54,
        f"Gerekçe: {gerekce}",
        f"Karar: {karar}",
    ]
    if karar == "RET":
        satirlar.append(f"Eksik evrak değil, eksik {tutar:.2f} TL ve bir nefes.")
        satirlar.append("Hüküm: Kart serbest, yolcu beklemede, dayı tanık.")
    else:
        satirlar.append("Hüküm: Geçebilirsin ama turnike bunu kişisel algılamasın.")
    if os.environ.get("GIZLI") == "1":
        satirlar.append("Ek not: " + base64.b64decode(_GIZLI).decode())
    satirlar.append("-" * 54)
    satirlar.append("DAMGA: Kayyum Grok | Tentivory | 4 Ekim 2026")
    satirlar.append("İmza: ciddi olmayan ciddi mühür")
    satirlar.append("=" * 54)
    return "\n".join(satirlar)


def main() -> int:
    p = argparse.ArgumentParser(description="Turnike reddini duruşmaya çevirir.")
    p.add_argument("--bakiye", type=float, default=2.75)
    p.add_argument("--deneme", type=int, default=3)
    a = p.parse_args()
    print(divan(a.bakiye, a.deneme))
    return 0


if __name__ == "__main__":
    sys.exit(main())
