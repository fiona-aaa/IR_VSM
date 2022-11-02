### <center>向量空间模型实验报告</center>
<center>计算机科学与技术  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 2012679 &nbsp&nbsp王娇妹</center>

#### 实验内容
1. 给定查询文档集合（诗词txt文件），完成向量空间模型并对文档集合实现查询功能。
2. 实现带域的查询功能，具体为诗名、作者、诗句三个域，要求实现自定义组合域中的查询。

#### 设计思路
##### 1、读取文档

我构建了一个Doc类，用来存储某个文档的词项，它含有三个成员变量，分别是poem_name、author和content，对应三个域中的词项，并将域中的内容以字符串的形式保存。
 ```python
class Doc:
    """
    用来存储dataset中文档的诗名、作者、诗句
    """
    poem_name = None
    author = None
    content = None
    def __init__(self, poem_name):
        self.poem_name = poem_name
 ```
* 诗名
诗名就是文档的名字。
我借助os.listdir函数，顺序读取所有的文档名，存到列表中，并计算文档总数，便于后面索引文档。

 ```python
if os.path.exists(path):
    # 读取文档名（str类型）到列表，计算文档数量
    file_name_list = os.listdir(path)
    file_num = len(file_name_list)
else: # 路径不存在
    print('Error: this path not exist.')
 ```
 这一步骤读取的文档名带有.txt后缀，通过切片去掉。

 ```python
 # 用doc列表来保存每个文档的class实例（包括诗名、作者、诗句）
 doc = []
 # 读文档的诗名（poem_name）
for i in range(file_num):
    doc.append(Doc(file_name_list[i]))
    # remove ".txt"
    doc[i].poem_name = doc[i].poem_name[:-4]
 ```
* 作者
作者部分位于txt文档内容的第一行。
* 诗句
诗句是txt文档除第一行以外的部分。
 ```python
 # 读文档的第一行（author）和剩余部分（content）
i = 0
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    with open(file_path, 'r') as f:
        doc[i].author = f.readline()
        lines = f.readlines()
        doc[i].content = str('')
        for line in lines:
            doc[i].content = doc[i].content + line
 ```

##### 处理文档


##### 自定义组合域


##### 计算 $tf$ 和 $idf$ 


##### 向量表示查询和文档


##### 余弦相似度
   
#### 运行测试