import glob  # Imports the various libraries for use in the program.
import os
import re
import shutil
import textwrap
import time


def dependencies():  # Checks for the program's dependencies, if they are not all found it halts execution and informs the user to add the files.
    if not os.path.exists("dependencies/"):
        print("The dependencies folder could not be found, please download it from GitHub and relaunch the program.")
        print("Ensure that the folder name is correct.")
        input("Press any key to end program.")
        quit()

    if not os.path.exists("yosuga.csx") and not os.path.exists("Haruka.csx"):
        print("The yosuga.csx or Haruka.csx file could not be found, please download it and relaunch the program.")
        print("Ensure that the file name is correct.")
        input("Press any key to end program.")
        quit()


def csxDecrypter(choice):  # Decrypts the csx file for the specific games using Proger's CSX Importer/Exporter.
    mainDirectory = os.getcwd()
    os.chdir("dependencies")
    print("Please press the Enter key to after you see 'Success.' to continue program execution.")
    print("Beginning execution...")
    time.sleep(5)
    if choice == 1:
        os.system("csx " + mainDirectory + "\yosuga.csx export-no-names")
    elif choice == 2:
        os.system("csx " + mainDirectory + "\Haruka.csx export-no-names")
    os.chdir("..")


def utfCombiner():  # Combines the .utf files into 1 file for easier processing.
    with open("temp.txt", "wb") as outfile:
        for filename in glob.glob('*.utf'):
            if filename == "temp.txt":
                continue
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)


def textReplacer(choice):  # Removes random pieces of text that are added in the conversion process.
    textReplace = open("temp.txt", "r", encoding="UTF-8")  # Opens the new file into the file stream.
    data = textReplace.read()  # Declaring the data variable used to store the changes to the text.

    data = re.sub("<.*>", "", string=data)  # Replaces the numbers in <> before each line with nothing.
    data = data.replace('???', ' ')  # Replaces the '???' symbol with a space.
    data = data.replace('\=', '')  # Replaces the '\=' symbol with nothing.
    data = data.replace('???', '.')  # Replaces the ??? symbol with .
    data = data.replace('???', "'")  # Replaces the ??? symbol with '
    data = data.replace('???', '-')  # Replaces the '???' symbol with '-'.
    data = data.replace('??? ', '')  # Replaces the '??? ' symbol with nothing.
    data = data.replace('???', '-')  # Replaces the '???' symbol with '-'.
    data = data.replace('???', '-')  # Replaces the '???' symbol with '-'.
    data = data.replace('[', '(')  # Replaces the '[' symbol with '('.
    data = data.replace(']', ')')  # Replaces the ']' symbol with ')'.
    data = data.replace('*', '???')  # Replaces the '*' symbol with ???.
    data = data.replace('??', 'a')  # Replaces the '??' symbol with a.
    data = data.replace('??', 'e')  # Replaces the '??' symbol with e.
    data = data.replace('??', 'o')  # Replaces the '??' symbol with o.

    textReplace = open("temp.txt", "w", encoding="UTF-8")  # Reopens the file for writing the new data to the file.
    textReplace.write(data)  # Writes the variable into the file.
    textReplace.close()  # Closes the file stream.

    if choice == 1:
        with open("temp.txt", "r", encoding="UTF-8") as file:  # Adds the missed data from the csx file, this must be added because the csx file is encoded weirdly at these lines and skips the text for the choices.
            lines = file.readlines()
            file.close()
        lineNumber = 1
        with open("temp.txt", "w", encoding="UTF-8") as file:
            for line in lines:
                if lineNumber == 2320:
                    file.write("Even though, we still haven't heard from her what should we do.\n")
                elif lineNumber == 35154:
                    file.write("At this point, Sora was projecting her annoyance so clearly that, were at it directed at Motoka-san, it would've had her stumbling over her words. It didn't seem to bother her mother, though.\n")
                elif lineNumber == 38120:
                    pass
                elif lineNumber == 38121:
                    pass
                elif lineNumber == 38618:
                    pass
                elif lineNumber == 38619:
                    pass
                elif lineNumber == 39282:
                    pass
                else:
                    file.write(line)
                lineNumber += 1
        file.close()
    elif choice == 2:
        with open("temp.txt", "r", encoding="UTF-8") as file:  # Removes the additional line that was inserted into file 34.txt accidentally.
            lines = file.readlines()
            file.close()
        lineNumber = 1
        with open("temp.txt", "w", encoding="UTF-8") as file:
            for line in lines:
                if lineNumber == 5357:
                    pass
                else:
                    file.write(line)
                lineNumber += 1
        file.close()


