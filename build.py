"""Generuje statický web Lucky Canteen (náhrada za WordPress/Mioweb).

python3 build.py  → index.html + podstránky v priečinkoch (zachované staré URL /o-nas/, /denne-menu/ …)
Obsah prevzatý z luckycanteen.sk (28. 10. 2026). Denné menu ide z widgetu Menučka.sk – netreba ho tu meniť.
"""
from pathlib import Path

ROOT = Path(__file__).parent
TEL = "+421 948 130 504"
TEL_LINK = "+421948130504"
MAIL = "objednavky@canteen.sk"
ADRESA = "Ivánska cesta 30/B, Bratislava"
OBJEDNAVKA = "https://luckycanteen.order.app.hd.digital/menus"
MENUCKA = "https://www.menucka.sk/widget/main/luckycanteen/weekmenu"

RANAJKY = [
    ("Praženica s jarnou cibuľkou", "4,90 €"),
    ("Volské oká", "4,90 €"),
    ("Ham & eggs", "4,90 €"),
    ("Bacon & eggs", "4,90 €"),
    ("Omeleta so syrom", "4,90 €"),
    ("Čoko proteínová ovsená kaša", "5,00 €"),
    ("Chia puding", "3,50 €"),
]

NAV = [("", "Úvod"), ("o-nas/", "O nás"), ("denne-menu/", "Denné menu"),
       ("ranajkove-menu/", "Raňajkové menu"), ("kontakt/", "Kontakt")]

CSS = """
:root{--bg:#121212;--panel:#1c1c1c;--line:#2c2c2c;--text:#f2efe9;--muted:#b9b3a8;--gold:#f2b43a;--gold-dark:#d99a1c}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;font-size:17px;line-height:1.6}
a{color:var(--gold)}img{max-width:100%;display:block}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
header{position:sticky;top:0;z-index:10;background:rgba(18,18,18,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:72px}
header img{height:52px;width:auto}
nav{display:flex;flex-wrap:wrap;gap:4px 18px;align-items:center}
nav a{color:var(--text);text-decoration:none;font-family:'Oswald',sans-serif;text-transform:uppercase;letter-spacing:.06em;font-size:15px}
nav a:hover,nav a[aria-current]{color:var(--gold)}
.btn{display:inline-block;background:var(--gold);color:#1a1300;font-family:'Oswald',sans-serif;text-transform:uppercase;letter-spacing:.06em;text-decoration:none;padding:12px 22px;border-radius:6px;font-weight:600}
.btn:hover{background:var(--gold-dark)}.btn.ghost{background:transparent;color:var(--gold);border:2px solid var(--gold)}
h1,h2,h3{font-family:'Oswald',sans-serif;font-weight:600;line-height:1.15;letter-spacing:.01em}
h1{font-size:clamp(34px,6vw,60px);margin:0 0 14px}h2{font-size:clamp(26px,4vw,38px);margin:0 0 16px;color:var(--gold)}
.hero{position:relative;min-height:72vh;display:flex;align-items:center;background:linear-gradient(rgba(10,10,10,.62),rgba(10,10,10,.82)),url(IMG/hero.jpg) center/cover}
.hero p{max-width:640px;color:#e8e2d6;font-size:19px}.hero .tag{color:var(--gold);font-family:'Oswald',sans-serif;text-transform:uppercase;letter-spacing:.12em}
.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
section{padding:64px 0}section.alt{background:var(--panel)}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:36px;align-items:center}
.photos{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
.photos img{border-radius:8px;aspect-ratio:16/10;object-fit:cover;width:100%}
.menu-list{list-style:none;padding:0;margin:0}.menu-list li{display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px dashed var(--line)}
.menu-list span:last-child{color:var(--gold);font-weight:600;white-space:nowrap}
.note{color:var(--muted)}
.info{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px}
.info div{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:20px}
.info h3{margin:0 0 8px;color:var(--gold);font-size:20px}
iframe.menucka{width:100%;min-height:900px;border:0;border-radius:8px;background:#fff}
footer{border-top:1px solid var(--line);padding:28px 0;color:var(--muted);font-size:15px}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px}
@media (max-width:760px){header .wrap{flex-direction:column;padding:10px 16px}nav{justify-content:center}section{padding:44px 0}.wrap{padding:0 16px}}
"""


