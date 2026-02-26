# Section Templates — Deutsch

Schreibmuster, Wortbudgets und Stilrichtlinien fur den Inhalt jeder Folie in der Kick-Off-Prasentation.

---

## Allgemeine Schreibprinzipien

1. **Prasentationsfolien, keine Absatze** — Jeder Aufzahlungspunkt muss in 2-3 Sekunden erfassbar sein
2. **Aktive Sprache** — "Daten analysieren" statt "Die Daten werden analysiert"
3. **Kundenvokabular** — Begriffe des Kunden verwenden (ihre Produktnamen, nicht generische Bezeichnungen)
4. **Konkret statt allgemein** — "4 Sprints uber 16 Wochen" statt "mehrere Entwicklungsphasen"
5. **Kein Fulltext** — "Um zu", "Es ist wichtig zu beachten, dass" streichen
6. **Parallele Struktur** — Wenn der erste Punkt mit einem Verb beginnt, beginnen alle mit Verben
7. **Gedankenstriche fur strukturierte Inhalte** — Format: "Titel — Beschreibung" bei Risiken, Phasen, Sprint-Zielen
8. **Metriken nur aus Quellmaterial** — Keine erfundenen Zahlen; `[Zu bestatigen]` verwenden wenn unsicher
9. **Ehrlich aber konstruktiv** — Risiken benennen, ohne Defaitismus
10. **Zielgruppenorientiert** — Jede Folie beantwortet: "Warum ist das fur mich relevant?"

---

## Power Verbs Liste

Aktionsverben fur Sprint-Ziele, Phasenbeschreibungen und Lieferergebnisse:

**Daten & Analyse:**
- Analysieren, Parsen, Extrahieren, Einlesen, Erfassen, Importieren, Profilieren, Bewerten

**Design & Aufbau:**
- Gestalten, Bauen, Prototypen, Entwickeln, Implementieren, Konfigurieren, Bereitstellen, Konzipieren

**Validierung & Qualitat:**
- Validieren, Verifizieren, Testen, Prufen, Auditieren, Bestatigen, Benchmarken, Evaluieren

**Prozess & Lieferung:**
- Ausfuhren, Liefern, Releasen, Ausrollen, Launchen, Ubergeben, Veroffentlichen, Bereitstellen

**Zusammenarbeit & Kommunikation:**
- Abstimmen, Koordinieren, Moderieren, Prasentieren, Dokumentieren, Schulen, Onboarden, Briefen

**Optimierung & Iteration:**
- Optimieren, Verfeinern, Erweitern, Verbessern, Iterieren, Ausbauen, Skalieren, Tunen

**Integration & Verbindung:**
- Integrieren, Verbinden, Synchronisieren, Migrieren, Verknupfen, Anbinden, Einbetten, Koppeln

**Beispiele:**
- "Bestehende Datenpipelines analysieren" (nicht "Daten anschauen")
- "Kern-Matching-Engine prototypen" (nicht "Eine erste Version bauen")
- "Output-Genauigkeit gegen historische Daten validieren" (nicht "Schauen ob es funktioniert")
- "MVP in Staging-Umgebung bereitstellen" (nicht "Irgendwo zum Testen hinstellen")

---

## Regeln fur parallele Struktur

**Regel**: Wenn das erste Element einer Liste mit einem Verb beginnt, MUSSEN alle mit Verben beginnen. Gleiches gilt fur Nomen, Adjektive oder Prapositionalphrasen.

**Schlechtes Beispiel (gemischt):**
```
- Eingehende Kundenanfragen analysieren
- Matching-Algorithmus entwickeln
- Das System generiert Entwurfsvorschlage
```

**Gutes Beispiel (parallele Verben):**
```
- Eingehende Kundenanfragen analysieren
- Matching-Algorithmus entwickeln
- Entwurfsvorschlage generieren
```

**Schlechtes Beispiel (gemischte Sprint-Titel):**
```
Sprint 1: Datenbasis
Sprint 2: Den Kern-Motor bauen
Sprint 3: Integrationsphase
Sprint 4: Nutzertests und Feedback
```

**Gutes Beispiel (parallele Nominalphrasen):**
```
Sprint 1: Datenbasis
Sprint 2: Kern-Engine
Sprint 3: Systemintegration
Sprint 4: Nutzervalidierung
```

---

## 1. Titelfolie

**Wortbudget:** 20 Worter
**Ton:** Kraftig, markenkonform
**Platzierung:** Erste Folie

### Vorlage

```
{TAGLINE}

{USE_CASE_TITEL}

Projekt Kick-Off | TT.MM.JJJJ
```

### Tagline-Muster

```
{CLIENT} MIT KI STARKEN
```

### Beispiel

```
HABA MIT KI STARKEN

Produktberater — Intelligente Empfehlungs-Engine

Projekt Kick-Off | 15.03.2026
```

### Regeln

