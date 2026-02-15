# Scope Document Abschnitt-Templates - Deutsch

Professionelle Referenzanleitung für die Verfassung jedes Abschnitts eines Scope Documents auf Deutsch. Basierend auf RVT Scope Document Stil: partnerschaftsorientiert, evidenzbasiert und professioneller Ton.

---

## 1. Kontext & Ziele

**Zweck**: Etablieren Sie das geschäftliche Problem, rechtfertigen Sie den PoC-Ansatz und zeigen Sie, was während des Hackathons validiert wurde.

### Mustervorlagen

#### Muster A (Erkenntnisfokussiert)
"Während des Hackathons am {{DATUM}} haben {{KUNDE}} und One Thousand {{THEMA}} erkundet. Diese Erkundung offenbarte {{HACKATHON_ERKENNTNIS}}. Dieser PoC baut auf diesen validierten Annahmen auf, um eine produktionsreife {{USE_CASE}}-Lösung bereitzustellen."

#### Muster B (Herausforderungsfokussiert)
"{{KUNDE}} sieht sich derzeit mit einer bedeutenden Herausforderung bei {{GESCHÄFTSPROBLEM}} konfrontiert. Dies führt zu {{AUSWIRKUNG_DES_PROBLEMS}}. Während des Hackathons am {{DATUM}} haben wir demonstriert, dass {{HACKATHON_ERKENNTNIS}} diese Lücke adressieren kann. Dieser PoC-Umfang beschreibt, wie eine vollständige Lösung für {{USE_CASE}} entwickelt werden kann."

#### Muster C (Chancenfokussiert)
"Der Hackathon am {{DATUM}} mit {{KUNDE}} identifizierte eine Chance, {{CHANCE}} zu nutzen. Unsere Erkundung zeigte, dass {{HACKATHON_ERKENNTNIS}}. Dieser PoC wird diesen Proof-of-Concept in eine skalierbare, integrierte Lösung für {{USE_CASE}} transformieren."

### Zu verwendende Schlüsselphrasen
- "Während des Hackathons haben wir validiert..."
- "Die Erkundung offenbarte..."
- "Dies zeigt die Machbarkeit von..."
- "Basierend auf dieser Grundlage wird dieser PoC..."
- "One Thousand und {{KUNDE}} erkundeten die Schnittstelle zwischen..."

### Zu vermeidende Schlüsselphrasen
- "Wir werden erkunden, ob..." (suggeriert Unsicherheit, nicht Validierung)
- "Wir hoffen zu zeigen..." (passiv, nicht selbstbewusst)
- "Angeblich könnte das System..." (informell für professionelle Dokumente)
- Vage Verweise auf "Anforderungen" ohne Kontext

### Struktur
1. Eröffnungssatz: Was während des Hackathons erforscht wurde
2. Mittelsätze: Wichtige Erkenntnis aus dem Hackathon, warum sie wichtig ist
3. Schlusssatz: Wie dieser PoC auf dieser Grundlage aufbaut

### Variable Platzhalter
- `{{KUNDE}}`: Kundenunternehmen
- `{{DATUM}}`: Hackathon-Datum (z.B. "15.-16. März 2024")
- `{{THEMA}}`: Was der Hackathon erforscht hat (z.B. "KI-gestützte Dokumentenklassifizierung")
- `{{USE_CASE}}`: Der spezifische Anwendungsfall (z.B. "Rechnungsverarbeitungsautomation")
- `{{HACKATHON_ERKENNTNIS}}`: Wichtigste validierte Erkenntnis
- `{{GESCHÄFTSPROBLEM}}`: Die Herausforderung, der sich {{KUNDE}} stellt
- `{{AUSWIRKUNG_DES_PROBLEMS}}`: Wie es sie beeinflusst (Zeit, Kosten, Qualität)

### Längenvorgaben
- Mindestens 2-3 Sätze
- Maximal 5-6 Sätze
- Typisches Bereich: 150-250 Wörter

---

## 2. In-Scope Funktionen

**Zweck**: Beschreiben Sie genau, was gebaut wird, mit ausreichend Details, um bindend zu sein.

### Mustervorlagen

#### Abschnitts-Kopfzeilenformat
"### 2.1 [Funktionsname]"

#### Absatz-Einführungsmuster
"[Funktionsname] umfasst die Möglichkeit, {{AKTION}} durch {{METHODE}} durchzuführen. Diese Funktion wird {{NUTZEN}}. Die Implementierung umfasst [spezifische Komponenten oder Integrationen]."

#### Mehrteiliges Funktionsmuster
"2.1 [Funktionsname] wird drei Kernfunktionen bieten:
- [Fähigkeit A]: [Einzeilenbeschreibung]
- [Fähigkeit B]: [Einzeilenbeschreibung]
- [Fähigkeit C]: [Einzeilenbeschreibung]

Die Funktion umfasst [zusätzlicher Kontext]. {{KUNDE}} kann [greifbares Ergebnis] erreichen."

### Lieferumfang-Format
Nach jeder Funktionsbeschreibung sollten Aufzählungspunkte für konkrete Liefergegenstände enthalten sein:

```
**Lieferumfang:**
- [Spezifische Komponente/Funktion]
- [Technisches Implementierungsdetail]
- [Integrationspunkt]
- [Benutzer-sichtbare Fähigkeit]
```

### Häufige KI-Funktionen - Schreibmuster

