import os
import argparse
import requests
import json
import platform


def do_ping_sweep(ip, num_of_host):
    """
    Ping sweep function
    :param ip: ip-address
    :param num_of_host: number of hosts to sweep
    """
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
    if platform.system() == 'Windows':
        response = os.popen(f'ping {scanned_ip}')
    else:
        response = os.popen(f'ping -c 1 {scanned_ip}')
    res = response.readlines()
    print(res)
    print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[3]}", end='\n\n')


def sent_http_request(target, method, headers=None, payload=None):
    """
    Sending http request function
    :param target: target URL
    :param method: type of method - POSt or GET
    :param headers: headers of requests
    :param payload: payload
    """
    headers_dict = dict()
    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)
    response = None
    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f'[#] Response status code: {response.status_code}\n'
        f'[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n'
        f'[#] Response content:\n {response.text}'
    )


parser = argparse.ArgumentParser(description='Network scanner')
parser.add_argument('task', choices=['scan', 'sendhttp'], help='Network scan or send HTTP request')
parser.add_argument('-i', '--ip', type=str, default='192.168.0.1', help='IP address')
parser.add_argument('-n', '--num_of_hosts', type=int, default=1, help='Number of hosts')
parser.add_argument('-t', '--target', type=str, default='http://ya.ru', help='URL address')
parser.add_argument('-m', '--method', type=str, choices=['GET', 'POST'], default='GET', help='Type of method')
parser.add_argument('-hd', '--header', nargs="+", default=None, help='Headers (name1:value1 name2:value2 ...)')
args = parser.parse_args()
if args.task == 'scan':
    for nhost in range(args.num_of_hosts):
        do_ping_sweep(args.ip, nhost)
elif args.task == 'sendhttp':
    sent_http_request(args.target, args.method, args.header)