def chapterCreator():
    file = open("temp.txt", "a", encoding="UTF-8")
    file.write("\n ~ AdvScreen ~ ")
    file.close()

    file = open("temp.txt", "r", encoding="UTF-8")
    data = file.readlines()
    temp = []
    fileNumber = 1
    for i in range(1, len(data)):
        if ' ~ ' in data[i]:
            fn = os.path.join(os.getcwd(), f"{fileNumber}.txt")
            with open(fn, "w", encoding="UTF-8") as file:
                file.writelines(temp)
            temp = []
            fileNumber += 1
        else:
            temp.append(data[i])


def deleteMiscFiles():  # Deletes the miscellaneous files generated by the conversion of the csx file into chapter files.
    for file in [file for file in os.listdir(os.getcwd()) if
                 file.endswith(".txt") or file.endswith(".utf") or file.endswith(".cji") or file.endswith(
                         "yosuga_original.csx") or file.endswith("Haruka_original.csx")]:
        os.remove(os.path.join(os.getcwd(), file))


def fileImporter(choice):  # Retrieves the file names for use in the fileConverter function.
    try:
        shutil.rmtree("compile")  # Removes the "compile" folder if it exists.
    except OSError:
        pass  # If the file does not exist, it will give an error, this ignores the error.
    os.mkdir("compile")   # Recreate a new compile folder for the data to be inserted into.
    os.chdir("compile")
    os.mkdir("scenario")
    os.chdir("..")

    if choice == 1:  # Used to import the files for Yosuga no Sora
        with open("306.txt", "r", encoding="UTF-8") as file:  # Removes the additional line that was inserted into file 306.txt accidentally.
            lines = file.readlines()
            file.close()
        lineNumber = 1
        with open("306.txt", "w", encoding="UTF-8") as file:
            for line in lines:
                if lineNumber == 145:
                    pass
                else:
                    file.write(line)
                lineNumber += 1
        shutil.copyfile(f"dependencies/yosuga/macro.ks", f"compile/scenario/macro.ks")  # Copies the macro.ks file that doesn't need to be changed.
        for count in range(1, 306 + 1):  # Used to iterate through the files.
            if count == 114:  # Used to skip the file that has Nao's extra chapter.
                pass
            elif count <= 306:
                formattedFileName = yosugaFileNames(count)  # Calls the function and stores the current value in a variable.
                unformattedFileName = str(count) + ".txt"  # Increases the value of the unformatted file that is called.

                newFile = open(f"dependencies/yosuga/{formattedFileName}", "r", encoding="Shift_JIS")  # Opens the file stream for the formatted (new) file.
                formatted = newFile.readlines()  # Reads the lines from the file and inserts it into a variable.
                newFile.close()  # Closes the file stream for the formatted (new) file.

                oldFile = open(f"{unformattedFileName}", "r", encoding="UTF-8")  # Opens the file stream for the unformatted (old) file.
                unformatted = oldFile.readlines()  # Reads the lines from the file and inserts it into a variable.
                oldFile.close()  # Closes the file stream for the unformatted (old) file.

                fileConverter(formatted, unformatted, formattedFileName)  # Calls the fileConverter function to move the data between files.
    elif choice == 2:
        with open("114.txt", "r", encoding="UTF-8") as file:  # Removes the additional line that was inserted into file 114.txt accidentally.
            lines = file.readlines()
            file.close()
        lineNumber = 1
        with open("114.txt", "w", encoding="UTF-8") as file:
            for line in lines:
                if lineNumber == 159:
                    pass
                else:
                    file.write(line)
                lineNumber += 1
        file.close()

        shutil.copyfile(f"dependencies/haruka/macro.ks", f"compile/scenario/macro.ks")  # Copies the macro.ks file that doesn't need to be changed.
        for count in range(1, 114 + 1):  # Used to iterate through the files.
            formattedFileName = harukaFileNames(count)  # Calls the function and stores the current value in a variable.
            unformattedFileName = str(count) + ".txt"  # Increases the value of the unformatted file that is called.

            newFile = open(f"dependencies/haruka/{formattedFileName}", "r", encoding="Shift_JIS")  # Opens the file stream for the formatted (new) file.
            formatted = newFile.readlines()  # Reads the lines from the file and inserts it into a variable.
            newFile.close()  # Closes the file stream for the formatted (new) file.

            oldFile = open(f"{unformattedFileName}", "r", encoding="UTF-8")  # Opens the file stream for the unformatted (old) file.
            unformatted = oldFile.readlines()  # Reads the lines from the file and inserts it into a variable.
            oldFile.close()  # Closes the file stream for the unformatted (old) file.

            fileConverter(formatted, unformatted, formattedFileName)  # Calls the fileConverter function to move the data between files.


