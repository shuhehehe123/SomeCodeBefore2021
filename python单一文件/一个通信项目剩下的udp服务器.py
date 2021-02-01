import argparse,socket
MAX_BYTES=65535
from datetime import datetime

def server(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',port)) 
    print('监听于 {} '.format(sock.getsockname()))
    while 1:
        data,address=sock.recvfrom(MAX_BYTES )
        text = data.decode('ascii')
        data=text.encode('ascii')
        print('位于{}的客户端消息：{!r} '.format(address,text))
        sock.sendto(data,address)
def client(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text='现在的时间是{}'.format(datetime.now())
    data=text.encode('ascii')
    sock.sendto(data,('127.0.0.1',port))
    print('{}'.format(sock.getsockname()))
    data,address = sock.recvfrom(MAX_BYTES)
    text=data.encode('ascii')
    print('服务端{}回复了：{!r}'.format(address,text))
if __name__ == "__main__":
    choices = {'client':client,'server':server}
    parser=argparse.ArgumentParser(description='local udp')
    parser.add_argument('role',choices=choices,help='选择server还是client')
    parser.add_argument('-p',type=int,default=1060,help='UDP服务端口(默认为1060)')
    args=parser.parse_args()
    function=choices[args.role]
    function(args.p)
