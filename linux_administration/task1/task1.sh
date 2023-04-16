#!/bin/bash

# 1. Проверка на наличие репозитория Backports в списке репозиториев.
# Если отсутствует — добавляем (под используемый вами дистрибутив).
cnt=$(grep -rhE ^deb /etc/apt/sources.list* | grep -Fic 'backports')
if [[ $((cnt)) -gt 0 ]]
then echo “Backports уже установлен”
else
  sudo add-apt-repository -r "deb http://archive.ubuntu.com/ubuntu $(lsb_release -cs)-backports main restricted universe multiverse "
fi
# 2. Обновление пакетного менеджера.
sudo apt update
sudo apt upgrade
# 3. Установка и запуск Apache2.
sudo apt install apache2
sudo systemctl enable apache2
# Установим некоторые нужные модули apache2 и перезагрузка сервера (допдействие).
sudo a2enmod ssl
sudo a2enmod rewrite
sudo a2enmod headers
sudo a2enmod expires
sudo systemctl restart apache2
# 4. Установка Python.
sudo apt install python3.11
python3.11 -V
# Установка python пакетов (допдействие).
sudo apt -y install python3-pip
pip install requests fastapi==0.63.0 uvicorn==0.13.4 pandas bs4
# 5. Установка и поднятие SSH-сервера.
sudo apt-get install ssh
sudo systemctl start sshd
# Поменяем порт для ssh на 2222 например (допдействие).
sudo sed -ie 's/^[#]*Port [0-9]*/Port 2222/g' /etc/ssh/sshd_config
sudo systemctl restart sshd
# Создаем архив tar.gz текущего каталога (допдействие).
sudo tar -czf "../${PWD##*/}.tar.gz" .
# Установка curl (допдействие).
sudo apt install curl
curl -V
# Напоследок сводка погоды в Санкт-Петербурге (допдействие).
curl -2 wttr.in/Saint-Petersburg
