# SmartXMLAnalyzer

### Prerequisites

* python3
* BeautifulSoup
* FuzzyWuzzy

### Installing Needed Dependencies

```
pip install beautifulsoup4
pip install fuzzywuzzy
pip install python-Levenshtein
```
### Starting the application:
```
python3 main.py <input_origin_file_path> <input_other_sample_file_path> <original_element_id>

```
### Test cases with provided output results 

python3 main.py examples/sample-0-origin.html examples/sample-1-evil-gemini.html make-everything-ok-button
```
Original tag attribute values : {'class': 'btn btn-success', 'title': 'Make-Button', 'href': '#ok', 'text': 'Make everything OK'}
Path to the most similar tag in diff_case : [document] > html > body > div > div > div > div > div > div > a 
Tag attribute values : {'class': 'btn btn-success', 'title': 'Make-Button', 'href': '#check-and-ok', 'text': 'Make everything OK'}
Similarity per tag attribute : {'class': 100, 'title': 100, 'href': 29, 'text': 100}
Final similarity score : (82.25,)
```

python3 main.py examples/sample-0-origin.html examples/sample-2-container-and-clone.html make-everything-ok-button
```
Original tag attribute values : {'class': 'btn btn-success', 'title': 'Make-Button', 'href': '#ok', 'text': 'Make everything OK'}
Path to the most similar tag in diff_case : [document] > html > body > div > div > div > div > div > div > div > a 
Tag attribute values : {'class': 'btn test-link-ok', 'title': 'Make-Button', 'href': '#ok', 'text': 'Make everything OK'}
Similarity per tag attribute : {'class': 52, 'title': 100, 'href': 100, 'text': 100}
Final similarity score : (88.0,)
```

python3 main.py examples/sample-0-origin.html examples/sample-3-the-escape.html make-everything-ok-button
```
Original tag attribute values : {'class': 'btn btn-success', 'title': 'Make-Button', 'href': '#ok', 'text': 'Make everything OK'}
Path to the most similar tag in diff_case : [document] > html > body > div > div > div > div > div > div > a 
Tag attribute values : {'class': 'btn btn-success', 'title': 'Do-Link', 'href': '#ok', 'text': 'Do anything perfect'}
Similarity per tag attribute : {'class': 100, 'title': 33, 'href': 100, 'text': 43}
Final similarity score : (69.0,)
```

python3 main.py examples/sample-0-origin.html examples/sample-4-the-mash.html make-everything-ok-button
```
Original tag attribute values : {'class': 'btn btn-success', 'title': 'Make-Button', 'href': '#ok', 'text': 'Make everything OK'}
Path to the most similar tag in diff_case : [document] > html > body > div > div > div > div > div > div > a 
Tag attribute values : {'class': 'btn btn-success', 'title': 'Make-Button', 'href': '#ok', 'text': 'Do all GREAT'}
Similarity per tag attribute : {'class': 100, 'title': 100, 'href': 100, 'text': 20}
Final similarity score : (80.0,)
```

