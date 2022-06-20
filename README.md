# CSV files to Excel Workbook

## Running prerequisites

**1. Download repo into local Mac directory**

**2. Install Python and Pandas library**

2a. Click OpenInTerminal.app to open current directory in the Terminal

2a. Install brew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2b. Install python 3.10

```
brew install python@3.10
```

2c. Install pip


```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

2d. Install pandas library

```
pip install pandas
```

### Using python script to merge a workbook

**1. Place desired CSV files to merge in the input folder**

**2. Open the directory in the Terminal**

Using OpenInTerminal.app

**3. Run the python script**
```
python run.py
```