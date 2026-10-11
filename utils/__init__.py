[pytest]
addopts = --base-url http://localhost:3000 --tracing retain-on-failure --screenshot only-on-failure --video retain-on-failure --html=reports/report.html --self-contained-html --alluredir=allure-results
markers =
    smoke: fast checks that the app is alive
    regression: full functional suite
    api: API-level tests
testpaths = tests