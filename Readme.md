# Platform (CSAdmin) UI Automation using Robot Framework


## Installation

* Checkout from GitHub repository by forking: git clone git@github.com:oneconcern/platform-qa.git

* Install Python 3.8 or greater

* From the command-line, enter: pip3 install -r requirements.txt

* Install Community Version of PyCharm and install the pluggin called, Intellibot, Robot Framework Support

* Download the proper chromedriver appropriate to your current Chrome browser from here: https://chromedriver.chromium.org/downloads

* Download the proper geckodriver appropriate to your current Firefox browser from here: https://github.com/mozilla/geckodriver/releases

* Before running the automation, assure that you decrypt the file associated with your environment, which can be found under the data directory using SOPS


## Local configuration for webdriver installed
Using your favorite Python editor, open the files libs/api/CommonAPI.py and libs/pages/CommonLibrary.py. Update the "executable_path" in each files for locations for the following:
* chromedriver
* geckodriver

## Usage

```robot
# Runs Robot UI tests by tag names:
robot -i <tag name> --variable BROWSER:<your browser> --variable URL:<csadmin url> --variable ENVFILE:<env JSON file> --pythonpath ./libs/pages tests/

# Runs all Robot tests in parallel using pabot:
pabot --variable BROWSER:<your browser> --variable URL:<csadmin url> --variable ENVFILE:<env JSON file> --pythonpath <library path> tests/

# Runs parallel browsers using pabot:
pabot --pabotlib --argumentfile1 chrome.txt --argumentfile2 ff.txt --variable URL:<csadmin url> --variable ENVFILE:<env JSON file> --pythonpath ./libs/pages tests/

# More ways of executing the scripts can be found here:
https://dev.to/juperala/how-to-run-robot-framework-test-from-command-line-5aa


# Command-line variable(s):
<tag name>: Should be "Smoke", "Login", or combination, i.e. "SmokeANDLogin".
<your browser>: Should be "chrome", "firefox". No support for Safari or MS Edge at this time.
<csadmin url>: Should be "https://csadmin.staging.onec.co/#/orgs" or "https://csadmin.oneconcern.com/#/orgs"
<env JSON file: Should be "stage.json" or "prod.json".
<library path>: Should be Python library directory to "./libs/pages".
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change contact: rsarmiento@oneconcern.com
