# 0
def power_2(power=38):
    return 2**power

# 1
def map(string, shift):
    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghijklmnopqrstuvwxyz"
    message = ""
    for letter in string:
        if letter in cap_letters:
            index = cap_letters.index(letter)
            new_index = index + shift
            message = message + cap_letters[new_index % len(cap_letters)]
        if letter in letters:
            index = letters.index(letter)
            new_index = index + shift
            message = message + letters[new_index % len(letters)]
        else:
            message = message + letter
    return message

# 2
def import_text(filename):
    with open(filename, 'r') as file:
        text = file.read().replace('\n', '')
    return text

def extract_text(string):
    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghijklmnopqrstuvwxyz"
    message = ""
    for character in string:
        if character in letters:
            message = message + character
        if character in cap_letters:
            message = message + character
    return message

# 3
def three_small_three(string):
    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghijklmnopqrstuvwxyz"
    index = 3
    message = ''
    while index < len(string) - 4:
        lead_string = string[index - 3:index]
        tail_string = string[index + 1 : index + 4]
        flag = True
        if string[index - 4] not in letters:
            flag = False
        if string[index + 4] not in letters:
            flag = False
        for letter in lead_string:
            if letter not in cap_letters:
                flag = False
        for letter in tail_string:
            if letter not in cap_letters:
                flag = False
        if string[index] not in letters:
            flag = False
        if flag:
            message = message + string[index]
        index += 1
    return message

# 4. Linked List
def linked_list():
    import urllib
    url_prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    nothing = '12345'
    for count in range(400):
        page = urllib.request.urlopen(url_prefix + nothing).read()
        string = str(page)[2:-1]
        if string.rfind(' ') == -1:
            return string
        else:
            nothing = string[string.rfind(' ') + 1:]
        # print(nothing)

# 5. Peak hell (peak.html)
# Need to import pickle
def peak_hell():
    import pickle
    with open('banner.p', 'rb') as file:
        unpickled = pickle.load(file)
    message = ''
    for item in unpickled:
        for subitem in item:
            message = message + subitem[0] * subitem[1]
        message = message + '\n'
    print(message)

# 6. Channel
def channel():
    nothing = '90052'
    for i in range(911):
        with open('channel-zip/' + nothing + '.txt') as file:
            string = file.read()
        space_pos = string.rfind(' ')
        nothing = string[space_pos + 1:]
        print(string)

# 7. Oxygen
def oxygen():
    import PIL.Image as Image
    import codecs
    file_loc = 'oxygen.png'
    pic = Image.open(file_loc)
    width, height = pic.size
    colors = []
    y = int(height/2)
    for x in range(0, width, 7):
        colors.append( hex(pic.getpixel((x, y))[0])[2:] )
    message = ''
    for color in colors:
        message = message + str(codecs.decode(color,'hex'), 'utf-8')
    # message is : 'smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]'
    level_array = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    level = ''
    for character in level_array:
        level = level + str(codecs.decode(hex(character)[2:], 'hex'), 'utf-8')
    return level

# 8. Integrity
def integrity():
    import bz2
    import codecs
    un = r'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = r'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    un = un.encode('latin1').decode('unicode_escape').encode('latin1')
    pw = pw.encode('latin1').decode('unicode_escape').encode('latin1')
    return str(bz2.decompress(un))[2:-1], str(bz2.decompress(pw))[2:-1]
    # returns: 'huge', 'file'

# 9. Good
def good():
    import matplotlib.pyplot as plt
    import numpy as np

    first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
332,155,348,156,353,153,366,149,379,147,394,146,399]
    second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136]

    first_x = first[0::2]
    first_y = first[1::2]
    second_x = second[0::2]
    second_y = second[1::2]

    plt.plot(first_x, -np.array(first_y), '-')
    plt.plot(second_x, -np.array(second_y), '-')
    plt.axis('equal')
    plt.show()

# 10. Bull
def bull():
    a = []
    string = '1'
    a.append(string)
    for count in range(35):
        length = len(string)
        if length == 1:
            string = '1' + string
            a.append(string)
        else:
            new_string = ""
            repeats = 1
            for i in range(1, len(string)):
                if string[i] == string[i-1]:
                    repeats += 1
                else:
                    new_string = new_string + str(repeats) + string[i-1]
                    repeats = 1
            new_string = new_string + str(repeats) + string[-1]
            a.append(new_string)
            string = new_string
    return a

# 11. 5808
# Initially solved this by luck. My hover preview in Windows showed the solution.
def image_split():
    pass

# 12. Evil
def evil():
    pass
