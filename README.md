# TeamTux-Game-Project: TuxTris

## Anleitung
- Eine Konsole mit einer Höhe von mindestens 27 Zeilen öffnen
- Spiel auf der Konsole starten mit `python3 tetris.py` oder eine Release-Binary ausführen (sofern verfügbar)
- Die fallenden Tetrominos sollten lückenfüllend angeordnet werden
- Steuerung per Tastendruck:
```
Tetromino nach links bewegen:   a
Tetromino nach rechts bewegen:  d
Tetromino rotieren:             w
Tetromino nach unten bewegen:   s
Spiel beenden:                  q
```
- Komplett gefüllte Zeilen (ohne Lücken) werden gegen die Erhöhung des Spielstandes entfernt
- Kann ein Tetromino auf Grund eines zu hohen Unterbau nicht vollständig in das Spielfeld fallen, so ist das Spiel beendet

## Projektplanung
- Feature Branch Workflow
- Projektziele werden in GitHub Issues formuliert
- Gemeinsam coden (Turnus)
- Treffen/Arbeiten mindestens 1x pro Woche
- PEP8 Style Guide für Python Code
- Dokumentationen und Präsentationen befinden sich im docs Ordner

## Blöcke/Figuren (auch Tetrominoe) (7)

```
[1][ ][ ][ ]    [ ][4][4][ ]    [7][ ][ ][ ]
[1][1][1][ ]    [4][4][ ][ ]    [7][ ][ ][ ]
[ ][ ][ ][ ]    [ ][ ][ ][ ]    [7][ ][ ][ ]
[ ][ ][ ][ ]    [ ][ ][ ][ ]    [7][ ][ ][ ]

[ ][ ][2][ ]    [ ][5][ ][ ]
[2][2][2][ ]    [5][5][5][ ]
[ ][ ][ ][ ]    [ ][ ][ ][ ]
[ ][ ][ ][ ]    [ ][ ][ ][ ]

[3][3][ ][ ]    [ ][ ][ ][ ]
[ ][3][3][ ]    [ ][6][6][ ]
[ ][ ][ ][ ]    [ ][6][6][ ]
[ ][ ][ ][ ]    [ ][ ][ ][ ]
```
