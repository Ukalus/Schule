# Test vorbereitungen


#### ISO OSI Model

> 7 Anwendungsschicht ✔

> 6 Darstellungsschicht ✔

> 5 Sessionschicht ✔

> 4 Transportschicht ✔

> 3 Vermittlungsschicht ✔

> 2 Sicherungsschicht ✔

> 1 Bitübertragungsschicht ✔


#### Kopplungselemente 

> Repeater ✔

> Hub ✔

> Switch ✔

> Router ✔

> Firewall


#### 3 Way Handshake

> SYN ✔

> SYN ACK ✔

> ACK ✔

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

#### ISO OSI-Modell

## Generelle Infos

**OSI** steht für
> **Open System Interconnection**

Früher gab es nur kommunikation zwischen Geräten des gleichen Herstellers (IBM <=> IBM)

Das OSI-Modell entstand in 1978 um einhaltliche kommunikation zwischen allen Systemen zu ermöglichen (IBM <=> DEV)

Die Ziele beim Erschaffen des OSI-Modells waren also:

> unabhängikeit vom Hersteller 
> unabhängikeit vom Betriebsystem


## Aufbau und Struktur

Das OSI-Modell beschreibt 7 Hierarische  Schichten die Jeweils auf der Sender als auch auf der Empfänger seite zu finden ist. Beim senden werden diese Schichten von Oben nach unten (7 --> 1) Durchgangen beim empfangen umgekehrt  von Unten nach Oben (1 --> 7).

**vorteile eines Hierarischen Schichten Modells:**

- Jede Schicht kann sich getrennt um eine Aufgabe kümmern 
- Leichte Austauschbarkeit/ Modular 
- Unabhängikeit vom Herrsteller, System und Hardware

#### OSI Schichten 

## OSI-Schicht 7 (Anwendungsschicht)

Die Anwendungsschicht Stellt Ein- und Ausgabe Punkte für die zu kommunizierenden Daten zur Verfügung.

## OSI-Schicht 6 (Darstellungsschicht)

Die Darstellungschicht sorgt für einheiltliche Datenformate (ASCII, JPEG, MP3, UTF, Unicode).

## OSI-Schicht 5 (Sitzungsschicht)

Die Sitzungsschicht baut Sitzungen(Sessions) auf,verwaltet sie und baut sie wieder ab.

## OSI-Schicht 4 (Transportschicht)

Bei der Transport Sicht geht es um die End-to-End Kommunikation also welches Program/ welcher Prozess empfängt die Daten bzw soll die Daten empfangen.

Um diese zuweisung zu ermöglichen werden port-adressen verwendet.

es wird Unterschieden zwischen Reservierten Ports und Registrierten Ports 

- Reservierte Ports (0-1023) sind von der IANA Organisation festgelegte Ports die eine bestimmte funktion erfüllen sollen diese sollten nicht vom User benutzt werden .

Beispiel:

80/TCP => wird benutzt um daten via http Protokoll zu senden

21/UDP => wird benutz um daten via ftp Protokoll zu senden

- Registrierte Ports (1024-49152) können vom User frei benutzt werden bzw können von Software frei benutzt werden (25565 standard port Minecraft-server)


Header Inhalt:
 - > Sender und Empfänger Port Nummer (jeweils 16 bit)
 - > Sequence Number (32 bit)
 - > Acknowledgement number (32 bit)
 - > header length (4 bits)
 - > flag bits URG, ACK, PSH, RST, SYN, FIN (jeweils 1 bit)
 - > Checksum (Prüfwert)

## OSI-Schicht 3 (Vermittlungsschicht)
sucht und findet einen Transportweg durch ein Verbundsnetzwerk (Mehrere Lan-Netzwerke die miteinander per router verbunden sind)

verwendet werden logische Adressen: Ip Adressen

Die Vermittlungsschicht arbeitet mit Datagrammen

Datagramme bestehen aus Header und dem Datenteil
aus OSI-Schicht 4 

Inhalt des Headers:

> Version

> Header Length

> Type of Service 

> Total Length

> Time To Live 

> Protokoll

> Headerprüfwert (Checksum)

> Quelladresse (ip)

> Zieladresse (ip)

## OSI-Schicht 2 (Sicherungsschicht)

Arbeitet mit Frames(Rahmen)

Frame = Header + Datagram aus OSI-Schicht 3 + Trailer

Inhalt des Headers:

> Absender Mac Adresse 

> Ziel Mac Adresse 

> Länge(Header + Datagram)

Inhalt des Trailers:

> Prüfwert (header + Datagram)

## OSI-Schicht 1 (Bitübertragungsschicht)

- Schicht liegt auf/in der Hardware
- Schicht hat zugriff auf das Übertragungsmedium (netzwerkkarte)
- Übertragungsgeschwindikeit wird festgelegt
- Überträgt einen Rohbitstrom 

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Kopplungselemente OSI Schicht 2
_____________________________
### Repeater

erhöht die maximale Übertragungsdistanz
durch das empfangen der reinkommenden daten und erneute senden dieser daten wird dieses regeneriert (zeichnung unten)

Hub (Multiport repeater)

gleiche funktionsweise wie der Repeater nur das das signal an alle am netzwerk angeschlossenen teilnehmer gesendet wird

### Bridge 

eine Bridge verbindet 2 Netzwerke mithilfe von Bridgeports und SAT(Source Adress Table)

im Source Adress Table stehen pro Spalte der Bridge Port zusammen mit allen, über den Bridgeport zu erreichenden Mac Adressen

### Switch (Multiport Bridge)

Gleiche Funktionsweise wie bei der Bridge nur mit mehr "Bridge-ports" die aber beim Switch "Switch Ports" genannt werden

<br>

<br>

<br>

<br>

<br>

<br>
## Kopplungselemente OSI Schicht 3
____________________________________________________
### Router

hat mindestens 2 Anschlüsse. welche Logische IP netzwerke verbindet
Um einen Router zu benutzen muss eine Routingtabelle erstellt werden
es gibt 2 verschiedene arten dies zu tun 

> **Statisches Routing**
Beim Statischen Routing muss der Netzwerk Administrator den Routing Table selbst anlegen

> **Dynamisches Routing**
Beim Dynamischen Routing wird mit hilfe von Protokollen der Routing Table Dynamisch Angelegt 

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## 3 way handshake

### Schritt: 1
Sender A sendet an Empfänger B:

> Zufällig generierte Sequenznummer

> Flag SYN auf 1



### Schritt: 2

Sender B bei erfolgreichem Empfang:
> wird eine neu zufällig generierte Sequenznummer

> Acknowledgement nummer ist die empfangene Sequenznummer + 1
> ACK und SYN Flag geschickt 


### 

Sender A sendet bei erfolgreichem empfang:
>  als Sequenznummer die vorher empfangene Acknowledgement nummer 

> als Acknowledgement nummer die vorher empfangene Sequenznummer + 1

> setzt die SYN Flag auf 0
