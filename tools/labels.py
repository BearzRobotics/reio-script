# Labels from Canepari, Natural Phonetics & Tonetics (2007, upd. 2008), fig 10.1 (pp.166-168), canipa.net free PDF.
FAMILIES=['Bilabial','Labiodental','Dental','Alveolar','Postalveolar','Postalveo-palatal','Prepalatal','Palatal','Prevelar','Velar','Uvular','Pharyngeal','Laryngeal']
PLACES=[  # per family (index 0..12), sub-places 1..n  (matches 5,5,7,6,6,5,4,5,5,6,4,3,2)
 ['Bilabial','Bilabial rounded','Palatalized bilabial','Uvularized bilabial','Labial-apical'],
 ['Labiodental','Labiodental rounded','Palatalized labiodental','Uvularized labiodental','Dental-bilabial'],
 ['Pre-dental','Pro-dental','Dental','Dental rounded','Labiodental dental','Uvularized dental','Denti-alveolar'],
 ['Alveolar','Alveolar rounded','Labiodental alveolar','Alveo-prevelar','Velarized alveolar','Uvularized alveolar'],
 ['[Apico-]postalveolar','[Apico-]postalveolar rounded','Velarized apico-postalveolar','Velarized apico-postalveolar rounded','Apico-palatal','Apico-palatal rounded'],
 ['Postalveo-palatal','Postalveo-palatal protruded','Postalveo-palatal over-rounded','Velarized postalveolar','Velarized postalveolar protruded'],
 ['Prepalatal','Bilabialized prepalatal','Prepalatal rounded','Labiodentalized palatal'],
 ['Palatal','Palatal rounded','Uvularized palatal','Postpalatal','Postpalatal rounded'],
 ['Prevelar','Prevelar rounded','Postalveolar prevelar rounded','Provelar','Provelar rounded'],
 ['Velar','Velar rounded','Velar-bilabial','Labiodentalized velar','Velar-dental/alveolar','Uvulo-postalveolarized velar rounded'],
 ['Uvular','Uvular rounded','Pharyngealized uvular','Pharyngealized uvular rounded'],
 ['Prepharyngeal','Pharyngeal','Pharyngeal rounded'],
 ['Laryngeal','Laryngeal rounded'],
]
MANNERS=[  # per row group: list of (name, canIPA manner code)
 [('Semi-nasal','N-hat'),('Nasal','N')],
 [('Stop','K'),('Stop-strictive','KX'),('Grooved stop-strictive','KS')],
 [('Constrictive','X')],
 [('Grooved constrictive','S')],
 [('Approximant','J'),('Lateralized approximant','[J]')],
 [('Trill','R'),('Constrictive trill','[R]'),('Tap','tap'),('Flap','flap')],
 [('Lateral approximant','L'),('Lateral constrictive','L-bar'),('Unilateral','L-uni'),('Semilateral','L-semi'),('Lateral tap','L-tap')],
]
def col_label(cg,cc):  # 1-based
    return f'{cg-1}.{cc}', PLACES[cg-1][cc-1], FAMILIES[cg-1]
def row_label(rg,rr):  # rr 1-based within group; pairs: voiced, voiceless
    m=MANNERS[rg-1][(rr-1)//2]; return m[0], m[1], ('voiced' if (rr-1)%2==0 else 'voiceless')