#### Datenenextraktions-Funktion
"2.1 Automatische Datenextraktion ermöglicht dem System, [Schlüsselinformationen] aus [Dokumenttyp] zu identifizieren und zu extrahieren. Mit Hilfe von [Extraktionsmethode] analysiert das System [Dokumentstruktur] und füllt [Zielformat] mit {{GENAUIGKEITSRATE}}% Genauigkeit. {{KUNDE}}-Benutzer können [Benutzeraktion] durchführen und reduzieren damit die manuelle Dateneingabe um geschätzte {{ZEIT_GESPART}}."

**Lieferumfang:**
- Extraktionsmodell trainiert auf [Datenquelle]
- API-Endpunkt akzeptiert [Eingabeformat]
- Ausgabeschema passt zu {{KUNDE}}'s Datenbankstruktur
- Zuverlässigkeitsbewertung für extrahierte Werte
- Überprüfungsschnittstelle mit menschlicher Einbindung

#### Klassifizierungs-Funktion
"2.2 Dokumentenklassifizierung klassifiziert [Dokumenttyp] automatisch in [Anzahl] vordefinierte Kategorien. Der Klassifizierer verwendet [Methode] und erreicht [Genauigkeitsmetrik] basierend auf [Trainingsdatenquelle]. Dies ermöglicht {{KUNDE}} [Workflow-Verbesserung], eliminiert [Schmerzpunkt]."

**Lieferumfang:**
- Klassifizierungsmodell mit [Anzahl] Ausgabekategorien
- Zuverlässigkeitsschwellen für automatische vs. manuelle Überprüfung
- API-Integration mit [Systemname]
- Admin-Dashboard zur Anzeige von Klassifizierungsgenauigkeitsmetriken
- Prozess zur Aktualisierung von Kategorien

#### Chatbot/Konversationsschnittstelle-Funktion
"2.3 Intelligente Abfrageschnittstelle ermöglicht {{KUNDE}}-Mitarbeitern, Fragen in natürlicher Sprache zu [Domäne] zu stellen. Das System versteht [Fragetypen] und ruft [Informationsquelle] ab, präsentiert Antworten in [Format]. Dies reduziert die Abhängigkeit von [manueller Prozess]."

**Lieferumfang:**
- Modell zum Verständnis natürlicher Sprache für [Domäne]
- Integration mit [Wissensquelle/Datenbank]
- Verwaltung des Gesprächskontexts
- Rückgriff auf menschliche Agenten, wenn [Bedingung]
- Mechanismus für Benutzerzufriedenheits-Feedback

#### Dashboard/Analyse-Funktion
"2.4 Executive Dashboard bietet Echtzeit-Sichtbarkeit in [Metriken]. Das Dashboard zeigt [Schlüsselmetriken], mit Drill-Down-Funktionalität zu [Detailebene]. {{KUNDE}}-Führungskräfte können [Geschäftsziel] überwachen und [Verbesserungschance] identifizieren."

**Lieferumfang:**
- Echtzeit-Datenverbindung zu [Datenquelle]
- Visualisierungskomponenten für [spezifische Metriken]
- Konfigurierbare Zeitbereichsfilter
- Export-Fähigkeit zu [Format]
- [Anzahl] vorkonfigurierte Berichtsvorlagen

#### API-Integrations-Funktion
"2.5 Integration mit [Externe System] ermöglicht nahtlosen Datenaustausch zwischen [System A] und [System B]. Die Integration wird [synchronisieren/austauschen/abrufen] [Datentyp] auf [Häufigkeit], stellt sicher, dass {{KUNDE}} eine einzige Datenquelle für [kritische Daten] beibehält."

**Lieferumfang:**
- OAuth/API-Authentifizierungskonfiguration
- Datentransformationslogik von [Quellformat] zu [Zielformat]
- Geplanter Synchronisierungsjob mit Fehlerbehandlung und Wiederholungslogik
- Audit-Log aller Datenübertragungen
- Dokumentation von Feldmappings

### Zu verwendende Schlüsselphrasen
- "Die Funktion ermöglicht es {{KUNDE}}, ..."
- "Diese Implementierung umfasst..."
- "Lieferumfang für diese Funktion ist..."
- "Das System wird automatisch..."
- "{{KUNDE}}-Benutzer können..."

### Zu vermeidende Schlüsselphrasen
- "Wir werden versuchen..." (unsicher)
- "Die Funktion könnte..." (Vorsichtssprache)
- "Best-Effort für..." (nicht bindend)
- Übermäßig technisches Jargon ohne Erklärung

### Struktur pro Funktion
1. Eröffnungssatz: Was die Funktion aus geschäftlicher Perspektive tut
2. Technische Details: Wie es funktioniert, Genauigkeit, Integrationen
3. Nutzenaussage: Was sich für {{KUNDE}} verbessert
4. Lieferumfang: Spezifische, messbare Ergebnisse

### Variable Platzhalter
- `{{AKTION}}`: Was Benutzer tun können (z.B. "Lieferanteninformationen aus Rechnungen extrahieren")
- `{{METHODE}}`: Wie es funktioniert (z.B. "ein Modell des maschinellen Lernens trainiert auf historischen Daten")
- `{{NUTZEN}}`: Warum es wichtig ist (z.B. "Verarbeitungszeit von 2 Stunden auf 5 Minuten pro Dokument reduzieren")
- `{{GENAUIGKEITSRATE}}`: Erwartete Leistung (z.B. "95%")
- `{{ZEIT_GESPART}}`: Zeiteinsparungen

