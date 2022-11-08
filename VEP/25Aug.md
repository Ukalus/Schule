**Andere Topologie Arten**

**Stern-Topologie**

- einen verteiler (hub/switch) <=> viele Clienten
- jeder client hat erstmal nur eine verbindung zum verteiler 
- die clienten haben keine besondere rolle / rolle egal
- in modernen netzwerken werden switches benutzt keine hubs
- Hub verteilt an alle <=> switch an einzelne
- switches sind im server raum 
- pro arbeitsplatz/client 2 netzwerk kabel netzwerk und telefon
- spezielle kabel mit kunststoff mantel von steckdose zu switch. anders als normales netzwerkkabel aus brandschutzgründen
- früher würde bei einem brand giftige gase ausgestoßen deshalb werden nun andere kunststoffe benutzt
- Maximale länge zwischen 2 Anwendern = (Anwender zu Client = 100)* 2 = 200m 

**Contra**
- hoher verkabelungsaufwand 
- teuer 

**Pro**
- weniger störanfällig 
    - twisted pair kabel mit rj45 stecker 
    - keine netzwerk noise 
    - bei kabelbruch ist nur der Client der mit dem Kabel verbunden ist beinträchtigt
    - Elektromagnitisch weniger störanfällig wegen symetrischer übertragung 
        - ein pol => asymetrisch
        - zwei pole => symetrisch 
- Übertragungsgeschwindikeit 100mb(verbreitet) bis zu 1 Gb

**Symetrische Übertragung**

2 gleichzeitige übertagungen

+5v
-5v 

störspannung beeinflusst beide spannungen 

+5v
-5v

normale nachricht:
+5v -(-5v) 

störung: +3v
+5v -(-5v) + 3v -(+3v)

**Usb-pin belegung(symetrisch)**

1 pin : +5v(strom)
2 pin : D+ (Data)
3 pin : D- (Data)
4 pin : Ground

**Kabellänge bei sterntopologie**

Maximal(bei elektronischem Signal):

- 5m von switch zu wand Serverraum
- 90m von Serverraum zu Andwenderraum
- 5m bis zum client 

Wenn länger:
- Signal wird schwächer(spannung wird geringer)

Maximal(bei Lichtwellenleitern/Glasfaser)

2 arten

- Multimoden (relativ dick) (1km)
- Monomoden (relativ dünn) (400km)

- bei diffusem licht => 
    durch zu viele reflexionen können daten verloren gehen (nicht sichtig  wichtig)
    (1km-400km je nachdem ob Multi Mono oder Polymoden)

***Baum-Topologie***

Alles was für Stern-Topologie gilt gilt auch für Baum Topologie 

Underschiede: 
 - es kann mehrere switches geben diese sind miteinander verbunden und es kann einen Core switch geben (muss es aber nicht)

***Maschen-Verbindung***

2 arten 

- Jeder Switch ist verbunden mit jedem anderen switch (Vollvermascht)
- jeder Switch ist mehreren anderen knoten verbunden (Teilvermascht)

**Contra**

- Riesiger Kabelaufwand 
- Riesiger Verwaltungsaufwand 
- Hohe ausfallsicherheit (es gibt ausweichstrecken fall eine andere verbindung gestört ist)

**Pro(nicht wirklich besprochen)**
- Alle Switches sind miteinander verbunden
- hohe ausfallsicherheit 