def fileConverter(formatted, unformatted, formattedFileName):  # Converts the chapter files into KiriKiri files.
    if '\n' in unformatted[len(unformatted) - 1]:
        pass
    else:
        unformatted[len(unformatted) - 1] = unformatted[len(unformatted) - 1] + "\n"
    count = 0
    for x in range(0, len(formatted)):
        if x > len(formatted) - 1:
            break
        tempcount = 1
        if "@Hit" in formatted[x]:
            while True:
                if "@Talk name=" in formatted[x - tempcount]:
                    break
                else:
                    del formatted[x - tempcount]
                    tempcount += 1
        else:
            pass

    y = 0
    while True:
        if count > len(unformatted) - 1:
            break

        if "@Talk name=" in formatted[y] and "@Hit" in formatted[y + 1]:
            val = unformatted[count]
            wrapper = textwrap.TextWrapper(width=60)
            word_list = wrapper.wrap(text=val)
            word_list[len(word_list) - 1] = str(word_list[len(word_list) - 1] + "\n")
            formatted.insert(y + 1, "\n".join(word_list))
            count += 1
        else:
            pass
        y += 1

    file = open(f"compile/scenario/{formattedFileName}", "w", encoding='UTF-16')  # Opens the file stream for the final file.
    file.write(str(''.join(formatted)))  # Writes the data from the variable to the file.
    file.close()


