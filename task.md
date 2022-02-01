# Datenbeschreibung

Der Bundesstaat Berlin veröffentlicht jährlich die Details von staatlichen Ausgaben. Die Datensatz und Dateidefinitionen sind zu finden unter:

- https://www.berlin.de/sen/finanzen/service/zuwendungsdatenbank/

Ein Auszug der Dateien:

| Name                                                                     | Geber               | Art              | Jahr | Anschrift                       | Politikbereich | Zweck                                      | Betrag |
| ------------------------------------------------------------------------ | ------------------- | ---------------- | ---- | ------------------------------- | -------------- | ------------------------------------------ | ------ |
| ImPULS e. V.                                                             | Bezirksamt Neukölln | Projektförderung | 2016 | Bat-Yam-Platz 1, 12353 Berlin   | Bildung        | Sprachschulungen für aktive Gropiusstädter | 6607   |
| Verein zur Förderung der Kommunikation unter Gropiusstädter Frauen e. V. | Bezirksamt Neukölln | Projektförderung | 2016 | Löwensteinring 22, 12353 Berlin | Familie        | Kinderbildungscafe                         | 2499   |
| Verein zur Förderung der Kommunikation unter Gropiusstädter Frauen e. V. | Bezirksamt Neukölln | Projektförderung | 2016 | Löwensteinring 22, 12353 Berlin | Jugend         | Service Learning                           | 15363  |

# Aufgabenbeschreibung

## Klassifizierung

Einzelne Ausgaben müssen basierend auf Zweck Felde, in den passenden Politikbereich zugeordnet werden.

## Clustering/Topic Modelling (Optional bei Werkstudenten)

In der Praxis fehlen die Kategorie-Kennzeichnungen. Um dieses Problem beheben zu können, wird nach Gruppierungen in dem Datensatz gesucht. Deine Aufgabe ist es, diese Gruppierungen anhand einer Kombination der Felder Zweck und Name zu finden.

Unsere Erwartung an dich:

Ziel ist es, eine mögliche Zusammenarbeit zwischen dir und BANKSapi zu simulieren. Bitte entwickle deine Lösung in einer ähnlichen wie der unsrigen Umgebung – nicht maßgeblich, aber willkommen:

- Docker Container für die Standardisierung unserer Umgebungen
- Python3, scikit-learn Stack, TensorFlow, xgBoost, nltk, gensi, spacy (Du kannst ebenso eine andere Bibliotheken benutzen, bitte dokumentiere die Abhängigkeiten ausführlich)
- Cloud-AI Plattformen für das Training
- Jupyter Notebooks für die gemeinsame Zusammenarbeit

Bitte zeig uns, dass du Grundkenntnisse über Data Science besitzt und sie anwendest:

- Sicherung der Datenqualität
- Validierung deiner Modelle
- Deine Modelle sollen in der Lage sein, Predictionsanfragen zu beantworten

Wir lieben diese [Haiku](https://www.python.org/dev/peps/pep-0020/#id4):

> Beautiful is better than ugly.

> Explicit is better than implicit.

> Simple is better than complex.

> Complex is better than complicated.

# Bedingungen

- **Deadline**: Bitte gib uns mit einer E-Mail Bescheid, wie lange für du diese Aufgabe brauchen würdest. Wir wollen messen, wie gut du bist mit Zeitplanung.
- **Format**: githup Repo, gezipped
- **Inhalt**: Code, Ergebnissen, Dokumentation
- **Rückfragen**: per e-Mail an HR, unsere Data Scientist antworten deine Fragen
- **Nächster Schritt**: Unsere Data Scientist werden sich deine Lösung ansehen. Wenn sie zufrieden sind, wirst du in einem Call sie kennenlernen und deine Lösung vorstellen
