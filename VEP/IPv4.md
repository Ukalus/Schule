#### IPv4

IPv4 Adressen bestehen aus 32 bits

    haben 2 informationsanteile
        Netz(werk)anteil
        Hostanteil

    benötigen eine Subnetzmaske, die ebenfalls aus 32 bits besteht und die eine Zeiger funktion hat 

    netzwerkadresse is wenn im host anteil alle bits auf null stehen
    jedes IP netzwerk hat seine eigene Broadcast adresse. alle bits müssen im host anteil dabei auf 1 stehen
    
mit hilfe einer Subnetzmaske kann man sehen wie die teile verteilt sind 

Adresse: 12580
Subnetz: 11100

Ergebnis: die Zahlen 1,2 und 5 sind der Netzwerkanteil
          die Zahlen 8 und 0 sind der Hostanteil

jede Subnetzmaske beginnt mit 1 und hat genau einen einzigen wechsel auf die null

von der 32 bit großen IP range wird eine unterteilung in klassen(A,B,C,D,E) unterteilt vorgenommen (nur A,B,C relevant)

Klasse A:
    Subnetzmaske: 255.0.0.0 oder /8
    erste Netzadresse : 1.*.*.*
    letzte NetzAdresse : 126.*.*.*
    erste Hostadresse : *.0.0.1
    letzte Hostadresse : *.255.255.254
    Testzwecke: 127.*.*.*
    Localhost: 127.0.0.1
Klasse B:
    Subnetzmaske: 255.255.0.0 oder /16 

Klasse C:
    Subnetzmaske: 255.255.255.0 oder /24