- Tagline ist IMMER in Grossbuchstaben
- Muster verwenden: "{CLIENT} MIT KI STARKEN" — konsistent uber alle Kick-Offs
- Use-Case-Titel folgt der Tagline; kann einen Gedankenstrich-Untertitel enthalten
- Datumsformat: `Projekt Kick-Off | TT.MM.JJJJ`
- Kein Logo- oder Bildhinweis — das kommt aus dem Design-System
- Gesamttext unter 20 Worter halten

---

## 2. Check-In

**Wortbudget:** 30 Worter gesamt (2-3 Fragen)
**Ton:** Locker, Eisbrecher
**Platzierung:** Fruhe Folie (Folie 2-3)
**Uberschrift:** WIR STELLEN UNS ERSTMAL VOR

### Standardfragen (Empfohlen)

```
Wie bin ich heute da? | 1 Adjektiv
Was sind meine Erwartungen an diesen Kick-Off?
```

### Alternative Fragen

```
Was begeistert mich am meisten an diesem Projekt?
Wie sieht eine erfolgreiche Zusammenarbeit fur mich aus?
Was wurde ich als erstes bei {client_name} automatisieren?
```

### Beispiel

```
WIR STELLEN UNS ERSTMAL VOR

Wie bin ich heute da? | 1 Adjektiv
Was sind meine Erwartungen an diesen Kick-Off?
```

### Regeln

- Maximal 3 Fragen; 2 ist bevorzugt fur Kick-Offs (kurzer als Hackathons)
- Erste Frage ist immer eine personliche Vorstellungsaufforderung
- Zweite Frage verankert Erfolgskriterien fur die Sitzung
- Fragen mussen offen sein (kein Ja/Nein)
- Fragen NICHT zu lang oder formell machen
- KEINE technischen Fragen — das ist ein Eisbrecher
- Fragen NICHT vorab beantworten
- "Wie bin ich heute da? | 1 Adjektiv" ist das Standardformat fur deutsche Kick-Offs

---

## 3. Pain x Data Folie — DIE ANWENDUNG

**Wortbudget:** 120 Worter gesamt (40 Pain, 40 Data, 40 Solution)
**Ton:** Problemorientiert aber konstruktiv; datenbasiert
**Platzierung:** Fruh-mittlere Folie (Kontextsetzung)
**Uberschrift:** NO PAIN, NO GAIN (bleibt Englisch)

### Layout: Drei Spalten

```
PAIN                     DATEN                    LOSUNG
(3-5 Punkte)             (3-5 Punkte)             (2-3 Punkte)
```

### Pain-Spalte — Vorlagen

**Volumen/Kapazitats-Muster:**
```
~{Zahl} {Aufgaben} pro {Zeitraum} werden manuell bearbeitet und binden {Team}-Kapazitat.
```
Beispiel: `~200 Produktanfragen pro Woche werden manuell bearbeitet und binden Vertriebskapazitat.`

**Zeitverschwendungs-Muster:**
```
Zu viel Zeit fur {Aktivitat}: {spezifische Details}.
```
Beispiel: `Zu viel Zeit fur Produktsuche: Kundenbeschreibungen manuell mit Katalogartikeln abgleichen.`

**Fehler/Qualitats-Muster:**
```
Hohe Fehlerquote bei {Prozess} aufgrund von {Ursache}.
```
Beispiel: `Hohe Fehlerquote bei Produktempfehlungen aufgrund unvollstandiger Kundenanforderungen.`

**Format/Kanal-Muster:**
```
{Elemente} kommen in unterschiedlichen Formaten ({Liste}), erfordern manuelle Interpretation.
```
Beispiel: `Kundenanfragen kommen in unterschiedlichen Formaten (E-Mail, Telefon, Chat), erfordern manuelle Interpretation.`

**Engpass-Muster:**
```
{Aktivitat} ist ein Engpass: {Grund}, fuhrt zu {Konsequenz}.
```
Beispiel: `Produktzuordnung ist ein Engpass: keine automatisierte Suche, fuhrt zu 20-minutigen Verzogerungen pro Anfrage.`

### Pain-Spalte — Regeln

- Mit dem wirkungsvollsten oder quantifizierbaren Schmerzpunkt beginnen
- Mindestens eine Metrik/Zahl einbeziehen, wenn aus Quellmaterial verfugbar
- Eigene Worte und Terminologie des Kunden verwenden
- Jeder Punkt muss eigenstandig verstandlich sein
- KEINE Metriken erfinden — `[Zu bestatigen]` verwenden wenn Zahlen nicht in der Quelle sind
- 3-5 Punkte, jeweils 8-15 Worter

### Daten-Spalte — Vorlagen

**Strukturierte-Daten-Muster:**
```
{System} enthalt {Datentyp}: {Details zu Umfang, Format oder Abdeckung}.
```
Beispiel: `ERP-System enthalt Produktstammdaten: 5.000+ Artikel mit Spezifikationen und Preisen.`

**Unstrukturierte-Daten-Muster:**
```
{Quelle} liefert {Datentyp} in {Format}: {Umfang oder Abdeckungsdetail}.
```
Beispiel: `E-Mail-Archiv liefert historische Anfragen als Freitext: 3 Jahre Kundenkorrespondenz.`

