В данном репозитории вы являетесь Developer'ом, т.е. не можете делать push в мастер ветку. Вам нужно запушить код дз в соответствующую ветку, залив туда `main.sh` со скриптом для запуска задания. А после сделать Merge Request в мастера

В репозитории работают автотесты, запускаемые в докере при каждом push. `gitlab-ci` файл заливать не нужно, он существует, но невидим. Удачи в выполнении дз)

Если потребуются к установке какие либо дополнительные программы для тестов (внутри докера), то создайте файл `install.sh` и запишите в него команды установки по типу (не обязательно)
```bash
#!/bin/bash
apt-get update
apt-get -y updrade
apt-get install -y tmux
```
