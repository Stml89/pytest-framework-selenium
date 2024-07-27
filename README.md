# About
This is a simple example of a test automation repository structure.
Made by Siarhei Stamal for Python Test Automation course

# Project structure
```
/<project-name>
| .gitignore
| pytest.ini
| README.md
| test_data/
|_____ <file_name.json>
|_____ ...
| tests/
|_____ unit/
|________ test_calculator.py
|________ ...
|_____ api/
|_____ ui/
| source/
|_____ calculator.py
|_____ ...
| test-reports/
|_____ Test_report_xxxx-xx-xx xx:xx:xx.html
```


# How to run test cases:
Args:
`-m <marker> - to execute test cases to given marker`
`--log-level <log-level> - to override default log level`

To run ALL tests:
`pytest . --log-level=INFO`

To execute only SMOKE test cases:
`pytest . --log-level=INFO -m smoke`