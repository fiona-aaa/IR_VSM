import os
import string
class Doc:
    """
    用来存储dataset中文档的诗名、作者、诗句
    """
    poem_name = None
    author = None
    content = None

    def __init__(self, poem_name):
        self.poem_name = poem_name

path = r'F:\workspace\pycharmProjects\IR_VSM\dataset'
file_num = 0
file_name_list = []

if os.path.exists(path):
    # 读取文档名到列表，文档数量
    file_name_list = os.listdir(path)
    file_num = len(file_name_list)
    # print(file_num)
    # print(file_name_list)
    # print(type(file_name_list[0])) # str类型

else:
    print('Error: this path not exist.')

# names = globals()
doc = []
for i in range(file_num):
    # names['doc' + str(i)] = Doc(file_name_list[i])
    # exec('doc{} = {}'.format(i,Doc(file_name_list[i-1])))
    # doc.append('doc' + str(i))
    doc.append(Doc(file_name_list[i]))
    # remove ".txt"
    doc[i].poem_name = doc[i].poem_name[:-4]
    # print(doc[i].poem_name)

# 读文档的第一行（author）
i = 0
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    # print(file_path)
    # print(type(file_path))
    with open(file_path, 'r') as f:
        doc[i].author = f.readline()
        lines = f.readlines()
        doc[i].content = str('')
        for line in lines:
            doc[i].content = doc[i].content + line
        doc[i].content = doc[i].content.replace('\n', ' ')
        for c in string.punctuation:
            doc[i].content = doc[i].content.replace(c, '')
            doc[i].author = doc[i].author.replace(c, '')
        # print(doc[i].author)
        # if i == 0 or i == 8:
            # print(doc[i].content)
    i += 1












