import os
while True:
    content=input('请输入目录：')  # file04
    if os.path.exists(content):
        '''表示路径存在'''
        os.chdir(content)  # 切换到输入的目录 切换到了file04目录
        all_file_lst=os.listdir(os.getcwd())
        # 获取目录列表形式 将file03目录下的文件或者文件夹以列表形式打印
        print(all_file_lst) # ['c.txt', 'demon01.py', 'file05', '__init__.py']
        file_lst=[]   # 保存所有文件
        dir_lst=[]   # 保存所有文件夹
        
        for file in all_file_lst:
            if os.path.isfile(file):  # 判断当前目录下面的内容是否为文件
                '''文件'''
                file_lst.append(file)
            else:
                '''文件夹'''
                dir_lst.append(file)
        # 打印所有的文件和文件夹
        print('文件{}：'.format(file_lst))
        print('文件夹{}'.format(dir_lst))
 
        ret=input('请选择操作：添加前缀(A) 删除前缀(D) 添加文件(c) 删除文件(del) 修改文件名称(R)')
        if ret.lower() == 'a':
            prefix=input('请输入前缀：')
            for file in all_file_lst:
                os.rename(file,prefix+file)
 
            print('前缀添加成功了...')
        elif ret.lower() == 'd':
            prefix = input('请输入要删除的前缀：')
            for file in all_file_lst:
 
                os.rename(file, file.replace(prefix,'',1))
            print('删除前缀成功了...')
 
        elif ret.lower() == 'c':
            file_name=input('请输入文件名称:')
            with open(file_name,mode='w') as f:
                pass
            print('亲，创建成功了')
 
        elif ret.lower() == 'del':
            file_name=input('请输入要删除的文件名称：')
            os.remove(file_name)
            print('删除文件成功...')
        elif ret.lower() == 'r':
            file=input('请输入要修改的名称和新名称[old new]')
            file = file.split()
            os.rename(file[0],file[1])
            print('修改成功了...')
 
        else:
            print('亲，输错啦...')
 
 
    else:
        print('此路径不存在...')
  
