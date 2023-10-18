import os
import sys
import random
import string
import subprocess
import argparse
import shutil
from pathlib import Path

# Функция для генерации случайного токена
def generate_token():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(10))

# Функция для создания и активации виртуального окружения
def create_env(env_dir):
    subprocess.run(['python3', '-m', 'venv', env_dir], check=True)
    activate_script = os.path.join(env_dir, 'bin', 'activate')
    source_activate_cmd = f'source {activate_script}'
    subprocess.run(['/bin/bash', '-c', source_activate_cmd], check=True)

# Функция для запуска окружения
def start_environment(env_dir, port):
    token = generate_token()
    notebook_dir = os.path.join(env_dir, 'notebooks')

    os.makedirs(notebook_dir, exist_ok=True)
    os.chdir(notebook_dir)

    # Запуск Jupyter Notebook с указанными параметрами
    cmd = f'jupyter notebook --ip localhost --port {port} --no-browser --NotebookApp.token={token} --NotebookApp.notebook_dir={notebook_dir}'
    subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=False)

    print(f'Запущено окружение: Порт - {port}, Токен - {token}')

# Функция для остановки окружения
def stop_environment(env_dir):
    if os.path.exists(env_dir):
        shutil.rmtree(env_dir)
        print(f'Окружение {env_dir} остановлено.')
    else:
        print(f'Окружение {env_dir} не существует.')

# Функция для остановки всех окружений
def stop_all_environments():
    notebooks_dir = Path.cwd()
    env_dirs = [p for p in notebooks_dir.iterdir() if p.is_dir() and p.stem.startswith('dir')]
    for env_dir in env_dirs:
        stop_environment(env_dir)

# Функция для парсинга аргументов командной строки
def parse_args():
    parser = argparse.ArgumentParser(description='Управление окружениями Jupyter Notebook')
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    # Команда start
    start_parser = subparsers.add_parser('start', help='Запуск N новых окружений')
    start_parser.add_argument('count', type=int, help='Количество окружений для запуска')

    # Команда stop
    stop_parser = subparsers.add_parser('stop', help='Остановка i-го окружения')
    stop_parser.add_argument('index', type=int, help='ID окружения для остановки')

    # Команда stop_all
    subparsers.add_parser('stop_all', help='Остановка всех окружений')

    return parser.parse_args()

# Основная функция
def main():
    args = parse_args()

    if args.command == 'start':
        count = args.count
        for i in range(count):
            env_dir = f'dir{i}'
            env_path = Path.cwd() / env_dir
            create_env(env_path)
            start_environment(env_dir=env_dir, port=8888 + i)

    elif args.command == 'stop':
        index = args.index
        env_dir = f'dir{index}'
        stop_environment(env_dir)

    elif args.command == 'stop_all':
        stop_all_environments()

if __name__ == '__main__':
    main()