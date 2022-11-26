import random, os, shutil, zipfile

file = input('APK (filename): ')
pack = input('Pack (filename): ')

with zipfile.ZipFile(file, "r") as to_import:
    rng = random.randint(1, 99)
    to_import.extractall(f'tmp{rng}')

    with zipfile.ZipFile(pack, "r") as packimport:
        rng2 = random.randint(100, 199)
        packimport.extractall(f'tmp{rng2}')

    packdir = os.listdir(f'tmp{rng2}')
    apkdir = os.listdir(f'tmp{rng}/assets')
    for x in packdir:
        for y in apkdir:
            if x == y:
                packdir2 = os.listdir(f'tmp{rng2}/{x}')
                apkdir2 = os.listdir(f'tmp{rng}/assets/{y}')
                for i in packdir2:
                    for j in apkdir2:
                        if i == j:
                            print(f'{i} == {j}')
                            os.remove(f'tmp{rng}/assets/{x}/{j}')
                            print(f'Removed tmp{rng}/assets/{y}/{j}' + "\n" + f'Copying tmp{rng2}/{x}/{i}...')
                            shutil.copy(f'tmp{rng2}/{x}/{i}', f'tmp{rng}/assets/{x}/')
                            print(f'Copied tmp{rng2}/{x}/{i}\nCompressing to modified.zip...')

shutil.make_archive('modified', 'zip', f'tmp{rng}')
os.rename('modified.zip', 'modified.apk')
print('NOTE: I have not yet added an APK Signing system to this yet.')
shutil.rmtree(f'tmp{rng}')
shutil.rmtree(f'tmp{rng2}')