**Externe-Daten-Muster:**
```
{Externe Quelle} bietet {Datentyp}: {Relevanz fur den Anwendungsfall}.
```
Beispiel: `Produktkataloge bieten Kategoriehierarchien: strukturierte Taxonomie fur Empfehlungslogik.`

### Daten-Spalte — Regeln

- Nur Daten auflisten, die tatsachlich existieren und zuganglich sind
- Spezifische Formate nennen (PDF, Excel, E-Mail, API, Datenbank)
- Ungefahres Volumen angeben wenn bekannt
- Bei unsicherer Datenverfugbarkeit mit `[Zu bestatigen]` markieren
- Auf Daten fokussieren, die den spezifischen Anwendungsfall unterstutzen
- 3-5 Punkte, jeweils 8-15 Worter

### Losungs-Spalte — Vorlagen

**Ergebnis-Muster:**
```
{Verb} {gewunschtes Ergebnis}, um {Nutzen} zu erzielen.
```
Beispiel: `Personalisierte Produktempfehlungen generieren, um Verkaufszyklen zu beschleunigen.`

**Automatisierungs-Muster:**
```
{Prozess} automatisieren — {Metrik} von {aktuell} auf {Ziel} reduzieren.
```
Beispiel: `Produktzuordnung automatisieren — Suchzeit von 20 Minuten auf Sekunden reduzieren.`

**Fahigkeits-Muster:**
```
{Team} befahigen, {neue Fahigkeit} mit KI-gestutztem {Tool/Prozess} auszufuhren.
```
Beispiel: `Vertriebsteam befahigen, mehr Kunden mit KI-gestutzter Produktberatung zu bedienen.`

### Losungs-Spalte — Regeln

- 2-3 Punkte, die direkt die Schmerzpunkte adressieren
- Jede Losung sollte mindestens einem Schmerzpunkt zugeordnet sein
- Auf gewunschte Ergebnisse fokussieren, nicht auf technische Umsetzung
- Aktive Verben verwenden (Generieren, Automatisieren, Befahigen, Reduzieren, Beschleunigen)
- Ambitioniert aber realistisch — keine Versprechen, die das Projekt nicht halten kann

### Vollstandiges Beispiel

```
PAIN:
- ~200 Produktanfragen pro Woche werden manuell bearbeitet, binden Vertriebskapazitat
- Zu viel Zeit fur den Abgleich von Kundenbeschreibungen mit Katalogprodukten
- Inkonsistente Empfehlungen je nach Berater
- Kein systematischer Weg fur Cross-Selling oder Upselling
- Kundenwartezeiten von durchschnittlich 2+ Tagen bei komplexen Produktfragen

DATEN:
- Produktstammdaten: 5.000+ Artikel mit Spezifikationen, Preisen und Verfugbarkeit
- 3 Jahre historische Anfrage-Antwort-Paare im E-Mail-Archiv
- Kundenkaufhistorie im CRM: Bestellmuster und Praferenzen
- Produktkatalog mit Kategoriehierarchien und Kompatibilitatsregeln

LOSUNG:
- Personalisierte Produktempfehlungen in Echtzeit generieren
- Produktzuordnung automatisieren — Antwortzeit von Tagen auf Minuten reduzieren
- Konsistente, datengetriebene Beratung fur das gesamte Vertriebsteam ermoglichen
```

---

## 4. Projektablauf — Schritt fur Schritt

**Wortbudget:** 60 Worter gesamt, 4 Punkte, je 1 Satz
**Ton:** Sequenziell, klar, vorwartsbewegend
**Platzierung:** Projektuberblick-Bereich
**Uberschrift:** PROJEKTABLAUF

### Phasenstruktur

```
Phase 1: MVP — {Beschreibung des Prototyps/Hackathon-Ergebnisses}
Phase 2: Daten-Vertiefung — {Beschreibung der Datenvalidierung und -anreicherung}
Phase 3: Erweiterung — {Beschreibung der Feature-Erweiterung und Integration}
Phase 4: Nutzer-Feedback — {Beschreibung der Tests und Iteration}
```

### Vorlage

```
{Phasennummer}: {Phasenname} — {Ein Satz, der die Kernaktivitat und das Lieferergebnis beschreibt}.
```

### Standard-Phasennamen (DE)

| Phase | Name | Fokus |
|-------|------|-------|
| 1 | MVP | Prototyp aus dem Hackathon; Kernfunktionalitat validieren |
| 2 | Daten-Vertiefung | Daten bereinigen, anreichern und Pipelines validieren |
| 3 | Erweiterung | Features ausbauen, mit Produktivsystemen integrieren |
| 4 | Nutzer-Feedback | Endnutzer-Tests, Iteration und Ubergabevorbereitung |

### Beispiel

