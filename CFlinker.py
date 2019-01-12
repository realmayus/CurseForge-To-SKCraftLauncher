import json
import sys
import os.path
import urllib.request

print('\033[95m################################################')
print('Open this python file in your directory for the SKLauncher Mods!')
print('################################################')


if len(sys.argv) == 1:
    print('\033[91m[FATAL] You did not specify a manifest.json! Exiting...')
    exit()
else:
    json_file = sys.argv[1]
    if not os.path.isfile(json_file):
        print('\033[91m[FATAL] The file you stated does not exist! Exiting...')
        exit()

json_data = open(json_file)

data = json.load(json_data)

json_data.close()

i = 0

for element in data['files']:
    i = i + 1
    projectID = str(element['projectID'])
    fileID = str(element['fileID'])

    print('Creating URL file...')
    url = 'https://minecraft.curseforge.com/projects/' + projectID + '/files/' + fileID + '/download'
    f = open("Mod-" + projectID + "-File-" + fileID + ".jar.url.txt", 'w')
    f.write(url)
    f.close()

    print('Downloading mod...')
    print(url)


    # Setting a user-agent because CurseForge doesn't allow us to download mods directly
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    # Actually downloading the file
    urllib.request.urlretrieve(url, "Mod-" + projectID + "-File-" + fileID + ".jar")


print('\033[92m[DONE!] Created ' + str(i * 2) + ' mod files with URLs for modpack \'' + data['name'] + '\' v.' + data['version'] + '!')

