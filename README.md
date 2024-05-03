## Simple USFM

This is a simple python script help you to convert complex usfm to simple usfm. The re generated USFM will only contains the book info and verse text.

- [USFM Grammar](https://pypi.org/project/usfm-grammar/) is used to parse and re generate USFM.


## Setup Locally

```
git clone -b version-2 https://github.com/sijumoncy/generate-plain-usfm.git
```

```
cd generate-plain-usfm
```

### Set up virtual Environment

```
python3 -m venv env
```

```
source env/bin/activate
```

```
pip install -r requirements.txt
``` 


## How to Use

- Add USFM file need to convert into `source` directory.
- You can add one or multiple files in the source directory
- remove the `sample.usfm` file from the  `source` directory. Which is added for testing.
- There multi ways to process the files
- Once the file is processed , it will be available in the `out` directory

- open terminal in the root directory
- use python3 for `linux` and python for `windows`

**Process single file**

```
python3 main.py <filename.usfm>
```

**Process multiple files**

```
python3 main.py <filename1.usfm> <filename2.usfm> <filename3.usfm>
```

**Process All files in the source**

```
python3 main.py all
```

## Errors and Status

- Errors and status will be shown in the terminal