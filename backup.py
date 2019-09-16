import shutil
import os
import time
import stat

class index:
    #Initilation
    def __init__(self):
        self.x = 0
        self.endfiles = [".txt", ".pdf", ".png", ".jpg", ".psd", ".mp4", ".mp3", ".docx", ".doc", ".zip", ".rar",
        ".iso", ".html", ".css", ".scss", ".js"]
        self.folders = ["\\Pictures\\", "\\Music\\", "\\Documents\\", "\\Desktop\\"]
        self.source = "C:\\Users\\George" #Source of the upper folders like C:\\Users\"Your User"
        self.destination = "G:\\Backup\\" #Destination of the folder !Backup should stay | example C:\\Users\\Patryk\\Desktop\\!Backup!
        self.partition = self.destination[:3]
        self.options()
        if self.opt2 == True:
            self.custom_backup()
        elif self.opt1 == True:
            self.default_backup()

    #Option of doing a custom Backup or the Default
    def options(self):
        x = 0
        self.opt2 = False
        self.opt1 = False
        x = input("Type 1: Default Backup or 2: Custom Backup: ")
        try:
          x = int(x)
          if x == 1:
              self.opt1 = True
          elif x == 2:
              self.opt2 = True
        except:
            os.system('cls')
            print('There was an error. Retry')
            self.options()

    #Path creation if it doesnt exist
    def assure_path_exists(self, path):
        if not os.path.exists(path):
           os.makedirs(path)

    #Removal of a folder and everything within it
    def folder_removal(self, mypath):
        try:
            os.chmod(mypath, stat.S_IRWXO)
            shutil.rmtree(mypath)

        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror) + " Try deleting the folder by yourself")

    #Process of the custom backup
    def custom_backup(self):
      print("runs")

    #Process of the default backup
    def default_backup(self):
        for x in self.folders:
            self.dir = self.source + self.folders[self.x]
            self.files = os.listdir(self.dir)
            for y in self.files:
                if y.endswith(tuple(self.endfiles)):
                   endfile = y[-3:] + "\\"
                   tmp = self.source + self.folders[self.x] + y
                   dest = self.destination + endfile
                   self.assure_path_exists(dest)
                   shutil.copy2(tmp, dest)
                elif y.endswith(""):
                    save_folder = False
                    if y[-4:] != ".ini":
                        try:
                          tmp0 = self.source + self.folders[self.x] + y
                          tmp1 = os.listdir(tmp0)
                          self.assure_path_exists(self.destination + "Folders")
                          for f in tmp1:
                            if f.endswith(tuple(self.endfiles)):
                                save_folder = True
                          if save_folder:
                             shutil.copytree(tmp0, self.destination + "Folders\\" + y)
                             print(tmp0)
                        except:
                            print(y + " |____| " + 'Was not saved, because its already there or is not meant to be saved')

            self.x += 1
            print("--------------------------------")
        backup_name = str(self.destination[:-1] + "-" + time.strftime("%x"))
        backup_name = backup_name.replace("/", "-")
        if not os.path.exists(backup_name + ".zip" or backup_name + ".rar"):
         print("Compressing files -- Please Wait")
         shutil.make_archive(backup_name, "zip", self.partition, "Backup")
         print("Deleting the temporary files")
         self.folder_removal(self.destination)
         print("Done ----- You can find your backup at %s" % backup_name)
        else:
            print("This Zip already exist's -- Try Again")


index()