def yosugaFileNames(count):  # A function used to give the specific names of the new files for Yosuga no Sora.
    match count:
        case 1:
            return "00_a001.ks"  # Start of Sora's Route
        case 2:
            return "00_a002.ks"
        case 3:
            return "00_a003.ks"
        case 4:
            return "00_a004.ks"
        case 5:
            return "00_a005.ks"
        case 6:
            return "00_a006.ks"
        case 7:
            return "00_a007.ks"
        case 8:
            return "00_a008.ks"
        case 9:
            return "00_a009.ks"
        case 10:
            return "00_a010.ks"
        case 11:
            return "00_a011.ks"
        case 12:
            return "00_a012.ks"
        case 13:
            return "00_a013.ks"
        case 14:
            return "00_a014.ks"
        case 15:
            return "00_a015a.ks"
        case 16:
            return "00_a015b.ks"
        case 17:
            return "00_a015c.ks"
        case 18:
            return "00_a016a.ks"
        case 19:
            return "00_a016b.ks"
        case 20:
            return "00_a016c.ks"
        case 21:
            return "00_a017.ks"
        case 22:
            return "00_a018a.ks"
        case 23:
            return "00_a018b.ks"
        case 24:
            return "00_a018c.ks"
        case 25:
            return "00_a019.ks"
        case 26:
            return "00_a020.ks"
        case 27:
            return "00_a021.ks"
        case 28:
            return "00_a022.ks"
        case 29:
            return "00_a023a.ks"
        case 30:
            return "00_a023b.ks"
        case 31:
            return "00_a024.ks"
        case 32:
            return "00_a025a.ks"
        case 33:
            return "00_a025b.ks"
        case 34:
            return "00_a025c.ks"
        case 35:
            return "00_a026.ks"
        case 36:
            return "00_a027.ks"
        case 37:
            return "00_a028a.ks"
        case 38:
            return "00_a028b.ks"
        case 39:
            return "00_a028c.ks"
        case 40:
            return "00_a028d.ks"
        case 41:
            return "00_a029a.ks"
        case 42:
            return "00_a029b.ks"
        case 43:
            return "00_a030.ks"
        case 44:
            return "00_a031.ks"
        case 45:
            return "00_a032.ks"
        case 46:
            return "00_a033.ks"
        case 47:
            return "00_a034.ks"
        case 48:
            return "00_b001.ks"  # Start of Nao's Route
        case 49:
            return "00_b001b.ks"
        case 50:
            return "00_b001c.ks"
        case 51:
            return "00_b001d.ks"
        case 52:
            return "00_b002.ks"
        case 53:
            return "00_b003.ks"
        case 54:
            return "00_b003b.ks"
        case 55:
            return "00_b003c.ks"
        case 56:
            return "00_b004.ks"
        case 57:
            return "00_b005.ks"
        case 58:
            return "00_b006.ks"
        case 59:
            return "00_b007.ks"
        case 60:
            return "00_b007b.ks"
        case 61:
            return "00_b007c.ks"
        case 62:
            return "00_b007d.ks"
        case 63:
            return "00_b008.ks"
        case 64:
            return "00_b008b.ks"
        case 65:
            return "00_b008c.ks"
        case 66:
            return "00_b009.ks"
        case 67:
            return "00_b009b.ks"
        case 68:
            return "00_b010.ks"
        case 69:
            return "00_b011.ks"
        case 70:
            return "00_b012.ks"
        case 71:
            return "00_b013.ks"
        case 72:
            return "00_b013b.ks"
        case 73:
            return "00_b013c.ks"
        case 74:
            return "00_b013d.ks"
        case 75:
            return "00_b014.ks"
        case 76:
            return "00_b015.ks"
        case 77:
            return "00_b015b.ks"
        case 78:
            return "00_b015c.ks"
        case 79:
            return "00_b015d.ks"
        case 80:
            return "00_b015e.ks"
        case 81:
            return "00_b016.ks"
        case 82:
            return "00_b016b.ks"
        case 83:
            return "00_b017.ks"
        case 84:
            return "00_b018.ks"
        case 85:
            return "00_b018b.ks"
        case 86:
            return "00_b019.ks"
        case 87:
            return "00_b020.ks"
        case 88:
            return "00_b020b.ks"
        case 89:
            return "00_b020c.ks"
        case 90:
            return "00_b021.ks"
        case 91:
            return "00_b022.ks"
        case 92:
            return "00_b022b.ks"
        case 93:
            return "00_b023.ks"
        case 94:
            return "00_b024.ks"
        case 95:
            return "00_b024b.ks"
        case 96:
            return "00_b025.ks"
        case 97:
            return "00_b026.ks"
        case 98:
            return "00_b026b.ks"
        case 99:
            return "00_b026c.ks"
        case 100:
            return "00_b027.ks"
        case 101:
            return "00_b027b.ks"
        case 102:
            return "00_b027c.ks"
        case 103:
            return "00_b028.ks"
        case 104:
            return "00_b028b.ks"
        case 105:
            return "00_b029.ks"
        case 106:
            return "00_b029b.ks"
        case 107:
            return "00_b029c.ks"
        case 108:
            return "00_b030.ks"
        case 109:
            return "00_b031.ks"
        case 110:
            return "00_b031b.ks"
        case 111:
            return "00_b032.ks"
        case 112:
            return "00_b033.ks"
        case 113:
            return "00_b034.ks"
        case 114:
            pass
        case 115:
            return "00_c001.ks"  # Start of Akira's Route
        case 116:
            return "00_c002.ks"
        case 117:
            return "00_c002b.ks"
        case 118:
            return "00_c003.ks"
        case 119:
            return "00_c004.ks"
        case 120:
            return "00_c005.ks"
        case 121:
            return "00_c006.ks"
        case 122:
            return "00_c006b.ks"
        case 123:
            return "00_c007.ks"
        case 124:
            return "00_c008.ks"
        case 125:
            return "00_c008b.ks"
        case 126:
            return "00_c008c.ks"
        case 127:
            return "00_c009.ks"
        case 128:
            return "00_c009b.ks"
        case 129:
            return "00_c010.ks"
        case 130:
            return "00_c010b.ks"
        case 131:
            return "00_c011.ks"
        case 132:
            return "00_c012.ks"
        case 133:
            return "00_c012b.ks"
        case 134:
            return "00_c013.ks"
        case 135:
            return "00_c013b.ks"
        case 136:
            return "00_c013c.ks"
        case 137:
            return "00_c013d.ks"
        case 138:
            return "00_c013e.ks"
        case 139:
            return "00_c014.ks"
        case 140:
            return "00_c014b.ks"
        case 141:
            return "00_c014c.ks"
        case 142:
            return "00_c014d.ks"
        case 143:
            return "00_c014e.ks"
        case 144:
            return "00_c014f.ks"
        case 145:
            return "00_c015.ks"
        case 146:
            return "00_c015b.ks"
        case 147:
            return "00_c016.ks"
        case 148:
            return "00_c016b.ks"
        case 149:
            return "00_c016c.ks"
        case 150:
            return "00_c017.ks"
        case 151:
            return "00_c018.ks"
        case 152:
            return "00_c019.ks"
        case 153:
            return "00_c019b.ks"
        case 154:
            return "00_c020.ks"
        case 155:
            return "00_c020b.ks"
        case 156:
            return "00_c021.ks"
        case 157:
            return "00_c022.ks"
        case 158:
            return "00_c022b.ks"
        case 159:
            return "00_c022c.ks"
        case 160:
            return "00_c023.ks"
        case 161:
            return "00_c024.ks"
        case 162:
            return "00_c025.ks"
        case 163:
            return "00_c025b.ks"
        case 164:
            return "00_c026.ks"
        case 165:
            return "00_c027.ks"
        case 166:
            return "00_c028.ks"
        case 167:
            return "00_c029.ks"
        case 168:
            return "00_c029b.ks"
        case 169:
            return "00_c030.ks"
        case 170:
            return "00_c031.ks"
        case 171:
            return "00_c031b.ks"
        case 172:
            return "00_c032.ks"
        case 173:
            return "00_c032b.ks"
        case 174:
            return "00_c033.ks"
        case 175:
            return "00_c033b.ks"
        case 176:
            return "00_c033c.ks"
        case 177:
            return "00_c034.ks"
        case 178:
            return "00_c035.ks"
        case 179:
            return "00_c035b.ks"
        case 180:
            return "00_c036.ks"
        case 181:
            return "00_d001.ks"  # Start of Kazuha's Route
        case 182:
            return "00_d002.ks"
        case 183:
            return "00_d003.ks"
        case 184:
            return "00_d004.ks"
        case 185:
            return "00_d005.ks"
        case 186:
            return "00_d006.ks"
        case 187:
            return "00_d007.ks"
        case 188:
            return "00_d008.ks"
        case 189:
            return "00_d009.ks"
        case 190:
            return "00_d010.ks"
        case 191:
            return "00_d010b.ks"
        case 192:
            return "00_d011.ks"
        case 193:
            return "00_d011b.ks"
        case 194:
            return "00_d012.ks"
        case 195:
            return "00_d013.ks"
        case 196:
            return "00_d014.ks"
        case 197:
            return "00_d014b.ks"
        case 198:
            return "00_d015.ks"
        case 199:
            return "00_d016.ks"
        case 200:
            return "00_d017.ks"
        case 201:
            return "00_d017b.ks"
        case 202:
            return "00_d018.ks"
        case 203:
            return "00_d019.ks"
        case 204:
            return "00_d019b.ks"
        case 205:
            return "00_d019c.ks"
        case 206:
            return "00_d020.ks"
        case 207:
            return "00_d021.ks"
        case 208:
            return "00_d022.ks"
        case 209:
            return "00_d023.ks"
        case 210:
            return "00_d023b.ks"
        case 211:
            return "00_d024.ks"
        case 212:
            return "00_d024b.ks"
        case 213:
            return "00_d025.ks"
        case 214:
            return "00_d025b.ks"
        case 215:
            return "00_d026.ks"
        case 216:
            return "00_d027.ks"
        case 217:
            return "00_d028.ks"
        case 218:
            return "00_d028b.ks"
        case 219:
            return "00_d029.ks"
        case 220:
            return "00_d030.ks"
        case 221:
            return "00_d030b.ks"
        case 222:
            return "00_d031.ks"
        case 223:
            return "00_d032.ks"
        case 224:
            return "00_d033.ks"
        case 225:
            return "00_d034.ks"
        case 226:
            return "00_d035.ks"
        case 227:
            return "00_d036.ks"
        case 228:
            return "00_d037.ks"
        case 229:
            return "00_d038.ks"
        case 230:
            return "00_d039.ks"
        case 231:
            return "00_d040.ks"
        case 232:
            return "00_d041.ks"
        case 233:
            return "00_d042.ks"
        case 234:
            return "00_d042b.ks"
        case 235:
            return "00_d043.ks"
        case 236:
            return "00_d044.ks"
        case 237:
            return "00_e000.ks"  # Start of Motoka's Route
        case 238:
            return "00_e001.ks"
        case 239:
            return "00_e002.ks"
        case 240:
            return "00_e003a.ks"
        case 241:
            return "00_e003b.ks"
        case 242:
            return "00_e004.ks"
        case 243:
            return "00_e005.ks"
        case 244:
            return "00_e006.ks"
        case 245:
            return "00_e007.ks"
        case 246:
            return "00_e008.ks"
        case 247:
            return "00_e009a.ks"
        case 248:
            return "00_e009b.ks"
        case 249:
            return "00_e010.ks"
        case 250:
            return "00_e011.ks"
        case 251:
            return "00_e012a.ks"
        case 252:
            return "00_e012b.ks"
        case 253:
            return "00_e013a.ks"
        case 254:
            return "00_e013b.ks"
        case 255:
            return "00_e013c.ks"
        case 256:
            return "00_e014.ks"
        case 257:
            return "00_e015.ks"
        case 258:
            return "00_e016.ks"
        case 259:
            return "00_e017a.ks"
        case 260:
            return "00_e018.ks"
        case 261:
            return "00_e018b.ks"
        case 262:
            return "00_e018c.ks"
        case 263:
            return "00_e019.ks"
        case 264:
            return "00_e020.ks"
        case 265:
            return "00_e021.ks"
        case 266:
            return "00_e022.ks"
        case 267:
            return "00_e023.ks"
        case 268:
            return "00_e024.ks"
        case 269:
            return "00_e024b.ks"
        case 270:
            return "00_e025.ks"
        case 271:
            return "00_e026.ks"
        case 272:
            return "00_e027.ks"
        case 273:
            return "00_e028.ks"
        case 274:
            return "00_e028b.ks"
        case 275:
            return "00_e029.ks"
        case 276:
            return "00_e030.ks"
        case 277:
            return "00_e031.ks"
        case 278:
            return "00_e032.ks"
        case 279:
            return "00_e032b.ks"
        case 280:
            return "00_e033.ks"
        case 281:
            return "00_e034.ks"
        case 282:
            return "00_e034b.ks"
        case 283:
            return "00_e035.ks"
        case 284:
            return "00_e036.ks"
        case 285:
            return "00_e036b.ks"
        case 286:
            return "00_e037.ks"
        case 287:
            return "00_g000.ks"  # Start of ??? Route
        case 288:
            return "00_g001.ks"
        case 289:
            return "00_g002.ks"
        case 290:
            return "00_g003.ks"
        case 291:
            return "00_z000.ks"  # Start of Common Route
        case 292:
            return "00_z001.ks"
        case 293:
            return "00_z002.ks"
        case 294:
            return "00_z003.ks"
        case 295:
            return "00_z004.ks"
        case 296:
            return "00_z005.ks"
        case 297:
            return "00_z006.ks"
        case 298:
            return "00_z007.ks"
        case 299:
            return "00_z008.ks"
        case 300:
            return "00_z009.ks"
        case 301:
            return "00_z010.ks"
        case 302:
            return "00_z011.ks"
        case 303:
            return "00_z012.ks"
        case 304:
            return "00_z013.ks"
        case 305:
            return "00_z014.ks"
        case 306:
            return "00_z015.ks"
        case _:
            return "Error! Make sure you are in the scenario folder, a file should look something like 00_a001.ks"


