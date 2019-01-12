# CurseForge-To-SKCraftLauncher
Creates .txt files with the download links for a [Minecraft CurseForge](https://minecraft.curseforge.com/) modpack, that can be used when creating custom Modpacks in the [SKCraft Launcher](https://github.com/SKCraft/Launcher)


## How to use
0. Download your curseforge Modpack manually (as a .zip file)
1. Make sure that you have Python 3.* installed.
2. Open the Mods folder of your custom Modpack.
3. Move this python file there into that folder.
4. Extract the `manifest.json` file from your downloaded modpack.
5. Open a command line and type: `python CFLinker.py [PATH TO manifest.json]'.
6. If everything went correctly you now have all your .txt files with the download link in the file! Their name is the projectID of any mod used in your pack.



## License

MIT