### Längenvorgaben
- Mindestens 3 Absätze pro Hauptfunktion
- 1-2 Absätze für Nebenfunktionen
- Typisches Bereich: 200-400 Wörter pro Funktion
- 4-8 Punkte pro Lieferumfang-Liste

---

## 3. Out-of-Scope Funktionen

**Zweck**: Explizit angeben, was NICHT enthalten ist, um Scope Creep zu vermeiden.

### Mustervorlage

Verwenden Sie ein Bindestrich-separiertes Listenformat:

```
## 3. Out-of-Scope Funktionen

Die folgenden Elemente sind explizit aus dem PoC-Umfang ausgeschlossen:

— **[Funktionsname]**: [Kurzer Grund, warum ausgeschlossen oder verschoben]
— **[Funktionsname]**: [Kurzer Grund]
— **[Funktionsname]**: [Kurzer Grund]
```

### Häufige Out-of-Scope-Elemente

#### Produktionsimplementierung
"— **Produktionsumgebungsimplementierung**: Während der PoC vollständig funktionsfähig sein wird, ist die Bereitstellung in {{KUNDE}}'s Produktionsinfrastruktur, einschließlich Lastausgleich, Katastrophenwiederherstellung und produktionsreifer Sicherheitshärtung, außerhalb dieses Umfangs. Ein separates Implementierungs-Engagement würde für den Produktionsrollout erforderlich sein."

#### Datenmigration
"— **Migration historischer Daten**: Der PoC wird so konfiguriert, dass neue Daten akzeptiert und korrekt verarbeitet werden. Die Migration von {{KUNDE}}'s bestehenden historischen Daten aus [Altsystem] ist nicht enthalten. Ein separates Datenmigrationsprojekt könnte vor dem Produktionsstart erforderlich sein."

#### Benutzer-Schulung & Change Management
"— **Schulung für Endbenutzer**: Dieses Engagement umfasst nicht die Entwicklung von Schulungsmaterialien oder die Durchführung von Benutzerschulungen. {{KUNDE}} ist verantwortlich für Benutzertrainings basierend auf bereitgestellter Dokumentation und Schulungsumgebungszugriff."

#### Sicherheits-Audit
"— **Sicherheitsaudit & Compliance-Zertifizierung**: Während die Lösung Best Practices zur Sicherheit folgt, ist ein formales Sicherheitsaudit oder Compliance-Zertifizierung (z.B. SOC 2, ISO 27001) nicht in diesem Umfang enthalten."

#### Last-Tests & Performance-Optimierung
"— **Last-Tests & Performance-Optimierung**: Der PoC wird unter typischen Nutzungsmustern getestet. Umfassende Last-Tests für [Anzahl] gleichzeitige Benutzer und Optimierung für Spitzenleistung sind an ein Post-PoC-Engagement verschoben."

#### Custom-Integrationen (zusätzlich)
"— **Integration mit [Drittanbieter-System]**: Dieser PoC umfasst die Integration mit [System A]. Custom-Integrationen mit [System B] und [System C] sind nicht enthalten und würden einen separaten Umfang erfordern."

#### Mehrsprachige Unterstützung
"— **Mehrsprachige Lokalisierung**: Der PoC wird auf Englisch bereitgestellt. Übersetzung zu [anderen Sprachen] und Lokalisierung für regionale Märkte sind nicht enthalten."

#### Erweiterte Analytik
"— **Erweiterte prädiktive Analytik**: Der PoC umfasst grundlegende Dashboards und Berichterstattung. Modelle des maschinellen Lernens basierend auf Vorhersagen für [Anwendungsfall] sind an eine zukünftige Phase verschoben."

#### Mobile-Anwendung
"— **Mobile-Anwendung**: Dieser PoC konzentriert sich auf webgestützten Zugriff. Die Entwicklung von nativen Mobil-Anwendungen für iOS und Android ist nicht enthalten."

#### Custom-Hardware-Integration
"— **Custom-Hardware-Integration**: Die Lösung wird auf Standard-Server-Infrastruktur ausgeführt. Die Integration mit [spezifische Hardware/Geräte] ist nicht enthalten."

### Zu verwendende Schlüsselphrasen
- "explizit aus diesem Umfang ausgeschlossen"
- "außerhalb dieses PoCs"
- "an eine zukünftige Phase verschoben"
- "nicht in diesem Engagement enthalten"
- "könnte in einem nachfolgenden Projekt erforderlich sein"

### Zu vermeidende Schlüsselphrasen
- "Wir werden nicht..." (zu informell)
- "Vielleicht später..." (vage)
- "Wahrscheinlich außerhalb des Umfangs..." (unsicher)
- Einfach nur Elemente auflisten ohne Erklärung

### Struktur pro Element
1. Funktions-/Elementname in Fettdruck
2. Klarer Grund, warum es ausgeschlossen oder verschoben ist
3. Falls zutreffend, Vorschlag, wann es adressiert werden könnte

### Variable Platzhalter
- `{{KUNDE}}`: Kundenname
- `{{SYSTEM}}`: Systemnamen
- `{{ALTSYSTEM}}`: Das System, das ersetzt/integriert wird
- `{{ZEITRAUM}}`: Zeitrahmen, falls zutreffend