def page(path, title, desc, body, active):
    depth = 1 if path else 0
    up = "../" * depth
    nav = "".join(
        f'<a href="{up}{href}"{" aria-current=page" if href == active else ""}>{label}</a>' for href, label in NAV
    )
    html = f"""<!DOCTYPE html>
<html lang="sk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="{up}img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Oswald:wght@500;600&display=swap" rel="stylesheet">
<!-- GTM-TX256C9Z + Meta Pixel doplniť až s cookie lištou (súhlas) -->
<style>{CSS.replace("IMG/", up + "img/")}</style></head>
<body>
<header><div class="wrap"><a href="{up}"><img src="{up}img/logo.png" alt="Lucky Canteen" width="63" height="52"></a>
<nav>{nav}<a class="btn" href="{OBJEDNAVKA}">Objednať</a></nav></div></header>
<main>{body.replace("IMG/", up + "img/")}</main>
<footer><div class="wrap"><span>Lucky Canteen · {ADRESA} (budova Aircraft)</span>
<span>Tel.: <a href="tel:{TEL_LINK}">{TEL}</a> · <a href="mailto:{MAIL}">{MAIL}</a></span>
<span><a href="https://www.tysomaru.sk/uvod/">Ty Somaru</a> · <a href="https://www.tysomaru.sk/blog/">Blog</a></span></div></footer>
</body></html>"""
    out = ROOT / path / "index.html" if path else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


INFO = f"""<div class="info">
<div><h3>Adresa</h3>{ADRESA}<br>budova Aircraft</div>
<div><h3>Otvorené Po – Pi</h3>Raňajky: 7:00 – 10:30<br>Obedy: 11:00 – 14:00</div>
<div><h3>Kontakt</h3>Tel.: <a href="tel:{TEL_LINK}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></div>
</div>"""

RANAJKY_HTML = '<ul class="menu-list">' + "".join(f"<li><span>{n}</span><span>{c}</span></li>" for n, c in RANAJKY) + "</ul>"
RANAJKY_NOTE = """<p class="note">Všetky vaječné raňajky pripravujeme zo 4 kvalitných vajec z voľného výbehu (Slovensko).
Ku každým raňajkám je v cene 1 kus pečiva alebo 2 krajce chleba a čerstvá zelenina.</p>
<p class="note">Každý deň pre vás pripravujeme aj domáce dezerty, smoothie bowls, proteínové nátierky
a vždy čerstvé pečivo priamo z remeselnej pekárne.</p>"""

page("", "Denné menu a raňajky pri letisku Bratislava | Lucky Canteen",
     "Moderná kantína v budove Aircraft na Ivánskej ceste – raňajky, denné obedové menu a rozvoz.",
     f"""<section class="hero"><div class="wrap"><div class="tag">Budova Aircraft · Ivánska cesta</div>
<h1>Chutné denné menu a raňajky pri letisku v Bratislave</h1>
<p>Poctivé, rýchle a cenovo dostupné jedlo pre všetkých, ktorí pracujú v okolí letiska a obchodných zón v Ružinove. Už aj na rozvoz.</p>
<div class="actions"><a class="btn" href="{OBJEDNAVKA}">Online objednávka</a><a class="btn ghost" href="denne-menu/">Denné menu</a></div></div></section>
<section><div class="wrap grid2"><div><h2>Raňajkové menu</h2>{RANAJKY_HTML}<p style="margin-top:18px"><a class="btn ghost" href="ranajkove-menu/">Celé raňajkové menu</a></p></div>
<img src="IMG/foto4.jpg" alt="Raňajky v Lucky Canteen" style="border-radius:8px"></div></section>
<section class="alt"><div class="wrap"><h2>Raňajkové a obedové menu najvyššej kvality</h2>
<p>Raňajky a obedy pripravujeme z kvalitných slovenských surovín – vajíčka od sliepok z voľného chovu a mäso z overených fariem. Poctivé chute, na ktoré sa oplatí vrátiť.</p>
<div class="photos"><img src="IMG/foto1.jpg" alt="Polievka"><img src="IMG/foto5.jpg" alt="Obedové menu"><img src="IMG/foto6.jpg" alt="Jedlo z Lucky Canteen"></div></div></section>
<section><div class="wrap"><h2>Kde nás nájdete</h2>{INFO}</div></section>""", "")

