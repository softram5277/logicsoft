
data = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'], 'is': ['doc1', 'doc2'],
        'james': ['doc1', 'doc2'],'a': ['doc2'], 'developer': ['doc2']}

data1=sorted(data.items(),key=lambda x:str(len(x[1]))+x[0])
print(data1)

