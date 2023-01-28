SiloManager
- silos Silo[]
- SiloKeys: int[]

+ SiloManager(Silos: Silo[])
+ addSilo(silo: Silo)
+ removeSilo(silo: Silo)
+ transferBestand({siloA: Silo, bestand int}, {siloB: Silo, bestand: int})
+ changeBestand()






Silo

- siloNr: int
- kapazitaet: float
- bestand: float

+ Silo(siloNr: int, kapazitaet: float, bestand: float = 0)
+ getSiloNr(): int
+ getbestand(): float
+ getkapazität(): float
+ einlagern(menge float): self.bestand
+ auslagern(menge float): self.bestand
