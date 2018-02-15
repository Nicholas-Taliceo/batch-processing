"""
FILE NAME:      batch-unzip.py

ABOUT:          This script batch extracts all compressed (ZIP) files that are
                located in the current user's "Downloads" folder. This is
                designed to work on the Windows operating system.
								
								This script is written in Python 3.4.

REFERENCES:     The get_download_path() definition utilizes code from the
                following thread: https://stackoverflow.com/questions/35851281/
                python-finding-the-users-downloads-folder.

                The unzip_download_folder() definition utilizes code I created
                located in the batchDEM repository: Nicholas-Taliceo/batchDEM.


AUTHOR:         Nicholas P. Taliceo

CONTACT
INFORMATION:    Email: ntaliceo@gmail.com
                Web:   www.NicholasTaliceo.com

DATE LAST
MODIFIED:       February 15, 2018
"""

import os
import zipfile


def get_download_path():
    """
    This code returns the pathname of the standard Download folder for the
    current user. This is valid for Windows or Linux.
    """
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def unzip_download_folder(pathname):
    """
    This code uses the pathname of the Downloads folder, parsing through, and
    identifying all downloaded ZIP folders. It then subsequently extracts all
    zipped folders, saving in an uncompressed folder of the same name. It then
    deletes the ZIP folders from the directory.
    """
    for i in os.listdir(pathname):
        if i[-3:].lower() == 'zip':
            new_folder = pathname + '\\' + i[:-4]
            zip_ref = zipfile.ZipFile(pathname + '\\' + i, 'r')
            zip_ref.extractall(new_folder)
            zip_ref.close()
            os.remove(pathname + '\\' + i)


# Call the download path folder unzipping definitions.
folder = get_download_path()
unzip_download_folder(folder)

print("\n" + "All folders have been successfully extracted!")