### Längenvorgaben
- 1 Satz pro Out-of-Scope-Element
- 40-80 Wörter pro Element
- Liste mit 4-8 Elementen typisch
- Gesamtabschnitt: 200-400 Wörter

---

## 4. Architekturdiagramm

**Zweck**: Bieten Sie eine visuelle Darstellung des vorgeschlagenen Systemdesigns mit kurzer erklärter Erklärung.

### Mustervorlagen

#### Einfache Architektur-Einleitung
"Das folgende Architekturdiagramm illustriert das vorgeschlagene Systemdesign für {{USE_CASE}}. Das Design trennt Belange über drei Schichten: [Schicht 1], [Schicht 2] und [Schicht 3]. Diese Architektur stellt sicher, dass [Nutzen], erfüllt {{KUNDE}}'s Datenverwaltungsstandards und bietet klare Trennung zwischen [Belang A] und [Belang B]."

#### Integrations-fokussierte Architektur-Einleitung
"Die vorgeschlagene Architektur für {{USE_CASE}} integriert {{KUNDE}}'s bestehende Systeme mit neuen KI-Funktionen. [System A] dient als primäre Datenquelle, [System B] behält die einzige Datenquelle, und die neue [Komponente] verarbeitet und bereichert Daten bevor [Ergebnis]. Dieser Ansatz stellt sicher, dass {{KUNDE}} die Kontrolle über [kritischer Aspekt] behält, während [Technologie] für [Nutzen] genutzt wird."

#### Multi-Komponenten-Architektur-Einleitung
"Die Lösung besteht aus vier Hauptkomponenten: (1) [Komponente A] für [Funktion], (2) [Komponente B] für [Funktion], (3) [Komponente C] für [Funktion] und (4) [Komponente D] für [Funktion]. Daten fließen von [Quelle] durch [Verarbeitung] und führen zu [Ergebnis]. Dieses Design ermöglicht [Nutzen] und minimiert [Risiko]."

### Zu beschreibende Schlüsselelemente nach dem Diagramm
- Primäre Datenflüsse und ihre Richtung
- Systemgrenzen und Sicherheitszonen
- Integrationen von Drittanbietern und ihre Rolle
- Wo {{KUNDE}}'s Daten gespeichert und verarbeitet werden
- Wie das System [kritischen Prozess] handhabt

### Zu verwendende Schlüsselphrasen
- "Die Architektur besteht aus..."
- "Daten fließen von [Quelle] zu [Ziel]..."
- "Dieses Design stellt sicher, dass..."
- "[Komponente] ist verantwortlich für..."
- "Das System integriert sich mit [externem Service]..."

### Zu vermeidende Schlüsselphrasen
- "Wir könnten verwenden..." (unsicher, gehört zu zukünftigen Phasen)
- "Das Diagramm zeigt, was wir wahrscheinlich bauen werden..." (Vorsichtssprache)
- Unerklärte technische Begriffe ohne geschäftlichen Kontext

### Was NICHT in der Architektur-Sektion enthalten sein sollte
- Implementierungsdetails, die zu Funktionsbeschreibungen gehören
- Spezifische Tool-/Bibliotheks-Auswahlmöglichkeiten (gehören zu technischen Spezifikationen)
- Bereitstellungsarchitektur (das ist getrennt vom logischen Design)
- Code-Schnipsel oder Pseudocode

### Struktur
1. Eröffnungssatz: Was das Diagramm zeigt
2. Schichten-/Komponenten-Übersicht: Hauptkomponenten und ihr Zweck
3. Datenfluss-Erklärung: Wie Informationen durch das System fließen
4. Wichtigste Vorteile: Warum diese Architektur gewählt wurde

### Variable Platzhalter
- `{{USE_CASE}}`: Der spezifische Anwendungsfall (z.B. "Rechnungsautomation")
- `{{NUTZEN}}`: Warum diese Architektur wichtig ist (z.B. "Skalierbarkeit und Wartbarkeit")
- `{{KOMPONENTE}}`: Systemkomponentenname

### Längenvorgaben
- Einleitung-Text: 150-250 Wörter
- Tatsächliches Architekturdiagramm enthalten (Miro, Lucidchart oder ähnlich)
- Diagrammtext minimal und klar halten

---

## 5. Voraussetzungen von {{KUNDE}}

**Zweck**: Klar angeben, was der Kunde liefern muss, damit der PoC erfolgreich ist.

### Mustervorlagen

#### Standard-Voraussetzungen-Format
```
## 5. Voraussetzungen von {{KUNDE}}

Damit dieser PoC erfolgreich ist, muss {{KUNDE}} bereitstellen:

- [Voraussetzungselement] - [Beschreibung] - {{STATUS}}
- [Voraussetzungselement] - [Beschreibung] - {{STATUS}}
- [Voraussetzungselement] - [Beschreibung] - {{STATUS}}
```

