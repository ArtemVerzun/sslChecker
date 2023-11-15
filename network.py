import ssl
import socket
from db import add_ssl


# Функция для определения поддерживаемых версий SSL
def get_ssl_info(host, port):
    list_ssl = ['SSLv2', 'SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3']
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssl_version = ssock.version()
            cert = ssock.getpeercert()
            list_cert_domains = [x[1] for x in cert['subjectAltName'] if x[0] == 'DNS']
            if ssl_version in list_ssl:
                for domains in list_cert_domains:
                    add_ssl(host, port, ssl_version, domains)
            else:
                print(f'На хосте: {host} нет ssl сертификата из данного списка: {list_ssl}')