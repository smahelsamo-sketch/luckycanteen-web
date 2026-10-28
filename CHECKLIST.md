---
name: web-checklist
description: "Pri stavbe/prestavbe webu (Lucky Canteen 28. 10.) – čo Samuel chce a ktoré chyby skontrolovať sám, skôr než mu web ukážem"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1f5d5742-4bd2-435f-b4e3-e79c9d694c0f
  modified: 2026-10-28T13:48:46.853Z
---

Samuel 28. 10. 2026: „pamätaj si, čo všetko opravuješ, aby si pri ďalšej stránke vedel hneď, čo a ako treba, a nemusel som ja hľadať chyby.“

**Zadanie pri prerábke existujúceho webu:**
- Texty, popisy, ceny, nadpisy, poradie sekcií **1:1 ako pôvodný web** – nič „nevylepšovať“ (ani preklepy typu „Back&eggs“, formát „4.90€“).
- Farby podľa **loga/značky** (Lucky Canteen = čierna + červená #9C2021), nie podľa súčasného webu ani mojej voľby.
- Zachovať staré URL (podstránky ako priečinky `/o-nas/` …), popup a sticky tlačidlá, ak ich pôvodný web má.
- Logo vziať oficiálne z Disku (nie zmenšeninu z webu). Stock fotky z knižnice platformy (napr. media.mioweb.cz) nepoužívať – licencia.

**Pred ukázaním Samuelovi skontrolovať sám:**
1. Mobil 360 / 390 / 768 px (iframe test v Chrome): `scrollWidth > clientWidth` = niečo preteká. Typické príčiny: `max-width:NNNpx` na obrázku prepíše globálne `max-width:100%` → písať `max-width:min(NNNpx,100%)` + `width:100%`.
2. **Nedávať `overflow-x:hidden` na html/body** – na mobile rozbije `position:fixed` (popup sa posunie doľava). Pretekanie riešiť pri zdroji.
3. Popup: `top:0;left:0;width:100%;height:100%` + box `margin:0 auto`; otvoriť a zmerať, či je box v strede.
4. Relatívne cesty na podstránkach (`../img/`), logo a odkazy v menu na každej podstránke.
5. Všetky odkazy/obrázky HEAD 200 (false positive: preconnect fonty, 403/466 bot ochrana).
6. Externé widgety (Menučka iframe) sa naozaj načítajú s aktuálnymi dátami.
7. GitHub Pages: pridať `.nojekyll` (inak build „errored“); free plán = verejné repo.
8. Meranie (GTM/Pixel) len s cookie lištou.

Pozri [[vystupy-citatelne-html]].
