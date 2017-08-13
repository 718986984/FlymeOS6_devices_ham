import common
import edify_generator

def ModifyBegin(info):
  edify = info.script
  edify.script[0] = \
  '''ifelse(is_mounted("/system"), unmount("/system"));
ui_print("******************************************");
ui_print("* Flyme6 for ZUK Z1");
ui_print("*");
ui_print("* Romer: Chopin_w");
ui_print("******************************************");
\n''' + edify.script[0]

def WritePolicyConfig(info):
  try:
    file_contexts = info.input_zip.read("META/file_contexts")
    common.ZipWriteStr(info.output_zip, "file_contexts", file_contexts)
  except KeyError:
    print "warning: file_context missing from target;"

def InstallRadio(img_name, img_file, partition, info):
    common.ZipWriteStr(info.output_zip, img_name, img_file)
    info.script.AppendExtra(('package_extract_file("' + img_name + '", "' + partition + '");'))
def Installall(info):
    img_file1 = info.input_zip.read("BOOTABLE_IMAGES/emmc_appsboot.mbn")
    InstallRadio("emmc_appsboot.mbn", img_file1, "/dev/block/bootdevice/by-name/aboot", info)
    img_file2 = info.input_zip.read("BOOTABLE_IMAGES/NON-HLOS.bin")
    InstallRadio("NON-HLOS.bin", img_file2, "/dev/block/bootdevice/by-name/modem", info)
    img_file3 = info.input_zip.read("BOOTABLE_IMAGES/sbl1.mbn")
    InstallRadio("sbl1.mbn", img_file3, "/dev/block/bootdevice/by-name/sbl1", info)
    img_file4 = info.input_zip.read("BOOTABLE_IMAGES/sdi.mbn")
    InstallRadio("sdi.mbn", img_file4, "/dev/block/bootdevice/by-name/dbi", info)
    img_file5 = info.input_zip.read("BOOTABLE_IMAGES/rpm.mbn")
    InstallRadio("rpm.mbn", img_file5, "/dev/block/bootdevice/by-name/rpm", info)
    img_file6 = info.input_zip.read("BOOTABLE_IMAGES/splash.img")
    InstallRadio("splash.img", img_file6, "/dev/block/bootdevice/by-name/splash", info)
    img_file7 = info.input_zip.read("BOOTABLE_IMAGES/tz.mbn")
    InstallRadio("tz.mbn", img_file7, "/dev/block/bootdevice/by-name/tz", info)
    img_file8 = info.input_zip.read("BOOTABLE_IMAGES/persist_1.img")
    InstallRadio("persist_1.img", img_file8, "/dev/block/bootdevice/by-name/persist", info)

def FullOTA_InstallEnd(info):
    WritePolicyConfig(info)
    ModifyBegin(info)
    info.script.AppendExtra(('ui_print("Writing radio image...");'))
    Installall(info)
