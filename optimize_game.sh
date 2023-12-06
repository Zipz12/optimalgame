#!/bin/bash

echo "Memulai optimalisasi untuk permainan..."

# Membersihkan memori
echo 1 > /proc/sys/vm/drop_caches

# Menonaktifkan swap
swapoff -a && swapon -a

# Menutup aplikasi yang tidak diperlukan
am kill-all

echo "Optimalisasi selesai. Selamat bermain!"
echo "Script By Ryuu!"