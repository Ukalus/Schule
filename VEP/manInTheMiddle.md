ARP - Address Resolution Protocol

besteht aus zwei nachrichten:

ARP-request
ARP-reply

ARP dient dazu, zu einer gegebenen IP-Adresse die zugehörige MAC-Adresse zu ermitteln.

ARP-request wird von fragenden geschickt.(Broadcast)
ARP-reply wird von dem Gerät mit der gegebenen IP-Adresse zurückgesendet(Unicast)

es gibt einen ARP-cache(lokal) für bereits erfragte MAC-Adressen:

ARP-request wird nur ausgeführt wenn es kein Eintrag im ARP-cache gibt.

schutz vor Man-in-the-middle attacken:

statischer eintrag in ARP-cache;
