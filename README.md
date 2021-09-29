# Mydictionary  ![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

Create a dictionary similar to the real-world dictionary. There is no limit to the definition you provide to any word.

The user will give the word as input. Suppose that the word is present in the dictionary along with its definition or meaning.
Then program will print the meaning or definition of that word.
and if it's not present then it will find all the closest matches to it.

**For example:**
```
Please enter the word whose meaning you searching for: wuit
finding the closest match to this is :  ['wit', 'with', 'wilt']
wit
The ability for rational thought.
```
### Module used
python module difflib `from difflib import get_close_matches`

`from dictonaryword import words` (importing words from different file nameing dictonaryword)


## PRE-REQUISITES
Your laptop with 3.6.x (onwards) installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

Do not delete this file or program may fail `dictonaryword.py` :warning:

## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/mydictionary.git
2. In source folder, run `python3 'Mydictionary.py'` to start program, optionally, run with `--help` argument to see other runtime options.