```
Phase 1: MVP — Funktionsfahigen Prototyp aus dem Hackathon mit Kern-Matching-Logik und Basis-UI liefern.
Phase 2: Daten-Vertiefung — Datenqualitat validieren, Pipelines anreichern und Genauigkeit gegen echte Falle benchmarken.
Phase 3: Erweiterung — Mit Produktiv-ERP/CRM integrieren, erweiterte Features und Sonderfallbehandlung hinzufugen.
Phase 4: Nutzer-Feedback — User-Acceptance-Tests durchfuhren, Feedback sammeln und vor Release iterieren.
```

### Regeln

- Genau 4 Phasen — das ist die Standard-Kick-Off-Struktur
- Jede Phase ist 1 Satz, 12-18 Worter
- Phase 1 referenziert immer das Hackathon-/Prototyp-Ergebnis
- Phase 4 beinhaltet immer Endnutzer-Validierung
- Gedankenstrich (—) zur Trennung von Phasenname und Beschreibung verwenden
- Parallele Struktur uber alle 4 Beschreibungen einhalten
- Phasennamen kurz halten (2-3 Worter maximal)
- KEINE Daten hier einfugen — Daten gehoren in die Zeitplan/Gantt-Folie

---

## 5. Sprint-Ziele

**Wortbudget:** 200 Worter gesamt, ~50 pro Sprint (fur 4 Sprints)
**Ton:** Ergebnisorientiert, spezifisch
**Platzierung:** Detailplanungsbereich
**Quelle:** Sprint-Design-Plan
**Uberschrift:** IN SPRINTS ERREICHEN WIR DAS PROJEKTZIEL IN AGILER ARBEITSLOGIK

### Vorlage — Einzelner Anwendungsfall

```
**Sprint {N}: {Sprint-Titel}**
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis}
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis}
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis}
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis} [optional 4.]
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis} [optional 5.]
```

### Vorlage — Mehrere Anwendungsfalle

```
**Sprint {N}: {Sprint-Titel}**
UC1 ({Anwendungsfall-Name}):
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis}
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis}

UC2 ({Anwendungsfall-Name}):
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis}
- {Lieferergebnis-Verb} {spezifisches Lieferergebnis}
```

### Standard-Sprint-Progression

| Sprint | Typischer Titel | Fokus |
|--------|----------------|-------|
| 1 | Grundlagen & Daten | Datenpipelines, Umgebungsaufbau, initiales Modell |
| 2 | Kernlogik | Hauptalgorithmus/-modell, primare Integrationen |
| 3 | Integration & Feinschliff | Ende-zu-Ende-Ablauf, UI, Systemanbindungen |
| 4 | Tests & Ubergabe | UAT, Dokumentation, Deployment-Vorbereitung |

### Beispiel — Einzelner Anwendungsfall

```
**Sprint 1: Grundlagen & Daten**
- Entwicklungs- und Staging-Umgebungen aufsetzen
- Daten-Ingestion-Pipeline fur Produktstammdaten bauen
- Historische Anfragedaten profilieren und bereinigen
- Genauigkeits-Baselines mit Testdatensatz etablieren

**Sprint 2: Kern-Matching-Engine**
- Produkt-Matching-Algorithmus mit Katalog-Taxonomie entwickeln
- Kundenkontext aus CRM-Datensatzen integrieren
- Empfehlungs-Ranking und Scoring-Logik aufbauen

**Sprint 3: Integration & UI**
- Mit Produktiv-ERP per API fur Live-Produktdaten verbinden
- Berater-Interface mit Empfehlungsanzeige bauen
- Feedback-Schleife fur Empfehlungsqualitat implementieren
- Cross-Selling- und Upselling-Vorschlagslogik erganzen

**Sprint 4: Tests & Ubergabe**
- User-Acceptance-Tests mit 3-5 Vertriebsberatern durchfuhren
- Systemarchitektur und Betriebshandbuch dokumentieren
- Deployment-Paket und Monitoring-Dashboards vorbereiten
- Abschlussprasentation und Wissenstransfer-Session liefern
```

### Beispiel — Mehrere Anwendungsfalle

```
**Sprint 1: Grundlagen & Daten**
UC1 (Produktberater):
- Daten-Ingestion-Pipeline fur Produktkatalog bauen
- Historische Anfrage-Antwort-Paare profilieren

UC2 (Bestellautomatisierung):
- Bestellvorlagen aus E-Mail-Archiv extrahieren
- Bestellfelder auf ERP-Datenmodell mappen

**Sprint 2: Kernlogik**
UC1 (Produktberater):
- Matching-Algorithmus mit Kategorie-Taxonomie entwickeln
- Empfehlungs-Scoring-Engine aufbauen

UC2 (Bestellautomatisierung):
- Bestell-Parsing und Feldextraktion-Pipeline bauen
- Validierungsregeln gegen Produktstamm implementieren
```

### Regeln

