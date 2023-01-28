Koppelelemente

Repeater
        OSI-Schicht 1
|-------->Repeater>---------|

verlängert die Übertragungsreichweite

ein signal wird auf längerer strecke abgedämpft
der Repeater verstärkt bzw kehrt die dämpfung um.

Hub

Hub = Multiport-Repeater
Bi-direktional
Bustopologie

ein Signal wird an alle angeschlossenen geräte "repeatet"
werden nicht in mordernen netzen nicht mehr benutzt

Bridge

    SAT (Source Address Table)

Switch (multiport-bridge)
    hat auch einen source-address table
    sucht im table nach adressat
    wenn gefunden dann werden die daten dahin geschickt
    falls nicht werden die daten an alle adressen geschickt
    Teure Switches sind manageable switches haben:
    Port security:
        Als administatoren kann man festlegen welche mac adresse an jeder Switch adresse sein darf
    DHCP security:

    Aufteilung von Switch: 

    Anforderung(Fachlich angemessen erklären wie ein switch funktioniert)

Router:
    mindestens 2 Anschlüsse
    verbindet mindestens 2 IP netzwerke
    OSI-Schicht 2
    Router müssen händisch konfiguriert werden
    Ip adressen müssen konfiguriert werden
    Routing Tabellen müssen konfiguriert werden
        Ziel (Ziel IP-Adresse)
        Entfernung (in Hops => sprünge zwischen Netzwerken)
        Welche richtung (welches Exit interface)
    Routing tabellen können:
        statisch konfiguriert werden 
            kleine netze
            kaum/ selten änderungen
        dynamisch konifguriert werden (Router tauschen Routing tabellen gegenseitig aus)
            große netze 
            häufige änderungen an der infrastruktur
            Routing Protokoll (RIP,OSPF,...)

Firewall:
    Firewall hat einen Internen und Externen port
    Richtungsabhängige Regeln

    
    