#### Voraussetzungen mit Status-Indikatoren
```
**Datenzugriffs-Voraussetzung:**
- Zugriff auf [System/Datenbankname] - Lesezugriff auf [spezifische Tabellen/Endpunkte] erforderlich für [Zweck] - Status: {{STATUS}}
  - {{KUNDE}} Besitzer: [Rolle]
  - Zeitrahmen: Sollte verfügbar sein bis [Datum]
  - Aufwand zur Bereitstellung: [Schätzung, z.B. "1-2 Stunden"]

**Domänen-Experte-Voraussetzung:**
- [Anzahl] Stunden pro Woche Fachexperten-Verfügbarkeit - Für Anforderungsklärung, Terminologie-Validierung und [spezifischer Anwendungsfall]. Mindestens [X] Stunden pro Sprint - Status: {{STATUS}}
  - {{KUNDE}} Besitzer: [Name/Rolle]
  - Empfohlene Besprechungshäufigkeit: [Häufigkeit]

**Infrastruktur-Voraussetzung:**
- [Infrastruktur-Anforderung] - {{KUNDE}} muss [Beschreibung] bereitstellen. Geschätzte Kapazität: [Spezifikation] - Status: {{STATUS}}
  - {{KUNDE}} Besitzer: [Rolle]
  - Zeitrahmen: Bereit bis [Datum]
```

### Häufige Voraussetzungen

#### API-Zugriff
"- **API-Zugriff zu [Systemname]**: Lese- und Schreibzugriff auf {{KUNDE}}'s [Systemname] API, mit Anmeldedaten zur Authentifizierung als [Integrations-Benutzer]. Erforderlich für [Datenquelle/Ziel]-Operationen. Status: {{STATUS}}"

#### Beispieldaten / Trainingsdaten
"- **Repräsentative Beispieldaten**: [Anzahl] Beispiel-Datensätze von [System/Prozess] mit [Datentypen]. Diese Daten werden verwendet für [Modelle trainieren/Extraktionsregeln konfigurieren/Funktionalität demonstrieren]. Status: {{STATUS}}"

#### Fachexperten-Verfügbarkeit
"- **Fachexperten-Verfügbarkeit**: [X] Stunden pro Woche Verfügbarkeit von {{KUNDE}}'s [Domäne]-Experte für Anforderungsvalidierung, Test-Case-Überprüfung und Terminologie-Klärung. Empfohlene Besprechungshäufigkeit: [Häufigkeit]. Status: {{STATUS}}"

#### Test-Umgebung
"- **Test-Umgebungsverifügung**: Dedizierte Test-Instanz von [Systemname] mit [Spezifikationen], wo One Thousand [installieren/testen/integrieren] kann ohne Auswirkung auf Produktion. Status: {{STATUS}}"

#### IT-Infrastruktur-Zugriff
"- **IT-Infrastruktur-Zugriff**: Netzwerkzugriff auf [Systeme], Datenbank-Verbindungszeichenfolge für [Datenbank] und geeignete Firewall-Regelzulassungen für [Services]. Status: {{STATUS}}"

#### Geschäftsprozess-Dokumentation
"- **Dokumentation des aktuellen Prozesses**: Dokumentation oder Videos von {{KUNDE}}'s aktuellem [Prozess], einschließlich [spezifischer Schritte]. Dies informiert unser [Verständnis/Anforderungen/Test-Cases]. Status: {{STATUS}}"

#### Genehmigungsprozess / Unterschriften
"- **Interessensvertreter-Genehmigung**: {{KUNDE}} wird [Rolle] ernennen, der [Entscheidungen/Änderungen] während des PoCs genehmigen kann. One Thousand benötigt dokumentierte Entscheidungen bis [Datum] zu [Themen]. Status: {{STATUS}}"

#### Feedback & Test-Ressourcen
"- **Benutzer-Test-Teilnahme**: [Anzahl] {{KUNDE}}-Endbenutzer verfügbar, um an [Test-Aktivitäten/UAT] auf [Häufigkeit] teilzunehmen. Status: {{STATUS}}"

### Status-Indikatoren
- ✓ Bestätigt - Kunde hat Verfügbarkeit bestätigt
- ⏳ In Bearbeitung - Kunde arbeitet an Bereitstellung
- ⚠ Risiko - Potenzielle Blocker identifiziert
- ❌ Noch nicht adressiert - Noch zu besprechen

### Zu verwendende Schlüsselphrasen
- "{{KUNDE}} muss bereitstellen..."
- "Erforderlich für {{USE_CASE}} um..."
- "Besitzer: {{KUNDE}} [Rolle]"
- "Zeitrahmen: Verfügbar bis [Datum]"
- "Geschätzter Aufwand zur Bereitstellung: [Schätzung]"

### Zu vermeidende Schlüsselphrasen
- "Wir hoffen, dass {{KUNDE}} könnte..." (passiv)
- "Idealerweise würde {{KUNDE}}..." (unsicher)
- "Falls möglich..." (Vorsichtssprache)

### Struktur
1. Gruppierung nach Kategorie (Daten, Infrastruktur, Personen, Ressourcen)
2. Spezifische Anforderungsbeschreibung
3. Warum es benötigt wird (Zweck)
4. Aktueller Status
5. Verantwortliche {{KUNDE}}-Partei
6. Zeitrahmen für Verfügbarkeit

### Variable Platzhalter
- `{{KUNDE}}`: Kundenunternehmen
- `{{STATUS}}`: ✓ Bestätigt, ⏳ In Bearbeitung, ⚠ Risiko, ❌ Nicht adressiert
- `{{USE_CASE}}`: Der spezifische Anwendungsfall
- `{{ROLLE}}`: Berufsbezeichnung bei {{KUNDE}}

### Längenvorgaben
- 1 Zeile pro unkomplizierte Voraussetzung
- 2-3 Zeilen pro komplexe Voraussetzung
- Gesamtliste: 6-12 Elemente typisch
- Gesamtabschnitt: 300-500 Wörter

