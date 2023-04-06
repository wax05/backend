import argparse
from app import Create_App

parser = argparse.ArgumentParser()
parser.add_argument("-T","--test",dest="TestServer",action="store_true")# -T --test TestServer On off option Default value is false
parser.add_argument("-G","--global",dest="Global",action="store_true")# -G --global server ip(0.0.0.0)option Default value is false
parser.add_argument("-P","--port",dest="Port",action="store")# -P --port Server Port number
Cli_args = parser.parse_args()

if Cli_args.Port == None:
    Cli_args.Port = 5000 #Flask default Port Value (IP:5000)
if Cli_args.Global:
    Cli_args.Global = "0.0.0.0"
else:
    Cli_args.Global = "127.0.0.1"

if __name__ == '__main__':
    Create_App().run(debug=Cli_args.TestServer, host=Cli_args.Global, port=Cli_args.Port)
