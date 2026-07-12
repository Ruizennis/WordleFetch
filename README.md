# WordleFetch
## A simple way to get information on todays wordle

## Setup

### Clone the repository
```bash
apt install git
git clone https://github.com/WordleFetch
cd WordleFetch
```
### Install rich
```bash
pip install rich
```
### Run the python file
```python
python Run.py
```

### Optional, Enable alias 
Open your bashrc file
```bash
nano ~/.bashrc
```
Add this to your .bashrc file so you can type wordle from anywhere and easily run the script.
```bash
alias wordle="cd pathtopythonfile&&python run.py
```