page("o-nas", "O nás | Poctivá kantína v budove Aircraft | Lucky Canteen",
     "Lucky Canteen – poctivá kantína na Ivánskej ceste v budove Aircraft pri letisku Bratislava.",
     f"""<section><div class="wrap grid2"><div><h1>Vaša poctivá kantína na Ivánskej ceste</h1>
<p>Sme Lucky Canteen a veríme, že stravovanie počas pracovného dňa by nemalo byť len nutnou rutinou, ale chvíľou, na ktorú sa budete tešiť. Naším cieľom je priniesť kvalitné, čerstvé a s radosťou pripravené jedlo ľuďom, ktorí pracujú v rýchlom tempe a potrebujú dobiť energiu na zvyšok dňa.</p></div>
<img src="IMG/jedlo.jpg" alt="Jedlo z Lucky Canteen" style="border-radius:8px"></div></section>
<section class="alt"><div class="wrap"><h2>Rýchle obedy bez kompromisov v kvalite</h2>
<p>Koncept Lucky Canteen vznikol z jednoduchej myšlienky: ponúknuť ľuďom pracujúcim v okolí poctivé jedlo, aké by si uvarili sami doma, ak by na to mali čas.</p>
<p>Zabudnite na stereotypy o unavených závodných jedálňach. U nás v kuchyni nerobíme skratky. Zakladáme si na starostlivo vyberaných surovinách, osvedčených receptoch a vyvážených porciách. Či už máte práve chuť na výdatnú tradičnú slovenskú klasiku, poctivú polievku, alebo ľahšie a moderné jedlo, naše denné menu zostavujeme tak, aby si v ňom každý našiel to svoje.</p></div></section>
<section><div class="wrap"><h2>Prečo práve budova Aircraft?</h2>
<p>Lokalitu sme si nevybrali náhodou. Naším domovom sa stala budova Aircraft na Ivánskej ceste 30/B, strategické miesto v tesnej blízkosti bratislavského letiska a ružinovských biznis zón. Vieme, že vaša obedná prestávka je často ohraničená časom. Preto sme tu – priamo vo vašom susedstve, aby ste drahocenné minúty nestrácali presunmi cez polovicu mesta. Ak to k nám z kancelárie predsa len nestíhate, náš spoľahlivý rozvoz vám raňajky aj obedy doručí rovno na recepciu alebo na stôl.</p>
<div class="actions"><a class="btn" href="{OBJEDNAVKA}">Objednať rozvoz</a></div></div></section>""", "o-nas/")

page("denne-menu", "Denné obedové menu Bratislava - Ivánska cesta | Lucky Canteen",
     "Aktuálne denné obedové menu Lucky Canteen – zastavte sa alebo objednajte donášku.",
     f"""<section><div class="wrap"><h1>Aktuálne denné obedové menu</h1>
<p>Zastavte sa alebo si objednajte donášku. Obedy podávame Po – Pi 11:00 – 14:00.</p>
<div class="actions" style="margin-bottom:24px"><a class="btn" href="{OBJEDNAVKA}">Online objednávka</a></div>
<iframe class="menucka" src="{MENUCKA}" title="Denné menu Lucky Canteen (Menučka.sk)" loading="lazy"></iframe></div></section>""", "denne-menu/")

page("ranajkove-menu", "Raňajky Bratislava letisko | Raňajkové menu | Lucky Canteen",
     "Raňajkové menu Lucky Canteen – vajíčka z voľného výbehu, ovsená kaša, chia puding. Po – Pi 7:00 – 10:30.",
     f"""<section><div class="wrap grid2"><div><h1>Raňajkové menu</h1>{RANAJKY_HTML}{RANAJKY_NOTE}
<p class="note">Raňajky podávame Po – Pi 7:00 – 10:30.</p></div><img src="IMG/foto4.jpg" alt="Raňajky" style="border-radius:8px"></div></section>""", "ranajkove-menu/")

page("kontakt", "Kontakt | Lucky Canteen – Ivánska cesta 30/B, Bratislava",
     "Kontakt na Lucky Canteen: Ivánska cesta 30/B (Aircraft), tel. +421 948 130 504, objednavky@canteen.sk.",
     f"""<section><div class="wrap"><h1>Kontakt</h1><p>Ak máte akékoľvek otázky, neváhajte nás kontaktovať. Objednávky na rozvoz vybavíte najrýchlejšie online.</p>
{INFO}<div class="actions"><a class="btn" href="{OBJEDNAVKA}">Online objednávka</a>
<a class="btn ghost" href="https://maps.google.com/?q=Iv%C3%A1nska+cesta+30%2FB+Bratislava">Navigovať</a></div></div></section>""", "kontakt/")

print("hotovo")
