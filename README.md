# flaskApi
![Code Style](https://img.shields.io/badge/code_style-Black-brightgreen.svg)
![Linted](https://img.shields.io/badge/linted-Flake8-orange.svg)
![Known Vulnerabilities](https://badgen.net/snyk/isearch/flaskapi)
![Security Scanner](https://img.shields.io/badge/security_scanner-Bandit-blue.svg)

FlaskApi public code (initial)

Web Search Proxy for Google, Bing, DDG and others.

## How To run
```
python searchApi/app.py
```

## How to test
```
pytest -v searchApi
```

## How to update with pip
```
pip install -r requirements.txt --use-deprecated=legacy-resolver
```

## Flake8 - Linter
```
flake8 searchApi --max-line-length=120
```

## Black - code formatter
```
black searchApi
```

## Bandit - source code security analyzer
```
bandit -r searchApi -lll -v --ignore-nosec
```

## Links

https://blog.hartleybrody.com/web-scraping-cheat-sheet/

https://stackoverflow.com/questions/20035101/why-does-my-javascript-get-a-no-access-control-allow-origin-header-is-present

https://pypi.org/project/bandit/


