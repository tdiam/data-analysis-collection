## Description

This tool parses the PDF grades file [[link]](https://shmmy.ntua.gr/forum/viewtopic.php?f=290&t=22175&start=80#p867105) for the June 2018 exam of the NTUA ECE Network Analysis course. The output is a frequency table showing the number of students that received each grade and the corresponding percentage.

## Dependencies

The pdf2txt utility is used, which is part of the [python-pdfminer](https://launchpad.net/ubuntu/+source/pdfminer) deb package.

To install:

```bash
sudo apt install python-pdfminer
```

## Usage
To print the grades frequency table run the following commands:

```bash
pdf2txt -o grades.txt grades.pdf
python parse.py
```

## Output
```
 0:  16    5.18%
 1:  21    6.80%
 2:  29    9.39%
 3:  38   12.30%
 4:  34   11.00%
 5:  60   19.42%
 6:  39   12.62%
 7:  33   10.68%
 8:  20    6.47%
 9:  12    3.88%
10:   7    2.27%
```