# Playwright Browsers

## Create virtual environment
```sh
$ py -m venv .venv
```

## Enable virtual environment
```sh
$ source .venv/Scripts/Activate
```

## Copy already installed packages into requirements file
```sh
$ py -m pip freeze > requirements.txt
```

## Manual installation
```sh
$ py -m pip install pytest pytest-playwright pytest-html pytest-tagging
```

## Install packages from requirements file
```sh
$ py -m pip install -r requirements.txt
```

## If browsers are not installed then install them
```sh
$ playwright install
``` 

## Run the tests
```sh
$ py -m pytest tests/test_login.py -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --slowmo 1500 --tags test_pom
```

```sh
$ py -m pytest tests/test_emin.py -v --browser webkit --headed -q --tracing=on --video=on --html=reports/report.html --slowmo 1500
```

```sh
$ py -m pytest tests/test_emin.py -v --browser firefox --headed -q --tracing=on --video=on --html=reports/report.html --slowmo 1500
```

```sh
$ py -m pytest tests/test_emin.py -v --browser-channel msedge --headed -q --tracing=on --video=on --html=reports/report.html --slowmo 1500
```

## Playwright Codegen
```sh
$ playwright codegen
```