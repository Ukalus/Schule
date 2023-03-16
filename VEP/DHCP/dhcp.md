## DHCP Dynamic Host Configuration Protocol

## nicht DHCP
IP-Configuration per Hand jedes einzelndes gerätes: Alias Netz
Nachteile:
Fehleranfällig
Doppelte Adressen

## DHCP

- Automatische IP-Configuration von Hosts
    - IP-Adresse, Subnetzmaske, + weitere Parameter 
Vorteile:

- Fehlervermeidung 
- Schneller (als per hand)
- Re-use von IP-Konfiguration

Nachteile:

- Abhängigkeit von DHCP-Server
- Anfälligkeit für Attacken


## Details

benötigte dinge:

DHCP-Server
DHCP-Client (nehmen den DHCP-Server)

DHCP-Server hat eine *menge* von IP-Adressem
+ Subnetzmaske
+ Weitere Parameter

## DHCP Server einschalten

1. DHCP-Discover paket (Client -> Network Broadcast adress) (look for DHCP-Server)
    
    Header(3 IP-Schicht):
    -   Absenderadresse: 0.0.0.0
    -   ZielAdresse(Broadcast): 255.255.255.255 
    Header(2 Sicherungs-schicht)
    -   AbsenderMAC: Client-Adresse
    -   ZielMAC(Broadcast-MAc): FFFFFFFFFFFF

2.  DHCP-Offer

    Header(3 IP-Schicht):
    -   Absenderadresse: DHCP-Server-ip-adresse
    -   ZielAdresse(Broadcast): 255.255.255.255 
    Header(2 Sicherungs-schicht)
    -   AbsenderMAC: DHCP-Server-Mac
    -   ZielMAC: Client-Mac-adresse

3. DHCP-Request Client teilt mit für welches angebot er sich entschieden hat

    Header(3 IP-Schicht)
    -   Absenderadresse: 0.0.0.0
    -   Zieladresse(Broadcast): 255.255.255.255
    Header(2 Sicherungs-schicht)
    -   AbsenderMAC: ClientMac
    -   ZielMAC: fffffff

4. DHCP-ACK der DHCP Server, dessen Angebot angenommen wurde, erteilt dem DHCP-Client die Freigabe zur verwendung dieser Ip-konfiguration

 Header(3 IP-Schicht)
    -   Absenderadresse: DHCP-Client-Adresse
    -   Zieladresse(Broadcast): 255.255.255.255
    Header(2 Sicherungs-schicht)
    -   AbsenderMAC: DHCP-ClientMAC
    -   ZielMAC: ClientMAC

Lease-Zeit: Wie lang ist die IP-Configuration gültig

- Nachdem 50% der Lease zeit abgelaufen ist bittet der client beim DHCP-server um eine verlängerung
- Wenn server da, DHCP server sendet bestätigung der verlängerung 
- Wenn server nicht da bzw antwortet nicht , Lease zeit wird nicht verlängert 
- Zeit läuft dann ab bis 87,5% der zeit abgelaufen ist fragt der Client wieder von einem irgendeinen DHCP server Als Broadcast die verlängerung an (DHCP-Tabellen werden geteilt)
- Wenn 100% der zeit abgelaufen ist wird eine neues DHCP-Discover paket losgeschickt(ip-adresse des Netzwerkes wird wieder auf 0.0.0.0 gesetzt)


## DHCP Infrastructur in gerouteten netzwerken

Dezentralisierte DHCP Infrastructur

1. Workaround: DHCP-Server in Jedem Subnetz einrichten
    Vorteil: 
    - Hohe Ausfallsicherheit (über alle subnetze)
    - Verwaltung kann abgegeben werden an jemand anderen (zuständigkeit für den DHCP-server)
    Nachteil:
    - Erhöhter Hardwareanteil

Zentrale DHCP Infrastructur
2. Workaround: DHCP-Relay Agent in jedes Subnetz

Was macht der Agent?

- der DHCP-Relay-agent ist der Vertreter des DHCP-servers im Subnetz
- kennt die IP-adresse eines DHCP-Servers 
- Der DHCP-Relay Agent hört auf dem Broadcast des DHCP-Servers
- Agent meldet sich per Unicast an den DHCP Server wenn eine neue Ip-configuration benötigt wird 

3. Router mit eingebautem DHCP-Relay-Agent

- man braucht nur den eingebauten DHCP-Relay-Agent

4. Hybride DHCP Infrastructur

- Jedes Subnetz bekommt einen DHCP-Server und einen DHCP-Relay-agent
- Dieser Relay-agent hat eine verzögerung weshalb zuerst der lokale DHCP server angesprochen wird
- sollte der locale DHCP-Server nicht antworten kümmert sich nach dem delay der DHCP-relay-Agent um die IP-config anfrage


DHCP-Hacking

Als DHCP-server ausgeben 
sagen das unser pc der standard gateway server ist 
alle nachrichten über unseren proxy sniffing server laufen lassen 

schützen indem man den switch so configuriert das nur über ein gewissen port DHCP-offers gesendet werden können

DHCP-discovers attack

so viele discover pakete schicken das standard DHCP-server nicht mehr erreichbar  ist 

danach kann man sich als DHCP-server ausgeben 

