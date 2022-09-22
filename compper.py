import os

arr = os.listdir()
valid_files = []
for item in arr:
    if " " in item:
        print(f"[ERROR] Cant handle filenames with whitespace!! - {item}")
    if ".mp4" in item and "_fastversion" not in item:
        valid_files.append(item)


def do_video(filename):
    newextension = filename.strip(".mp4") + "_fastversion.mp4"
    tempextension = filename.strip(".mp4") + "_ALTERED.mp4"
    ae_command = f'auto-editor --no-open {filename}'
    fm_command = f'ffmpeg -i {tempextension} -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" {newextension}'
    os.system(ae_command)
    os.system(fm_command)
    # os.remove(filename)
    os.remove(tempextension)


print(f"[Starting] {len(valid_files)} total files found!\n")
for ind, item in enumerate(valid_files):
    print(f"[{item}] Starting Video..")
    do_video(item)
    print(f"[Progress] Finished Video - {item}")
    print(
        f"\n \n \n \n[PROGRESS] {len(valid_files) - ind - 1} files remaining!\n \n \n \n")
