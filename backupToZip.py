# This script will backup a folder to a zip file
# Usage: backupToZip(srcfolder, destfolder)
# Create date: 2021/6/18

import zipfile
import os


def backupToZip(srcfolder, destfolder):
    folder = os.path.abspath(srcfolder)
    number = 1

    while True:
        # Create the zip folder name and zip folder path
        zipname = os.path.basename(folder) + '_' + str(number) + '.zip'
        zipname = os.path.join(destfolder, zipname)
        if not os.path.exists(zipname):
            break
        number = number + 1

    # Create a zip folder
    print('Creating %s ...' % zipname)
    backup_zip = zipfile.ZipFile(zipname, 'w', allowZip64=True)

    for foldername, subfolder, filenames in os.walk(folder):
        print('Adding files in %s ...' % foldername)
        backup_zip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print("Done")


backupToZip(r'D:\sikuli\Scan', r'D:\sikuli\backup')
