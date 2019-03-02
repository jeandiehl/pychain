from uuid import uuid4
import click
import cmd
import threading
import os
import time
import requests
from flask import Flask
from flask import jsonify
from flask import request


node_identifier = str(uuid4()).replace('-', '')
peers = []#[{ 'ip': '127.0.0.1', 'port': '5001' }]


class NodeCmd(cmd.Cmd):
    intro = 'Node is running!   Type help or ? to list commands.\n'
    prompt = '> '

    app = Flask(__name__)

    def __init__(self, ip, port):
        super(NodeCmd, self).__init__()
        self.ip = ip
        self.port = port
        self.thread = threading.Thread(target=self.app.run, kwargs=dict(host=self.ip, port=self.port))
        self.thread.daemon = True
        self.thread.start()

        #self.peers = []
        self.master_node = { 'ip': '127.0.0.1', 'port': '5001' }
        global peers
        peers.append(self.master_node)

        time.sleep(2)

    @app.route('/get_peers', methods=['GET'])
    def get_peers():
        global peers
        return jsonify(peers)

    @app.route('/add_peer', methods=['POST'])
    def add_peer():
        global peers
        values = request.get_json()
        print(values)
        required = ['ip', 'port']
        if not all(k in values for k in required):
            return 'Missing values', 400
        peers.append({'ip': values['ip'], 'port': values['port']})
        return jsonify(response='success')

    def broadcast(self):
        global peers
        for peer in peers:
            r = requests.post('http://{}:{}/add_peer'.format(peer['ip'], peer['port']), json={'ip': self.ip, 'port': self.port})

    def precmd(self, line):
        line = line.lower()

        return line

    def do_peers(self, arg):
        print(peers)

    def do_bc(self, arg):
        self.broadcast()

    def do_exit(self, arg):
        self.close()
        return True

    def close(self):
        pass

    @app.route('/mine', methods=['GET'])
    def mine():
        return "Hello World!"


@click.command()
@click.option('--ip', default='0.0.0.0', help='IP address of the server.')
@click.option('--port', default=5000, help='Port of the server.')
def start(ip, port):
    NodeCmd(ip, port).cmdloop()


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    cls()
    start()
