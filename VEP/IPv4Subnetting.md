# IPv4 Subnetting 

Abteilungen:

Geschäftleitung: 23 Geräte + 1 Router + 2 sonderadressen(netzwerkadresse und Broadcast adresse)
Einkauf: 29 Geräte + 1 Router + 2 sonderadressen(netzwerkadresse und Broadcast adresse)
Verkauf: 23 Geräte + 1 Router + 2 sonderadressen(netzwerkadresse und Broadcast adresse)
Produktion: 36 Geräte + 1 Router + 2 sonderadressen(netzwerkadresse und Broadcast adresse)

man benötigt 4 abteilungen plus 1 transfernetzwerk nach außen.
## Bestimmen der Subnetzmaske

Schönis Antwort:

am größten teilnetz Produktion(36) orientieren

36 

6bits => anzahl der bits zum darstellen des wertes 36

reserviere in der Subnetzmaske von rechts beginnend sechs 0

dann fülle den rest mit 1
11111111.11111111.11111111.11000000 oder /26

diese subnetzmaske wird jetzt nun überall im netzwerk benutzt

wir haben jetzt Classless inter domain Routing(CIDR)

## bestimmen der Netzadressen für die Teilnetze

übernimm den Netzwerkanteil der ungeteilten Adresse

Vorgabe: 172.20.0.0

alte subnetzmaske /16
neue subnetzmaske /26
differenz 10 bits

diese 10 bits werden benutzt um binär die geräte zu verteilen


die folgenden 26 - 16 bits gehören mit in den netzwerkanteil und werden verwendet um die subnetzmasken zu unterscheiden.

## zuordnen der netzadressen zu den teilnetzen

mann teilt diese selbst zu 

## Bestimmen der Hostadress-bereiche

binär durchzählen durch den hostanteil

172.20.0.65
172.20.0.126

## Bestimmen der broadcast adressen


172.20.1.127

## zuordnen der Geräteadressen(hostadressen) zu den Geräten

egal

## random kommentar von Schöni: 

es gibt Private und Öffentliche IP-Adressen, Private sind kostenlos, Öffentliche kosten geld 
jeder router hat 2 eine Private und eine Öffentliche.
wenn der router ein paket an seine Private adresse bekommt ersetz er diese im paket mit der Öffentlichen dresse
NAT(Network adress translation) wird genutzt um sich in einer NAT-Tabelle zu merken welche interne Ip ein paket gesendet hat. kommte ein Paket zurück weiß der router welcher privaten adresse er zuteilen soll.
Er ersetzt die Ziel Ip Adresse des pakets welches bei der öffentlichen Ip adresse ankommt mit der privaten Ip adresse
es gibt auch noch PAT(Port address translation) jeder in der NAT-tabelle wird noch ein eintrag im PAT-table erstelt in dem der zur absender ip adressen passenden port-adressen gespeichert werden um Geräte im Netzwerk zu differenzieren

