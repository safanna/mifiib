#!/bin/sh

# Напишите Bash-скрипт для резервного копирования директории /home,
# конфигурационных файлов основных утилит удалённого доступа (SSH, RDP, FTP), а также директории /var/log.
tar cpf /archive/"task2_`date '+%d-%B-%Y'`.tar" /home/ /var/log/ /etc/ssh/sshd_config /etc/vsftpd.conf /etc/xrdp/xrdp.ini
