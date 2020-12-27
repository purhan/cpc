![](docs/banner.png)
----------------------------------------

CPC is a command-line utility aimed towards competitive programmers.

# Features

At any point in time, you can run `cpc` or `cpc -h` to get a list of what the utility has to offer, or `cpc <command> -h` for details related to a particular command.

## Stress Testing

CPC provides functionality to test an optimized program against bruteforce to compare their outputs with 

```bash
cpc st -b <bruteforce-executable> -o <optimized-executable> -tg <testcase-generator>
```

It is advised to supply the arguments via the [`.cpcrc`](#Configuration) file. This would shorten the command to:

```bash
cpc st
```

## Scraping Submissions

Users can scrape their submissions from various online judges. Even though support is limited, contribution is welcome to add support to other judges.  
Judges currently supported:
- [Codeforces](codeforces.com/) (Gym is also supported)
- [SPOJ](spoj.com/)

Interactive scraper can be launched using:

```bash
cpc scrape
```

# Configuration

CPC can be configured using a `.cpcrc` file. This would sit in the same repository as to where you will be operating from. If it exists in another directory, a path can be specified using:

```bash
cpc <sub-command> -cf <path/to/.cpcrc>
```

This is very useful for the [stress testing](#stress-testing) command. Below is an example configuration:

```yaml
precommand: 
    # To compile code into executables
    g++ -std=c++17 testcase_generator.cpp -o generator
    g++ -std=c++17 main.cpp -o optimized
    g++ -std=c++17 bruteforce.cpp -o bruteforce
count: 1000                     # Default -> 100
bruteforce: bruteforce          # Default -> bruteforce
optimized: optimized            # Default -> optimized
testcase_generator: generator   # Default -> generator
```

# Installation

## Installation via PIP

The installation process is very straight-forward. CPC is available as a PYPI package and can be installed via:

```bash
pip install cpc
```

## Manual installation

To install manually, clone from github. It is advised to use [python venv](https://docs.python.org/3/library/venv.html):

```bash
git clone https://github.com/Purhan/cpc.git
cd cpc
pip install --editable .
```