- Jeder Sprint bekommt einen **fetten Titel** gefolgt von 3-5 Lieferergebnis-Punkten
- Punkte beginnen mit Aktionsverben (Bauen, Entwickeln, Integrieren, Testen, Bereitstellen, Dokumentieren, usw.)
- Parallele Struktur innerhalb jedes Sprints einhalten
- Sprints mussen aufeinander aufbauen (keine isolierten Sprints)
- Bei Multi-UC: klar kennzeichnen, welche Lieferergebnisse zu welchem Anwendungsfall gehoren
- Gesamt uber alle 4 Sprints: ~200 Worter
- Jeder Punkt: 8-15 Worter, ein spezifisches Lieferergebnis
- KEINE Daten einfugen — Daten gehoren in die Zeitplan/Gantt-Folie
- Alle Lieferergebnisse aus dem Sprint-Design-Plan beziehen; KEINE Features erfinden

---

## 6. Zeitplan / Gantt

**Wortbudget:** Minimaler Text — dies ist eine visuelle/strukturelle Folie
**Ton:** Sachlich, kalenderbasiert
**Platzierung:** Planungsbereich, nach Sprint-Zielen
**Uberschrift:** ZEITPLAN

### Strukturmuster

```
           | {MON1} | {MON2} | {MON3} | {MON4} | {MON5} | {MON6} |
           | KW{nn} | KW{nn} | KW{nn} | KW{nn} | KW{nn} | KW{nn} |
-----------+--------+--------+--------+--------+--------+--------+
Kick-Off   |   X    |        |        |        |        |        |
{Aufgabe1} |  ████  |  ████  |        |        |        |        |
{Aufgabe2} |        |  ████  |  ████  |  ████  |        |        |
{Aufgabe3} |        |        |        |  ████  |  ████  |        |
Release    |        |        |        |        |        |   X    |
-----------+--------+--------+--------+--------+--------+--------+
Sprint 1   |  ████  |  ████  |        |        |        |        |
Sprint 2   |        |  ████  |  ████  |        |        |        |
Sprint 3   |        |        |  ████  |  ████  |        |        |
Sprint 4   |        |        |        |  ████  |  ████  |        |
```

### Kopfzeile — Monatsnamen (DE)

```
JAN | FEB | MAR | APR | MAI | JUN | JUL | AUG | SEP | OKT | NOV | DEZ
```

### Kalenderwochen

```
KW01 | KW02 | KW03 | ... | KW52
```
"KW" (Kalenderwoche) als Prafix in der deutschen Version verwenden.

### Standard-Aufgabenzeilen

| Zeile | Beschreibung |
|-------|-------------|
| Kick-Off | Einzelmarkierung (X) am Projektstartdatum |
| {Projektspezifische Aufgaben} | Balken uber relevante Wochen; abgeleitet aus Sprint-Zielen |
| Release Party | Einzelmarkierung (X) am Projektenddatum |

### Sprint-Balken-Positionierung

- Jeder Sprint umfasst typischerweise 3-4 Wochen
- Sprints sollten zusammenhangend sein (keine Lucken zwischen Sprints)
- Sprint-Balken erscheinen unterhalb der Aufgabenzeilen
- Sprints farblich oder per Label unterscheidbar machen

### Legende

```
Legende:
████ {CLIENT_NAME}    (kundenverantwortliche Aufgaben)
████ 1000             (One-Thousand-verantwortliche Aufgaben)
```

### Beispiel

```
           | MAR    | APR    | MAI    | JUN    | JUL    |
           | KW10   | KW14   | KW18   | KW22   | KW27   |
-----------+--------+--------+--------+--------+--------+
Kick-Off   |   X    |        |        |        |        |
Datenvorbr.|  ████  |  ████  |        |        |        |
Modellentw.|        |  ████  |  ████  |        |        |
Integration|        |        |  ████  |  ████  |        |
UAT & QS   |        |        |        |  ████  |  ████  |
Release    |        |        |        |        |   X    |
-----------+--------+--------+--------+--------+--------+
Sprint 1   |  ████  |  ████  |        |        |        |
Sprint 2   |        |  ████  |  ████  |        |        |
Sprint 3   |        |        |  ████  |  ████  |        |
Sprint 4   |        |        |        |  ████  |  ████  |

Legende:
████ HABA       ████ 1000
```

### Regeln

- Monatskopfzeile verwendet deutsche 3-Buchstaben-Abkurzungen (MAR, APR, MAI, JUN, JUL, AUG, SEP, OKT, NOV, DEZ)
- Wochennummern verwenden "KW"-Prafix (Kalenderwoche)
- Erste Zeile ist immer "Kick-Off"; letzte Zeile vor Sprints ist immer "Release Party" oder "Release"
- Projektspezifische Aufgabenzeilen zwischen Kick-Off und Release werden aus Sprint-Zielen abgeleitet
- Sprint-Balken an den abgedeckten Aufgabenzeilen ausrichten
- Legende unterscheidet Kundenaufgaben von One-Thousand-Aufgaben
- Aufgabennamen kurz halten (1-3 Worter)
- Diagramm NICHT uberladen — maximal 4-6 Aufgabenzeilen plus Sprint-Balken

---

## 7. Risiken

**Wortbudget:** 80 Worter gesamt
**Ton:** Ehrlich, proaktiv, losungsorientiert
**Platzierung:** Planungsbereich

### Layout: Zwei Spalten

