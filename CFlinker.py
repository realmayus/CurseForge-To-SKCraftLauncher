import json
import sys
import os.path

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

#json_file = 'C:\\Users\\Marius\\Desktop\\manifest.jso'

json_data = open(json_file)

data = json.load(json_data)

json_data.close()

i = 0

for element in data['files']:
    i = i + 1
    projectID = str(element['projectID'])
    fileID = str(element['fileID'])

    url = 'https://minecraft.curseforge.com/projects/' + projectID + '/files/' + fileID + '/download'
    f = open(projectID + '.txt', 'w')
    f.write(url)
    f.close()

print('\033[92m[DONE!] Created ' + str(i) + ' mod download files for modpack \'' + data['name'] + '\' v.' + data['version'] + ' successfully!')
