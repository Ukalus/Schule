**Zugriffsverfahren**

- pakete werden verschickt (ca 1.5kb)
- es werden kleine pakete benutzt um fehleranfälligkeit und gerechte brandbreiten verteilung zu ermöglichen 

regeln welcher Teilnehmer wann etwas senden darf (und wann nicht )

Verfahren:

- CSMA/CD
- CSMA/CA
- Token Passing

CSMA/CD:
-Carrier Sense Multiple Access with Collision Detection-
-Wird benutzt im Ethernet-

Carrier sense => hören ob bereits übertragung stattfindet
Multiple Access => mehrere Geräte direkt verbunden
Collision Detection => man stellt fest das man etwas anderes hört als gesendet wurde und erkennt das die daten nicht richtig gesendet wurden 

was passiert bei einer collision:
- wir hören auf zu senden 
- wir bestimmen eine wartezeit zufällig bevor wir wieder senden (beide in der collision beteiligte computer machen das)

CSMA/CA:
-Carrier Sense Multiple Access with Collision Avoidance-
-wird benutzt in WLAN und Funknetzen-
-wird benutzt anstatt CSMA/CD da kein DUPLEX() datenübertragung verwendet werden kann-

was tut CSMA/CA um Collisionen zu vermeiden?
- man sendet eine nachricht das man nun eine übertragung starten will 
- man sendet außerdem an wen man eine nachricht senden will (um zu checken ob empfangsperson bereit ist zum empfangen)

Token Passing:
- Ring topologie 
- token wird die ganze zeit im kreis druchgereicht (anfangs leer)
- wer den token hat darf etwas in den token schreiben oder lesen
- der token enthält (Nachricht, absender, empfänger)
- jeder teilnehmer checkt ob er der empfänger ist wenn er den token bekommt
- die nachricht startet bei absender und wird durchgereicht bis zum empfänger 
- der empfänger senden dann eine bestätigung an den absender 
- danach kann der absender mehrere pakete nachsenden 
- es gibt eine obergrenze an gesendeten paketen die festgelegt
- kollisionen sind ausgeschlossen (es wird immer nur eine Nachricht/Token versendet)