```
WAS BEREITS PASSIERT IST           WELCHE RISIKEN SEHEN WIR
(2-4 Punkte)                       (2-4 Punkte)
```

### Linke Spalte — "Was bereits passiert ist"

**Zeitplan-Muster:**
```
{Ereignis} wahrend {Phase} fuhrte zu {Konsequenz}.
```
Beispiel: `Datenzugangsverzogerungen wahrend des Hackathons fuhrten zu reduzierter Testabdeckung.`

**Umfang-Muster:**
```
{Feature/Umfangspunkt} wurde aufgrund von {Grund} {verschoben/reduziert}.
```
Beispiel: `CRM-Integration wurde aufgrund von API-Verfugbarkeitseinschrankungen verschoben.`

**Qualitats-Muster:**
```
{Daten/System}-Qualitatsprobleme entdeckt: {spezifisches Detail}.
```
Beispiel: `Produktdaten-Qualitatsprobleme entdeckt: 15% der Artikel ohne Kategorielabel.`

### Rechte Spalte — "Welche Risiken sehen wir"

**Datenrisiko-Muster:**
```
{Datenquelle} konnte {Qualitats-/Verfugbarkeitsproblem} haben — Mitigation: {Massnahme}.
```
Beispiel: `Historische E-Mail-Daten konnten inkonsistente Formate haben — Mitigation: flexiblen Parser bauen.`

**Integrationsrisiko-Muster:**
```
{System}-Integration konnte durch {Abhangigkeit} verzogert werden — Mitigation: {Massnahme}.
```
Beispiel: `ERP-Integration konnte durch IT-Ressourcenverfugbarkeit verzogert werden — Mitigation: parallele Arbeitsstrome.`

**Adoptionsrisiko-Muster:**
```
Nutzerakzeptanz konnte langsamer als erwartet sein — Mitigation: {Massnahme}.
```
Beispiel: `Nutzerakzeptanz konnte langsamer als erwartet sein — Mitigation: Endnutzer ab Sprint 2 einbeziehen.`

**Scope-Risiko-Muster:**
```
Scope Creep durch {Quelle} — Mitigation: {Massnahme}.
```
Beispiel: `Scope Creep durch zusatzliche Anwendungsfalle — Mitigation: strenge Sprint-Backlog-Governance.`

### Standard-Risikomuster fur KI-Projekte

Diese Risiken gelten fur die meisten KI-Kick-Off-Projekte:

```
- Datenqualitatslucken konnten zusatzlichen Bereinigungsaufwand erfordern
- Modellgenauigkeit konnte beim ersten Durchlauf die Erwartungen nicht erfullen — Tuning-Sprints einplanen
- Integration mit Legacy-Systemen konnte undokumentierte Einschrankungen aufdecken
- Endnutzer-Vertrauen in KI-Empfehlungen erfordert schrittweises Onboarding
- Ressourcenverfugbarkeit auf Kundenseite konnte wahrend des Projekts schwanken
```

### Beispiel

```
WAS BEREITS PASSIERT IST:
- Datenzugang dauerte 2 Wochen langer als geplant wahrend des Hackathons
- Produktkatalog hatte 15% fehlende Kategorielabel — manuelle Anreicherung erforderlich
- CRM-API-Ratenlimits wahrend initialer Tests entdeckt

WELCHE RISIKEN SEHEN WIR:
- Historische Datenqualitat konnte vor Sprint 2 zusatzliche Bereinigung erfordern
- ERP-Integration konnte undokumentierte Geschaftsregeln aufdecken — Mitigation: fruhes IT-Alignment
- Nutzerakzeptanz braucht moglicherweise extra Onboarding — Mitigation: Co-Design-Sessions in Sprint 3
```

### Regeln

- Ehrlich sein uber Vergangenes — das baut Vertrauen beim Kunden auf
- Jedes Risiko in der rechten Spalte braucht eine Mitigationsmassnahme
- Gedankenstrich (—) zur Trennung von Risiko und Mitigation verwenden
- 2-4 Punkte pro Spalte; jeden Punkt unter 20 Wortern halten
- Nicht dramatisieren — Risiken als handhabbar mit guter Planung darstellen
- Mindestens ein nicht-technisches Risiko einbeziehen (Akzeptanz, Ressourcen, Scope)
- KEINE Risiken auflisten, die bereits vollstandig gelost sind — die gehoren in "Was bereits passiert ist"
- Risiken mussen spezifisch fur DIESES Projekt sein, nicht generische KI-Risiken

---

## 8. Teilnehmer / Meetings — ZUSAMMENARBEIT

**Wortbudget:** Variiert — strukturierter Inhalt
**Ton:** Organisiert, klar, handlungsorientiert
**Platzierung:** Zusammenarbeits-Bereich

### Uberschriften

- Teilnehmer: **UNSER PROJEKT HAT UNTERSCHIEDLICHE TEILNEHMER**
- Meetings: **WIR TREFFEN UNS REGELMAßIG UM DAS PROJEKT GEMEINSAM ZU BEGLEITEN**

### Teilnehmertypen

