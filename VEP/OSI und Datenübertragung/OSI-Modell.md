***VEP 8. September 2022***

**Abschlussprojekt**

- deutliches Projekt 
- deutlich was meine tätigkeit sein wird
- die doku nicht vernachlässigen 
- angemessenes niveu
- Zeitplanung aufschreiben (einteilung in realitische zeitabschnitte)

**Dokumentation**

- Betrieb vorstellen
- für wen wird das projekt gemacht
- ist zustandt
- problematik
- soll zustandt
- möglichkeiten zum erreichen des soll zustandes
- vorstellung von guten möglichkeiten
- erklärung von entscheidung der möglichkeit
- eigenleistung soll erkennbar sein 
- Analyse am ende: wie gut hat die Umsetzung funktioniert
- kosten des Projektes (in Arbeitsstunden)
- erreichter Nutzen in des endprodukts(return of investment)

**ISO-OSI-Modell**

ISO = International Standards Organisation
OSI = Open System Interconnection

Geschichtlicher Rückblick: 

- in den 1970er Jahren waren Netzwerke möglich von Firmen wie DEV, IBM, Xerox
- Nur Gleiche Systeme konnten untereinander Daten schicken (IBM <=> IBM, DEV <=> DEV)
- das verlangen nach unabhängiger kommunikation wurde stärker 
- ISO beschließt OSI Modell für einhaltliche kommunikaiton zwischen allen Systemen (Open System )

Ziel von OSI:

- unabhängikeit von:
    - Hersteller
    - Betriebsystem
    - 

OSI Beschreibt gesendete daten als schichten
- 7 Hierachisch angeordnete schichten/layer 
- beim abschicken werden diese von oben nach unten (7-1) durchgegangen
- beim empfangen andersrum (1-7)
- Layer können Parameter aushandeln falls es offene fragen oder fehler geben (sie müssen aber durch den Hierachischen fluss nach unten durch)
- vorteile von hierachischen schichten
    - spezialisierung jeder einzelnen Schicht 
    - leichte austauschbarkeit / modular
    - Unabhängikeit von Herrsteller, System und Hardware
- nachteile 
    - sperrig, klobig

OSI-Schichten:

- 1. bit Übertragungsschicht 
    - einzige schicht die Hardware ist
    - einzige schicht, die zugriff auf das übertragungsmedium hat 
    - muss einen geeigneten Anschluss für das verwendete Medium haben 
    - pinbelegung muss definert werden 
    - nachrichten werden in binär codiert (zum senden bereitgestellt)
    - Signalpegel(spannung von HIGH und LOW) wird festgelegt
    - übertragungsgeschwindigkeit wird festgelegt
    - überträgt einen Rohbitstrom(bedeutung der bits ist nicht bekannt)
    - auf der empfänger seite wird es wieder decodiert

- 2. Sicherungsschicht
    - alles zusammen heißt frame
    - aufgabe ist für eine fehlerfreie datenübertragung zu sorgen(zwischen zwei direkt miteinander verbundenen Geräten im Lan-Bereich)
    - erzeugt einen frame (Rahmen) mit
    - Header
        - Ziel-Mac (Hardware Adressen/ Physikalische Adressen)
        - Absender-Mac
        - Länge(Header + Datenpaket)
    - Datenpaket aus OSI-Schicht 3
    - Trailer 
        - prüfwert
            - wird berechnet vom absender aus header und datenteil und in den trailer geschrieben
            - der empfänger berechnet einen gegenprüfwert aus empfangenen daten und vergleicht diesen mit dem gesendeten prüfwert

- 3. Vermittlungsschicht
    - sucht und findet Transportwege durch ein Verbundsnetzwerk hindurch (Routing) (=WAN-Kommunikation)
        - Verbundnetzwerk mehreren Lans, die mit Routern miteinander verbunden sind
    - verwendet logische Adressen z.b. IP-Adressen
    Gerät-zu-Gerät kommunikation 
    - erzeugt Datagramme, d.h. eine Struktur, die aus zwei Teilen besteht:
        - Kopf
            - Version (kennnummer für IP-version entweder 4 oder 6 in binär)
            - IHL (IP Header Length)
            - TOS (Type of Service) priorisierung von IP-Paketen wird benutzt von Voice over ip weil schnell pakete benötigt werden bei datenverlust 
            - Total length(länge des gesamten IP-pakets)
            -TTL (Time to Live) man will verhindern das Datagramme eindlos im netzwerk umherschwirren ohne ihren empfänger zu erreichen. ein maximal 8 bit großer counter der bei jedem erreichen eines routers runterzählt. gelangt er auf null wird das gesendete paket verworfen.
            Protokoll: welches protokol wird verwendet (TCP UDP, HTTP, HTTPS)
            headerprüfwert: prüfwert zur sicherstellung der datenkorrektheit des headers
            Quelladresse(32 bit)
            Zieladresse(32 bit)


        - Datenteil (d.h. Daten aus der OSI-Schicht 4)

4. Transportschicht
- end-to-end kommunikation (welches Programm/ welcher Prozess empfängt die daten)
  für diese kommunikation wird eine port Adresse verwendet
- mit der Hilfe der Port-Adressen(16bit) werden Sockets gebildet:
    Sockets = IP-Adresse + Portnummer (z.b. 198.168.42.1:8080)
- einige der Port adressen sind für Server reserviert:
  bis 1023 sind die "well known ports" (von der IANA festgelegt bsp. http = port: 80/tcp ftp = 21/udp )
- Serverseitig 1-1023
- Clientseitig 1024-49152
- zwei wichtige Transportprotokolle
- UDP (User Datagram Protocol)
    - unbestätigt
    - verbindungslos
- TCP (Transmission Control Protocol)
    - bestätigt
    - verbindungsorientiert
    - verbindungsaufbau erfolgt  mit dem 3-Wege.
    - Handshake-verfahren
    - SYN
    - SYN-ACK
    - ACK
5. Sitzungschicht 
    Die Sitzungsschicht baut Sitzung(Session) auf, verwaltet sie und baut sie wieder ab. 
6. Darstellungsschicht
    sorgt für eine einheitliche Datenformate, z.B.
    ASCII, JPEG, MP3, UTF, unicode
7. Anwendungsschicht
stellt Eingabe und Ausgabe-Punkte für die Daten (die Kommuniziert werden) zur verfügung.