---

## 6. Sprint-Design

**Zweck**: Skizzieren Sie den Entwicklungszeitplan, Lieferumfang pro Sprint und wichtigste Meilensteine.

### Mustervorlagen

#### Standard-Sprint-Format
```
## 6. Sprint-Design

Der PoC wird über {{SPRINT_ANZAHL}} Sprints von jeweils {{SPRINT_LÄNGE}} Wochen bereitgestellt.

### Sprint 0: Grundlagen & Setup ({{DAUER}})
**Ziel**: Entwicklungsumgebung etablieren, Datenquellen integrieren und technischen Ansatz validieren.

**Wichtigste Aktivitäten**:
- [Aktivitätsbeschreibung]
- [Aktivitätsbeschreibung]
- [Aktivitätsbeschreibung]

**Lieferumfang**:
- [Spezifische arbeitende Komponente]
- [Integration/Konfiguration]
- [Dokumentation oder Artefakt]

**Erfolgskriterien**:
- [Messbare Bedingung]
- [Messbare Bedingung]

---

### Sprint 1: [Funktionsname] ({{DAUER}})
**Ziel**: [Was in einem Satz erreicht wird]

**Wichtigste Aktivitäten**:
- [Aktivität]
- [Aktivität]

**Lieferumfang**:
- [Funktionskomponente]
- [Test/Validierungs-Artefakt]

**Erfolgskriterien**:
- [Funktion funktioniert wie spezifiziert]
- [Performance-Schwelle erreicht]
```

#### Multi-Sprint-Funktions-Bereitstellung
"### Sprint 1-2: [Funktionsname] Entwicklung ({{DAUER}})"

### Häufige Sprint-Typen

#### Sprint 0 / Grundlagen-Sprint
```
### Sprint 0: Grundlagen & Setup (1 Woche)
**Ziel**: Vorbereitung der Entwicklungsinfrastruktur und Validierung technischer Annahmen aus dem Hackathon.

**Wichtigste Aktivitäten**:
- Konfiguration der Entwicklungsumgebung und Code-Repository
- Herstellung von Datenverbindungen zu {{KUNDE}}'s [Systemname]
- Validierung des Zugriffs auf [Datenquellen] und Bestätigung der Datenstruktur-Annahmen
- Durchführung der technischen Architektur-Überprüfung mit {{KUNDE}}-Interessensvertretern
- Einrichtung von Logging, Überwachung und lokalem Test-Framework

**Lieferumfang**:
- Entwicklungsumgebung vollständig funktionsfähig und dokumentiert
- Bestätigte Datenintegration funktioniert end-to-end
- Technisches Design-Dokument überprüft und von {{KUNDE}} genehmigt
- Definition von Done Standards etabliert

**Erfolgskriterien**:
- Entwicklungsteam kann Funktionen lokal erstellen und testen
- Daten fließen korrekt von {{KUNDE}}-Systemen zu Entwicklungsumgebung
- Technische Risiken identifiziert und Risikominderungspläne vorhanden
- {{KUNDE}} technische Interessensvertreter haben den Ansatz genehmigt
```

#### Funktions-Implementierungs-Sprint
```
### Sprint 1: [Funktionsname] Kernfunktionalität (1 Woche)
**Ziel**: Lieferung der Kernfunktionalität für [Funktion], einschließlich Datenverarbeitung und Benutzeroberfläche.

**Wichtigste Aktivitäten**:
- Implementierung von [spezifische Komponente] basierend auf [Ansatz]
- Erstellung von [Benutzeroberfläche/API-Endpunkte] für {{KUNDE}}, um [Benutzeraktion] durchzuführen
- Erstellung von [unterstützender Infrastruktur] für [Zweck]
- Entwicklung von Unit-Tests mit [Abdeckungsprozentsatz]
- Durchführung der internen Code-Überprüfung

**Lieferumfang**:
- Arbeitsfähige [Funktion] zugänglich via [Schnittstelle]
- Unit-Test-Suite mit [X%] Code-Abdeckung
- API-Dokumentation (falls zutreffend)
- Bericht zum internen Test mit bekannten Einschränkungen

**Erfolgskriterien**:
- Funktion [spezifische Kriterien]
- Leistung erfüllt [Schwelle]
- Code besteht Quality Gates
- {{KUNDE}} technisches Team kann überprüfen und testen
```

#### Test & Verfeinerungs-Sprint
```
### Sprint 2: Testen, Verfeinerung & Integration (1 Woche)
**Ziel**: Validierung von [Funktion] gegen {{KUNDE}}-Anforderungen, Fehlerbehebung und Vorbereitung für Übergabe.

**Wichtigste Aktivitäten**:
- Durchführung des {{KUNDE}} User Acceptance Testing mit [Teilnehmer]
- Dokumentation und Behebung identifizierter Probleme
- Verfeinerung [spezifische Bereiche] basierend auf Feedback
- Vorbereitung von Schulungsmaterialien und Benutzerdokumentation
- Performance-Tests und Optimierung

**Lieferumfang**:
- Aktualisierte Funktion mit allen von UAT identifizierten Fehlern behoben
- Benutzerdokumentation und [Typ]-Schulungsmaterialien
- Performance-Test-Ergebnisse und Optimierungsbericht
- Protokoll bekannter Probleme (falls vorhanden) mit Workarounds

**Erfolgskriterien**:
- {{KUNDE}} genehmigt Funktion für Produktion
- Alle kritischen und hochpriorität Probleme behoben
- Dokumentation vollständig und überprüft
- Keine offenen Blocker für Bereitstellung
```

