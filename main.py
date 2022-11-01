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


def read_files(path):
    """
    1.读取数据集中各文档，并分块保存。
    2.去除换行符、标点符号，全部统一为小写字母。
    3.单词变原型，没搜到相应的包，暂时没做。
    :param path: 数据集路径
    :return: doc 列表，存储每个文档各部分；file_num，文档数量
    """
    file_num = 0
    file_name_list = []
    # 读取文档名到列表，计算文档数量
    if os.path.exists(path):
        file_name_list = os.listdir(path)
        file_num = len(file_name_list)
        # print(file_num)
        # print(file_name_list)
        # print(type(file_name_list[0])) # str类型
    else:
        print('Error: this path not exist.')
    # 用doc列表来保存每个文档的class实例（包括诗名、作者、诗句）
    doc = []
    # names = globals()

    # 读文档的诗名（poem_name）
    for i in range(file_num):
        # names['doc' + str(i)] = Doc(file_name_list[i])
        # exec('doc{} = {}'.format(i,Doc(file_name_list[i-1])))
        # doc.append('doc' + str(i))
        doc.append(Doc(file_name_list[i]))
        # remove ".txt"
        doc[i].poem_name = doc[i].poem_name[:-4]
        # print(doc[i].poem_name)

    # 读文档的第一行（author）和剩余部分（content）
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
            # 去掉换行符
            # author（第一行）也有个换行符，要注意
            doc[i].author = doc[i].author.replace('\n', '')
            doc[i].content = doc[i].content.replace('\n', ' ')
            # 去掉标点符号
            for c in string.punctuation:
                doc[i].content = doc[i].content.replace(c, '')
                doc[i].author = doc[i].author.replace(c, '')
            # 单词统一为小写
            doc[i].poem_name = doc[i].poem_name.lower()
            doc[i].author = doc[i].author.lower()
            doc[i].content = doc[i].content.lower()
            # 测试处理后的文档
            # if i == 0 or i == 8:
            # print(doc[i].poem_name)
            # print(doc[i].author)
            # print(doc[i].content)
        i += 1
    return doc, file_num


def select_query_scope(doc, file_num, poem_name_query, author_query, content_query):
    new_doc = []
    for i in range(file_num):
        new_doc.append('')
        if poem_name_query:
            new_doc[i] = new_doc[i] + ' ' + doc[i].poem_name
        if author_query:
            new_doc[i] = new_doc[i] + ' ' + doc[i].author
        if content_query:
            # 可能会导致多几个空格，应该没有影响吧?-----已解决
            new_doc[i] = new_doc[i] + ' ' + doc[i].content
    return new_doc


if __name__ == '__main__':

    dataset_path = r'F:\workspace\pycharmProjects\IR_VSM\dataset'
    doc, file_num = read_files(dataset_path)
    """
    print(file_num)
    print(doc[2].poem_name)
    print(doc[2].author)
    print(doc[2].content)
    """
    # 诗名、作者、诗句
    print("--------------------请选择您的查询范围--------------------------")
    print("查询范围包括诗名、作者和诗句")
    print("选择该范围请输1, 不选择请输0")

    poem_name_query = int(input("查询诗名："))
    author_query = int(input("查询作者："))
    content_query =  int(input("查询诗句："))

    if not (poem_name_query or author_query or content_query):
        print("ERROR: 查询范围为空")
    else:
        newdoc = select_query_scope(doc, file_num, poem_name_query, author_query, content_query)
        # print(newdoc[4])
        # 对所有文档排序，并统计不同词项的数量
        terms_num = 0
        terms_list = []
        for i in range(file_num):
            # 解决上面select_query_scope可能多加了空格的问题
            newdoc[i] = newdoc[i].strip(' ')
            #print(newdoc[i])
            term_list = newdoc[i].split(' ')
            #print(term_list)
            # 借助集合去重
            term_list = list(set(term_list))
            #print(term_list)
            for item in terms_list:
                if item == '':
                    term_list.remove('')
            #print(term_list)
            terms_list.extend(term_list)

        print(len(terms_list))
        terms_list = list(set(terms_list))
        terms_num = len(terms_list)
        print(terms_num)
        print(terms_list)
        terms_list = sorted(terms_list)
        print(len(terms_list))
        print(terms_list)















