#!/bin/bash

##############################################################################################################
# На днях в комментариях человек предложил небольшой скрипт, который автоматизирует процесс.
# Я его немного доработал, чтобы можно было вручную указать необходимый размер перед созданием. Делаюсь с вами.
##############################################################################################################

read -p 'Enter swap size in megabytes: ' size_mb
size_kb=$((1024*${size_mb}))
dd if=/dev/zero of=/swap bs=1024 count=${size_kb}
chmod 0600 /swap
mkswap /swap
swapon /swap
if [ "$(grep '/swap' /etc/fstab)" ]; then
  echo "Error: file /etc/fstab already has 'Swap' record"
else
  echo "Add Swap record to /etc/fstab"
  echo -e '\n/swap swap swap defaults 0 0' >> /etc/fstab
fi
swapon --show
