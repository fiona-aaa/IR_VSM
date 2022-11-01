import os
class Doc:
    """
    用来存储dataset中文档的诗名、作者、诗句
    """
    poem_name = None
    author = None
    content = None
    def __init__(self,poem_name):
        self.poem_name = poem_name


path=r'F:\workspace\pycharmProjects\IR_VSM\dataset'
file_num = 0
file_name_list = []
# 读取文档名到列表，文档数量
if os.path.exists(path):
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
    print(doc[i].poem_name)






