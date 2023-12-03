# install


before proceeding with installation you must install [pyenv](https://github.com/pyenv/pyenv) in order to use the correct version of python interpreter, and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) to create virtual environments.

clone this repository in a location of your choice and navigate to the cloned directory.

```bash
git clone https://github.com/DenysSvintsylo/PP.git
```

open a terminal in the parent directory and run these commands.

```bash
virtualenv venv
```

```bash
.\venv\Scripts\activate 
```

```bash
python -m pip install -r requirements.txt
```

# run

Run this command in terminal in the parent directory in order to start the waitress server in debug mode. 


```bash
python serve.py  
```