def harukaFileNames(count):  # A function used to give the specific names of the new files for Haruka na Sora.
    match count:
        case 1:
            return "00_a001.ks"  # Start of Sora's Route
        case 2:
            return "00_a002.ks"
        case 3:
            return "00_a003.ks"
        case 4:
            return "00_a004.ks"
        case 5:
            return "00_a005.ks"
        case 6:
            return "00_a006.ks"
        case 7:
            return "00_a007a.ks"
        case 8:
            return "00_a007b.ks"
        case 9:
            return "00_a007c.ks"
        case 10:
            return "00_a008.ks"
        case 11:
            return "00_a009.ks"
        case 12:
            return "00_a010a.ks"
        case 13:
            return "00_a010b.ks"
        case 14:
            return "00_a011.ks"
        case 15:
            return "00_a012.ks"
        case 16:
            return "00_a013a.ks"
        case 17:
            return "00_a013b.ks"
        case 18:
            return "00_a013c.ks"
        case 19:
            return "00_a013d.ks"
        case 20:
            return "00_a013e.ks"
        case 21:
            return "00_a014a.ks"
        case 22:
            return "00_a014b.ks"
        case 23:
            return "00_a014c.ks"
        case 24:
            return "00_a015a.ks"
        case 25:
            return "00_a015b.ks"
        case 26:
            return "00_a016.ks"
        case 27:
            return "00_a017.ks"
        case 28:
            return "00_a017b.ks"
        case 29:
            return "00_a017c.ks"
        case 30:
            return "00_a018.ks"
        case 31:
            return "00_a019a.ks"
        case 32:
            return "00_a019b.ks"
        case 33:
            return "00_a020.ks"
        case 34:
            return "00_a021.ks"
        case 35:
            return "00_a022.ks"
        case 36:
            return "00_g001.ks"  # Start of Yahiro's Route
        case 37:
            return "00_g002.ks"
        case 38:
            return "00_g002b.ks"
        case 39:
            return "00_g003.ks"
        case 40:
            return "00_g004.ks"
        case 41:
            return "00_g005.ks"
        case 42:
            return "00_g006.ks"
        case 43:
            return "00_g007.ks"
        case 44:
            return "00_g008.ks"
        case 45:
            return "00_g009.ks"
        case 46:
            return "00_g010.ks"
        case 47:
            return "00_g010b.ks"
        case 48:
            return "00_g011.ks"
        case 49:
            return "00_g012.ks"
        case 50:
            return "00_g013.ks"
        case 51:
            return "00_g014.ks"
        case 52:
            return "00_g015.ks"
        case 53:
            return "00_g015b.ks"
        case 54:
            return "00_g016.ks"
        case 55:
            return "00_g017.ks"
        case 56:
            return "00_g017b.ks"
        case 57:
            return "00_g018.ks"
        case 58:
            return "00_g019.ks"
        case 59:
            return "00_g020.ks"
        case 60:
            return "00_g021.ks"
        case 61:
            return "00_g022.ks"
        case 62:
            return "00_g023.ks"
        case 63:
            return "00_g024.ks"
        case 64:
            return "00_g025.ks"
        case 65:
            return "00_h001.ks"  # Start of Kozue's Route
        case 66:
            return "00_h002.ks"
        case 67:
            return "00_h003.ks"
        case 68:
            return "00_h004.ks"
        case 69:
            return "00_h005.ks"
        case 70:
            return "00_h006.ks"
        case 71:
            return "00_h007.ks"
        case 72:
            return "00_h008.ks"
        case 73:
            return "00_h009.ks"
        case 74:
            return "00_h010a.ks"
        case 75:
            return "00_h010b.ks"
        case 76:
            return "00_h011a.ks"
        case 77:
            return "00_h011b.ks"
        case 78:
            return "00_h012.ks"
        case 79:
            return "00_h013a.ks"
        case 80:
            return "00_h013b.ks"
        case 81:
            return "00_h014.ks"
        case 82:
            return "00_h015a.ks"
        case 83:
            return "00_h015b.ks"
        case 84:
            return "00_h015c.ks"
        case 85:
            return "00_h015d.ks"
        case 86:
            return "00_h016.ks"
        case 87:
            return "00_h017.ks"
        case 88:
            return "00_h018a.ks"
        case 89:
            return "00_h018b.ks"
        case 90:
            return "00_h019a.ks"
        case 91:
            return "00_h019b.ks"
        case 92:
            return "00_h020.ks"
        case 93:
            return "00_h021.ks"
        case 94:
            return "00_h022.ks"
        case 95:
            return "00_h023.ks"
        case 96:
            return "00_h024.ks"
        case 97:
            return "00_h025.ks"
        case 98:
            return "00_h026.ks"
        case 99:
            return "00_h027.ks"
        case 100:
            return "00_h028.ks"
        case 101:
            return "00_h029.ks"
        case 102:
            return "00_h030a.ks"
        case 103:
            return "00_h030b.ks"
        case 104:
            return "00_h031a.ks"
        case 105:
            return "00_h031b.ks"
        case 106:
            return "00_h032.ks"
        case 107:
            return "countdown.ks"  # Countdown Scenario
        case 108:
            return "karaoke.ks"  # Rappa Sushi Karaoke Scenario
        case 109:
            return "web01.ks"  # Start of Web Scenario
        case 110:
            return "web02.ks"
        case 111:
            return "web03.ks"
        case 112:
            return "web04.ks"
        case 113:
            return "web05.ks"
        case 114:
            return "web06.ks"