#### Finaler Sprint (Übergabe)
```
### Sprint 3: Finales Testen, Dokumentation & Übergabe ({{DAUER}})
**Ziel**: Durchführung der finalen Qualitätssicherung, Vorbereitung der Betriebsdokumentation und Wissenstransfer zu {{KUNDE}}.

**Wichtigste Aktivitäten**:
- End-to-End-System-Tests in {{KUNDE}}'s Test-Umgebung
- Erstellung von [Betriebsdokumentation] für {{KUNDE}} IT-Team
- Durchführung der [Support-Team]-Schulung zu [Systembetrieb/Fehlerbehebung]
- Vorbereitung des Produktions-Bereitstellungs-Runbook
- Erstellung von [Wissenstransfer-Artefakten]

**Lieferumfang**:
- Finaler Qualitätssicherungs-Bericht
- Betriebsrunbooks und Fehlerbehebungs-Leitfäden
- Schulungsmaterialien für [Support/Betrieb/Endbenutzer]
- Produktions-Bereitstellungsplan und Checkliste
- Dokumentation zum Wissenstransfer

**Erfolgskriterien**:
- {{KUNDE}} Support-Team kann System betreiben und Fehlersuche durchführen
- Alle Dokumentation vollständig und überprüft
- Null-Blocker-Ebenen-Fehler verbleibend
- {{KUNDE}} bereit für Produktions-Übergabe
```

### Zu verwendende Schlüsselphrasen
- "Sprint [N] konzentriert sich auf..."
- "Lieferumfang für diesen Sprint:"
- "Erfolgskriterien umfassen..."
- "Wichtigste Meilensteine: [Datum], [Datum]..."
- "Am Ende von Sprint [N] wird {{KUNDE}} haben..."

### Zu vermeidende Schlüsselphrasen
- "Wir werden versuchen..." (unsicher)
- "Je nach Problemen..." (vage)
- "Hoffentlich werden wir abschließen..." (unprofessionell)

### Struktur pro Sprint
1. Sprint-Titel und Dauer
2. Zielaussage (ein Satz)
3. Wichtigste Aktivitäten (3-5 Elemente)
4. Spezifischer Lieferumfang (3-5 Elemente)
5. Klare Erfolgskriterien (2-3 messbare Elemente)

### Variable Platzhalter
- `{{SPRINT_ANZAHL}}`: Gesamtzahl von Sprints (z.B. "3")
- `{{SPRINT_LÄNGE}}`: Länge jedes Sprints (z.B. "1-Wochen")
- `{{DAUER}}`: Dauer dieses Sprints (z.B. "1 Woche")
- `{{FUNKTIONSNAME}}`: Funktion wird gebaut
- `{{KUNDE}}`: Kundenname

### Längenvorgaben
- Sprint 0: 200-300 Wörter
- Funktions-Sprints: 250-350 Wörter jede
- Finaler Sprint: 250-350 Wörter
- Gesamtabschnitt: 1000-1500 Wörter für 3-4 Sprint PoC

---

## 7. Fazit

**Zweck**: Schließen Sie professionell ab, verstärken Sie die Partnerschaft und bereiten Sie die Phase vor.

### Mustervorlagen

#### Partnerschaftsfokussierte Abschluss
"One Thousand freut sich darauf, mit {{KUNDE}} bei dieser {{USE_CASE}}-Initiative zusammenzuarbeiten. Wir glauben, dass der vorgeschlagene Umfang einen erreichbaren, großen Einfluss PoC darstellt, der [Nutzen] ermöglicht. Unser Team bringt [relevante Expertise], und wir sind verpflichtet, eine Lösung bereitzustellen, die [angegebenes Ziel] adressiert. Wir freuen uns auf [nächster Schritt] und auf die Unterstützung von {{KUNDE}}'s [strategischem Ziel] durch dieses Engagement."

#### Wertefokussierte Abschluss
"Dieser PoC wird {{KUNDE}} ermöglichen, [Hauptnutzen]. Durch Lieferung von [Ergebnis] wird {{KUNDE}} positioniert für [strategischen Vorteil]. Das Team von One Thousand ist bereit, die Arbeit am [Datum] zu beginnen. Wir sind zuversichtlich, dass der vorgeschlagene Umfang erreichbar ist und bei Abschluss des PoC im [Zeitrahmen] messbaren Nutzen liefert."

#### Handlungsorientierte Abschluss
"One Thousand ist bereit, den {{USE_CASE}} PoC zu starten. Der nächste Schritt ist, [spezifische Aktion] von {{KUNDE}} bis [Datum] durchzuführen, was es uns ermöglicht, am [Datum] zu starten. Wir werden formal am [Datum] mit {{KUNDE}} Führungs- und technischem Team starten. Bitte bestätigen Sie Ihre Verfügbarkeit und lassen Sie uns wissen, ob Sie Fragen zu diesem Scope-Dokument haben. Wir freuen uns, loszulegen."

### Zu beinhaltende Schlüsselelemente
- Wiederholungsbewertung des Wertversprechen
- Bestätigung der Bereitschaft zum Fortfahren
- Verweis auf den nächsten Schritt oder Kickoff
- Positiver, zukunftsorientierter Ton
- Kontaktinformationen oder nächster Besprechung-Termin