| Meeting-Typ | Haufigkeit | Typische Teilnehmer |
|------------|-----------|---------------------|
| Jour Fixe | WOCHENTLICH | Projektleiter, Entwickler, Kunden-PO |
| IT-Alignment | 14-TAGIG | IT-Architekten, Systemadmins, Security |
| Steering Committee | MONATLICH | Sponsoren, Abteilungsleiter, Projektleiter |
| Testing / UAT | NACH BEDARF | Endnutzer, QA, Product Owner |

### Meeting-Karten-Format

```
┌──────────────────────────────┐
│  {MEETING_TYP}               │
│  TAG: {Wochentag}            │
│  ZEIT: {HH:MM} - {HH:MM}    │
│  HAUFIGKEIT: {WOCHENTLICH/…} │
│  TEILNEHMER: {Liste}         │
└──────────────────────────────┘
```

### Haufigkeits-Labels (DE)

| Label | Bedeutung |
|-------|-----------|
| WOCHENTLICH | Jede Woche |
| 14-TAGIG | Alle zwei Wochen |
| MONATLICH | Einmal pro Monat |
| NACH BEDARF | Bei Bedarf |

### Beispiel

```
┌──────────────────────────────┐     ┌──────────────────────────────┐
│  JOUR FIXE                   │     │  IT-ALIGNMENT                │
│  TAG: Dienstag               │     │  TAG: Donnerstag             │
│  ZEIT: 10:00 - 10:30         │     │  ZEIT: 14:00 - 15:00         │
│  HAUFIGKEIT: WOCHENTLICH     │     │  HAUFIGKEIT: 14-TAGIG        │
│  TEILNEHMER:                 │     │  TEILNEHMER:                 │
│  - Projektleiter (1000)      │     │  - IT-Architekt (Kunde)      │
│  - Product Owner (Kunde)     │     │  - DevOps Lead (1000)        │
│  - Entwickler (1000)         │     │  - Security Officer (Kunde)  │
└──────────────────────────────┘     └──────────────────────────────┘

┌──────────────────────────────┐     ┌──────────────────────────────┐
│  STEERING COMMITTEE          │     │  TESTING / UAT               │
│  TAG: Erster Mittwoch/Monat  │     │  TAG: Nach Vereinbarung      │
│  ZEIT: 15:00 - 16:00         │     │  ZEIT: Variiert              │
│  HAUFIGKEIT: MONATLICH       │     │  HAUFIGKEIT: NACH BEDARF     │
│  TEILNEHMER:                 │     │  TEILNEHMER:                 │
│  - Projektsponsor (Kunde)    │     │  - Endnutzer (Kunde)         │
│  - Abteilungsleiter (Kunde)  │     │  - QA Lead (1000)            │
│  - Projektleiter (1000)      │     │  - Product Owner (Kunde)     │
└──────────────────────────────┘     └──────────────────────────────┘
```

### Regeln

- Jeder Meeting-Typ bekommt eine eigene Karte
- Alle Karten verwenden das gleiche Format: TAG / ZEIT / HAUFIGKEIT / TEILNEHMER
- Haufigkeits-Labels in GROSSBUCHSTABEN
- Teilnehmernamen im Rollenformat: "Rolle (Organisation)"
- Sowohl kundenseitige als auch 1000-seitige Teilnehmer einbeziehen
- Jour Fixe wird immer einbezogen — ist das primare Sync-Meeting
- Steering Committee wird immer einbezogen fur Sponsor-Sichtbarkeit
- IT-Alignment wird einbezogen wenn technische Integration involviert ist
- Testing/UAT wird einbezogen wenn Endnutzer-Validierung geplant ist
- Karten NICHT mit zu vielen Teilnehmern uberladen (3-5 pro Meeting)

---

## 9. Weitere Punkte / Diskussion

**Wortbudget:** 10-15 Worter (statischer Inhalt)
**Ton:** Offen, einladend
**Platzierung:** Gegen-Ende-Folie
**Uberschrift:** WIR SAMMELN AUSSTEHENDE ENTSCHEIDUNGEN UND FRAGEN

### Vorlage

```
WEITERE PUNKTE

Welche weiteren Fragen, Bedenken oder Ideen sollten wir heute noch besprechen?
```

### Regeln

- Dies ist eine uberwiegend statische Folie — minimaler Text
- Uberschrift ist immer "WEITERE PUNKTE"
- Einen offenen Impuls einbeziehen, der zum Gesprach einladt
- KEINE spezifischen Diskussionsthemen vorausfullen
- Diese Folie existiert, um Raum fur ungeplante Gesprache zu schaffen
- Den Impuls kurz und offen halten

---

## 10. Check-Out / Danke

**Wortbudget:** 20-30 Worter
**Ton:** Warm, wertschatzend, zukunftsgerichtet
**Platzierung:** Letzte Folie
**Uberschrift:** DANKE FUR EINEN SUPER KICK-OFF

### Vorlage

```
DANKE FUR EINEN SUPER KICK-OFF

Wann ist das Projekt ein Erfolg?
```

### Alternative Check-Out-Muster

