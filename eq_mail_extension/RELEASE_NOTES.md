## Modul eq_mail_extension


#### 25.11.2016
#### Version 1.0.9
##### CHG
- Modulicon und Beschreibung angepasst. 

#### 24.11.2016
#### Version 1.0.8
##### FIX
- Print Statement entfernt.

#### 24.11.2016
#### Version 1.0.7
##### FIX
- BugFix: es wird jetzt danach abgefragt, ob der in der Datenbank (ir_values) vordefinierte Mail Server überhaupt noch vorhanden ist, bevor die Send-Methode ausgeführt wird.


#### 15.11.2016
#### Version 1.0.6
##### FIX
- Print Statement entfernt.

#### 15.11.2016
#### Version 1.0.5
##### FIX
- Übernahme einer Abfrage aus dem Equitania-Modul (siehe ReleaseNotes Equitania-Modul vom 15.01.2016: - Anpassung des Mailversandes: gültige E-Mailadresse für Return-Path)
- Durch Übernahme dieser Abfrage wird nun wieder gewährleistet, dass bei installiertem eq_mail_extension Modul auch die dazugehörige send Methode ausgeführt wird (vorher wurde die def send Methode vom Equitania Modul ausgeführt, diese ist nun aber nicht mehr vorhanden, da Übernahme der Logik in die def send des eq_mail_extension Moduls).

#### 13.07.2016
#### Version 1.0.4
##### FIX
- Übersetzungsfehler beseitigt: "The two new passwords do not match." ----> "Die neuen (vorher: alten) Passwörter stimmen nicht überein."

#### 22.06.2016
#### Version 1.0.2
##### CHG
- Abhängigkeit zum Equitania-Modul entfernt (Funktion load_translation wird nun nicht mehr aufgerufen).

#### 21.04.2016
#### Version 1.0.1
##### ADD
- Je nach ausgewählten "Default Mail Server" wird der entsprechende Benutzername direkt in die "Default Mails Server Address" eingesetzt. 
- Das Feld + Label "Alias Domain" wird nun ausgeblendet und falls ein Wert drin Stand wird dieser entfernt.

