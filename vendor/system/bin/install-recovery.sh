#!/system/bin/sh
if [ -f /system/etc/recovery-transform.sh ]; then
  exec sh /system/etc/recovery-transform.sh 8796160 81d2883acdb34ca904540e277f5797825e5ed858 6113280 3e8a61fb55b8fe3aff1c3c911433326f1cd9f6bc
fi

if ! applypatch -c EMMC:/dev/block/bootdevice/by-name/recovery:8796160:81d2883acdb34ca904540e277f5797825e5ed858; then
  applypatch -b /system/etc/recovery-resource.dat EMMC:/dev/block/bootdevice/by-name/boot:6113280:3e8a61fb55b8fe3aff1c3c911433326f1cd9f6bc EMMC:/dev/block/bootdevice/by-name/recovery 81d2883acdb34ca904540e277f5797825e5ed858 8796160 3e8a61fb55b8fe3aff1c3c911433326f1cd9f6bc:/system/recovery-from-boot.p && log -t recovery "Installing new recovery image: succeeded" || log -t recovery "Installing new recovery image: failed"
else
  log -t recovery "Recovery image already installed"
fi