```
DANKE FUR EINEN SUPER KICK-OFF
Wie fuhlt ihr euch nach dem Kick-Off?
```

```
DANKE FUR EINEN SUPER KICK-OFF
Was ist eure wichtigste Erkenntnis von heute?
```

```
DANKE FUR EINEN SUPER KICK-OFF
Auf was freut ihr euch am meisten in diesem Projekt?
```

### Regeln

- "DANKE FUR EINEN SUPER KICK-OFF" ist immer in Grossbuchstaben
- Genau eine Feedback-/Check-Out-Frage einbeziehen
- Die Frage sollte reflektiv und zukunftsgerichtet sein
- NICHT zu formell machen — das ist ein Abschlussmoment
- KEINE nachsten Schritte hier einfugen — die gehoren in die Zeitplan- oder Sprint-Ziele-Folien
- Kurz und positiv halten

---

## Gedankenstrich-Muster Zusammenfassung

Gedankenstriche (—) verwenden, um Titel von Beschreibungen in strukturierten Inhalten zu trennen. Das schafft Klarheit und visuellen Rhythmus.

**Wo Gedankenstriche verwenden:**
- Phasenbeschreibungen: "MVP — Funktionsfahigen Prototyp aus dem Hackathon liefern"
- Sprint-Titel: "Grundlagen & Daten — Pipelines bauen und Baselines etablieren"
- Risikopunkte: "Datenqualitatslucken — Mitigation: zusatzlicher Bereinigungs-Sprint"
- Schmerzpunkte: "Manueller Abgleich — 20 Minuten pro Anfrage ohne Automatisierung"

**Gedankenstrich-Beispiele:**
```
OK  Phase 1: MVP — Funktionsfahigen Prototyp mit Kern-Matching-Logik liefern.
OK  Datenqualitatslucken konnten Bereinigung erfordern — Mitigation: dedizierte Sprint-1-Aufgabe.
OK  Nutzerakzeptanz konnte langsamer sein — Mitigation: Co-Design-Sessions.

SCHLECHT Phase 1: MVP. Funktionsfahigen Prototyp mit Kern-Matching-Logik liefern.
SCHLECHT Phase 1: MVP: Funktionsfahigen Prototyp mit Kern-Matching-Logik liefern.
```

**Gedankenstrich-Formatierung in Markdown:**
```
- Titel — Beschreibungstext folgt hier
- Weiterer — Beschreibungstext hier
```

---

## Konfidenz-Bewertung & `[Zu bestatigen]`-Marker

Jeder Abschnitt sollte Konfidenzwerte berechnet haben. `[Zu bestatigen]` fur grenzwertige (60-74%) oder niedrige (<60%) Konfidenzpunkte verwenden.

**Wann `[Zu bestatigen]` verwenden:**
- Eine Metrik wird im Quellmaterial erwahnt, aber ist nicht exakt
- Ein System oder API wird erwahnt, aber nicht bestatigt
- Ein Zeitplan oder Lieferergebnis hangt von externen Faktoren ab
- Datenverfugbarkeit wird angenommen, aber nicht verifiziert
- Meeting-Termine oder Teilnehmer sind vorlaufig

**Beispiel:**
```
Hohe Konfidenz (85%+):
Sprint 1 liefert Datenpipeline und Genauigkeits-Baseline.

Mittlere Konfidenz (60-74%):
ERP-API-Endpunkt fur Live-Produktdaten [Zu bestatigen: erfordert IT-Alignment]

Niedrige Konfidenz (<60%):
Release-Datum Ziel: Juli 2026 [Zu bestatigen: hangt von Integrationskomplexitat ab]
```

**In der Prasentation:**
- Hohe Konfidenz: Ohne Vorbehalt einbeziehen
- Mittlere Konfidenz: Mit `[Zu bestatigen]`-Marker einbeziehen; wahrend Sprint 1 klaren
- Niedrige Konfidenz: Markieren und Nutzer bitten, wahrend der Kick-Off-Diskussion zu verifizieren

---

## Checkliste: Inhaltsqualitat

Vor der Erstellung jeder Folie prufen:

- [ ] Jede Metrik ist zum Quellmaterial ruckverfolgbar
- [ ] Parallele Struktur eingehalten (alle Punkte beginnen gleich)
- [ ] Power Verbs fur Aktionspunkte und Lieferergebnisse verwendet
- [ ] Gedankenstriche fur strukturierte Beschreibungen verwendet
- [ ] Kundenterminologie verwendet (nicht generische Begriffe)
- [ ] Keine erfundenen Details oder aspirative Behauptungen
- [ ] Wortbudget eingehalten
- [ ] Ton angemessen fur Kick-Off-Publikum (kollaborativ, nicht Verkaufs-Pitch)
- [ ] Konfidenzwert berechnet
- [ ] Handlungsfahig und spezifisch (nicht vage)
- [ ] Sprint-Ziele auf Sprint-Design-Plan ruckverfolgbar
- [ ] Risiken enthalten Mitigationen
- [ ] Zeitplan stimmt mit Sprint-Zielen uberein
