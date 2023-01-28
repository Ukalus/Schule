# 1. Schritt Vorgaben

- Fall 1: eine anzahl an Teilnetzen ist gegeben 
- Fall 2: oder eine anzahl der Teilnehmer des größten teilnetzes angegeben 

# 2. neue Subnetzmaske bestimmen (Fall basiert)

## Fall 1: Anzahl x an Teilnetzen ist gegeben
    - Bestimme wieviele Bits benötigt werden um x darzustellen
    - Alte Subnetzmaske + x

## Fall 2: Anzahl der Teinehmer des Größten Teilnetz x ist gegeben
    - Bestimme die anzahl an bits die benötigt werden um x darzustellen
    - x = x + 2 (für die Netzwerkadresse und Broadcastadresse)
    - Alte Subnetzmaske - x

# 3. Benutzbare Netzadressen bestimmen 

    - Durch den "Bit bereich" [Neue Subnetzmaske - Alte Subnetzmaske] durch iterieren

    Beispiel:
### Vorgegebene IP-Adresse
    172.20.0.0
### Alte Subnetzmaske:<br>
    11111111.11111111.111111 [00] .00000000 ODER /22
### Neue Subnetzmaske: <br>
    11111111.11111111.111111 [11] .00000000 ODER /24
### Bit Bereich: <br>
    11111111.11111111.111111 [11] .00000000

### Erstes Teil netz in Binär
    11111111.11111111.111111 [00] .00000000


# 4. Benutzbare Geräteadressen bestimmen


# 5. Benutzbare Sub-Netzadressen bestimmen


