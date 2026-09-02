En simpel miniräknare skriven i Python som kan addera, subtrahera, multiplicera, dividera och ta kvadratroten ur ett tal.

Vad gör applikationen

Applikationen tar emot en operation och två tal via terminalen och returnerar sedan resultatet.
 
 Dessa operationer kan du använda:

add – addition
subtract – subtraktion
multiply – multiplikation
divide – division (ger felmeddelande vid division med noll)
sqrt – kvadratrot (ger felmeddelande vid negativa tal)

Hur man kör applikationen lokalt

1. Klona repot:
bash
git clone https://github.com/Demshk/DevOps1.git
cd DevOps1

2. Kör applikationen med önskad operation och två tal:

   python3 calculator.py add 5 3
   python3 calculator.py subtract 10 4
   python3 calculator.py multiply 3 6
   python3 calculator.py divide 20 5
   python3 calculator.py sqrt 16 0

   (när sqrt används ignoreras det andra talet, men du måste ändå ange 0)

3. För att köra de automatiserade testerna lokalt, installera pytest och kör:

   pip install pytest
   pytest -v

Hur CI-pipelinen fungerar

Projektet har en CI pipeline konfigurerad med GitHub Actions (.github/workflows/ci.yml). Pipelinen triggas automatiskt varje gång kod pushas till main, eller när en pull request görs mot main.

Pipelinen kör följande steg i ordning:

1. Checkout av koden – hämtar den senaste koden från repot
2. Sätt upp Python – installerar Python 3.11 på en vm
3. Installera beroenden – installerar pytest
4. Kör tester – kör samtliga automatiserade tester med pytest -v

Om något test failar misslyckas hela pipelinen, detta kan du se direkt under fliken Actions på GitHub. Det gör det möjligt att upptäcka fel tidigt innan koden når produktion.