from network import get_ssl_info


def main():
    # Чтение файла с записями
    with open('hosts.txt') as file:
        for line in file:
            host, port = line.strip().split(':')
            try:
                get_ssl_info(host, int(port))
            except:
                print(f'Не удалось подключиться к хосту: {host}')


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
