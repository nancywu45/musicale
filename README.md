# Musicale
This is a Web application called **Musicale** that uses Python's Flask framework.

## Description

This repository is a music library that allows you to browse through different tracks, register & sign-in, search by track, album and artist, add them to a playlist and review each track. Additionally, a new feature being able to listen to the audio of the tracks on the application.

## Installation

**Installation via requirements.txt**

```shell
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select your project from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment.

**After the installation**

Create a `.env` file in your local repository and add the following:

```
# Flask variables
# ---------------
FLASK_APP = 'wsgi.py'
FLASK_ENV = 'development'                                 # 'development' or 'production'
SECRET_KEY = '+Fus{=8MSV99y2ahF:@gcjtB_&J7f?}g'           # Used to encrypt session data.
TESTING = False                                           # True or False.

# WTForm variables
# ----------------
WTF_CSRF_SECRET_KEY = '$=H}j62u&SyJCy,JGELHx&3$jr6`>T3Y'  # Needed by Flask WTForms to combat cross-site request forgery.
```

## Execution

**Running the application**

From the project directory, and within the activated virtual environment (see _venv\Scripts\activate_ above):

```shell
$ flask run
```

## Data sources

The data files are modified excerpts downloaded from:
https://www.loc.gov/item/2018655052 or
https://github.com/mdeff/fma

We would like to acknowledge the authors of these papers for introducing the Free Music Archive (FMA), an open and easily accessible dataset of music collections:

Defferrard, M., Benzi, K., Vandergheynst, P., & Bresson, X. (2017). FMA: A Dataset for Music Analysis. In 18th International Society for Music Information Retrieval Conference (ISMIR).

Defferrard, M., Mohanty, S., Carroll, S., & Salathe, M. (2018). Learning to Recognize Musical Genre from Audio. In The 2018 Web Conference Companion. ACM Press.

## Pipeline

Github action will run on every pull request this includes

```shell
# formatting
$ black .
# type checking
$ mypy .
# testing
$ python -m pytest
```