print("Yosuga no Sora/Haruka na Sora EntisGLS to KiriKiri Convertor")
print("Created by MrWicked @ https://github.com/TheRealMrWicked/Yosuga-no-Sora-Patch-Conversion\n")

dependencies()

print("Which game do you want to convert?\n")
print("1. Yosuga no Sora. (yosuga.csx)")
print("2. Haruka na Sora. (Haruka.csx)")

while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice >= 3:
        print("Please enter a valid choice.")
        continue
    else:
        break

csxDecrypter(choice)
utfCombiner()
textReplacer(choice)
chapterCreator()
fileImporter(choice)
deleteMiscFiles()

if choice == 1:
    shutil.copyfile(f"dependencies/yosuga/begin.tjs", f"compile/begin.tjs")
    shutil.copyfile(f"dependencies/yosuga/startup.tjs", f"compile/startup.tjs")
    shutil.copytree(f"dependencies/yosuga/system", f"compile/system")
elif choice == 2:
    shutil.copyfile(f"dependencies/haruka/begin.tjs", f"compile/begin.tjs")
    shutil.copyfile(f"dependencies/haruka/startup.tjs", f"compile/startup.tjs")
    shutil.copytree(f"dependencies/haruka/system", f"compile/system")

input("Success the compile folder has been created.")