### Zu verwendende Schlüsselphrasen
- "One Thousand freut sich darauf, ..."
- "Dieser PoC wird {{KUNDE}} ermöglichen, ..."
- "Wir sind verpflichtet, ..."
- "Der nächste Schritt ist ..."
- "Wir freuen uns auf ..."

### Zu vermeidende Schlüsselphrasen
- "Wir hoffen, dass das funktioniert..." (unsicher)
- "Daumen gedrückt..." (informell)
- "Falls alles gut geht..." (Vorsichtssprache)
- Ungestützte Optimismus über Ergebnisse

### Struktur
1. Eröffnung: Partnerschaftsbestätigung und Wertaussage
2. Mitte: Wiederholung von Schlüsselnutzen
3. Abschluss: Nächste Schritte und Bereitschaftsbestätigung

### Variable Platzhalter
- `{{KUNDE}}`: Kundenunternehmen
- `{{USE_CASE}}`: Der spezifische Anwendungsfall
- `{{NUTZEN}}`: Wichtigste Nutzen aus diesem PoC
- `{{DATUM}}`: Nächster Meilenstein-Termin (Kickoff, Dokument-Genehmigung, usw.)
- `{{ZEITRAHMEN}}`: PoC-Abschluss-Zeitrahmen

### Längenvorgaben
- Mindestens 3-4 Sätze
- Maximal 4-5 Sätze
- Typisches Bereich: 150-250 Wörter

### Beispiel-Gesamtabschluss
"One Thousand freut sich darauf, mit {{KUNDE}} bei dieser Rechnungsautomations-Initiative zusammenzuarbeiten. Dieser PoC wird {{KUNDE}} ermöglichen, die Rechnungsverarbeitungszeit von 45 Minuten auf unter 10 Minuten pro Dokument zu reduzieren und dadurch die Effizienz der Kreditorenbuchhaltung dramatisch zu verbessern. Wir sind verpflichtet, eine robuste, gründlich getestete Lösung bereitzustellen, die {{KUNDE}} bis Ende Q2 selbstbewusst in Produktion einsetzen kann.

Der nächste Schritt ist die Bestätigung der in Abschnitt 5 aufgeführten Voraussetzungen und die Genehmigung dieses Scope-Dokuments durch {{KUNDE}}. Wir sind bereit, am 22. März zu starten und innerhalb von vier Wochen messbaren Einfluss zu liefern. Bitte lassen Sie uns wissen, wenn Sie Fragen haben oder einen Aspekt des vorgeschlagenen Umfangs besprechen möchten."

---

## Schreibstil-Richtlinien für alle Abschnitte

### Ton
- Professionell, aber nicht steif
- Selbstbewusst und Fähigkeits-fokussiert
- Partnerschaftsorientiert (verwenden Sie "wir" und "unser")
- Nutzen-fokussiert (betonen Sie {{KUNDE}}-Ergebnisse)
- Evidenzbasiert (alles verfolgt zum Hackathon oder angegebenen Anforderungen)

### Struktur
- Klare Abschnittskopfzeilen mit Nummerierung
- Themensätze am Anfang von Absätzen
- Aufzählungspunkte für Listen verwandter Elemente
- Kurze Absätze (3-5 Sätze typisch)
- Vermeiden Sie Textwände

### Sprache
- Aktivstimme bevorzugt: "Das System wird extrahieren..." nicht "Extraktion wird durchgeführt..."
- Spezifische und konkrete Sprache
- Technische Begriffe bei erster Verwendung definieren
- Konsistente Verwendung von Terminologie durchgehend (wechseln Sie nicht zwischen "extrahieren," "analysieren," "identifizieren" für dasselbe Konzept)
- Marketingjargon oder unbegründete Superlative vermeiden

### Was macht einen guten Scope Document Abschnitt
- ✓ Jede Behauptung verfolgt zur Hackathon-Dokumentation oder Benutzer-Notizen
- ✓ Funktionen werden mit ausreichenden Details beschrieben, um bindend zu sein
- ✓ {{KUNDE}}-Nutzen werden explizit angegeben
- ✓ Voraussetzungen sind klar und umsetzbar
- ✓ Zeitplan und Lieferumfang sind spezifisch
- ✓ Out-of-Scope-Elemente verhindern Scope Creep
- ✓ Keine unerklärten Jargons oder technischen Akronyme
- ✓ Konsistente Verwendung von Terminologie
- ✓ Nutzen überwiegt Aufwand (apparent in tone)

### Häufige Fehler zu vermeiden
- ✗ Vage Sprache: "Wir werden unser Bestes geben," "hoffentlich," "wir werden versuchen"
- ✗ Ungestützte Behauptungen: "Dies wird 50% Zeit sparen" (ohne Beweis)
- ✗ Erfundene Details: Funktionen nicht im Hackathon, erfundener Zeitplan, fiktive Metriken
- ✗ Inkonsistente Terminologie: Wechsel zwischen "Benutzer," "Operator," "Administrator"
- ✗ Fehlende Voraussetzungen: Annahme, dass Kunde Systeme/Ressourcen hat ohne zu angeben
- ✗ Scope Creep: Funktionen, die out-of-scope sind, nicht explizit als solche aufgelistet
- ✗ Undefinierten Akronyme: Verwendung von "DAG," "ETL," "RAG" ohne Erklärung bei erster Verwendung
