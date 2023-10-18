#!/bin/bash

if [ "$#" -lt 1 ]; then
  echo "Недостаточно аргументов."
  exit 1
fi

command="$1"
shift

case "$command" in
  start)
    if [ "$#" -lt 1 ]; then
      echo "ID окружения должно быть указано."
      exit 1
    fi

    for env_id in "$@"; do
      echo "Запуск окружения $env_id"
      python3 main.py start "$env_id"
    done
    ;;
  stop)
    if [ "$#" -lt 1 ]; then
      echo "ID окружения должно быть указано."
      exit 1
    fi

    for env_id in "$@"; do
      echo "Остановка окружения $env_id"
      python3 main.py stop "$env_id"
    done
    ;;
  stop_all)
    echo "Остановка всех окружений"
    python3 main.py stop_all
    ;;
  *)
    echo "Неверная команда."
    exit 1
    ;;
esac