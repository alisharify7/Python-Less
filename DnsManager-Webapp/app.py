import platform
import subprocess
import requests
import dns.resolver
import json
import pathlib
from flask import Flask, render_template, redirect, flash, request


app = Flask(__name__)
BASE_DIR = pathlib.Path(__file__).parent

app.config["SECRET_KEY"] = "secret"

def read_DNS_json():
    f = BASE_DIR.joinpath("dns.json")
    res = requests.get("https://public-dns.info/nameserver/us.json")
    return res.json()

DNS_SERVERS = [{"ip": x['ip'], "ct":x['country_id']} for x in read_DNS_json()]


def set_dns(ip_address):
    operating_system = platform.system()
    if operating_system == 'Windows':
        subprocess.call(['netsh', 'interface', 'ipv4', 'set', 'dns', 'name="Ethernet"', 'static', ip_address])
    elif operating_system == 'Linux':
        with open('/etc/resolv.conf', 'w') as file:
            file.write(f'nameserver {ip_address}')
    else:
        print('Unsupported operating system')

def get_dns():
    resolver = dns.resolver.Resolver()
    dns_servers = resolver.nameservers
    return dns_servers


@app.context_processor
def template_variable():
    variables = {
        "DNS_SERVERS": DNS_SERVERS,
        "CURRENT_DNS": get_dns()[0],
        "DNS_SERVERS_len":len(DNS_SERVERS)
    }
    return variables




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/setDNS/<string:ip>")
def setDNS(ip):
    re = set_dns(ip)
    flash(f"DNS Changed Successfully {re}", "success")
    print(re)
    return redirect(request.referrer)

if __name__ == "__main__":
    app.run(debug=True)
