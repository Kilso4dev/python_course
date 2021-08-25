# Cheatsheet Python
Dies soll eine kleine Zusammenfassung der wichtigsten Python-Kenntnisse sein.
Eine ausfuehrliche Variante is [hier](https://www.pythoncheatsheet.org) zu finden.

## Datentypen

| Datentyp    | Beschreibung                                                 |
| ----------- | ------------------------------------------------------------ |
| `bool`      | binaerer Wert(`True`, `False`)                               |
| `float`     | Gleitkommazahlen (`.0`, `1.`, `3.14152`)                     |
| `string`    | Zeichenketten (`"Thisisatest"`, `'Hallo Welt!'`) -> UTF-8    |
| `list`      | Veraenderbare listen (`['Hey', 'du']`, `[10, 1, 2, 3, 10]`)  |
| `tuple`     | nicht-veraenderbare listen (`('Test1', 10, 0.1)`)            |
| `bytes`     | binaere Raepresentation von Daten (immutable, `0(0x00) < x < 255(0xFF)`) (`b'\x00\x00\x00\x00\x00'`, `bytes('test', 'utf-8')`, `bytes(size)`) |
| `Bytearray` | Veraenderbares byte-array (binaere Daten)                    |
| `complex`   | Komplexe Zahlen (`complex(r, i)`)                            |


## Operatoren
- Boolean
    - not;and;or;xor[^]
- Arithmetisch
    - `+`;`-`;`*`;`/`;`**`;`%`[modulo]
    - `+=`;`-=`;`*=`;`/=`;`%=`;`**=`
