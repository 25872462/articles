'''
コマンドライン引数の雛形
2022/09/02/20:00
'''

import sys


def printhelp(str):
    print('Erorr:',str)
    print('Usage:python + option')
    print('-p1 textfile')
    print('-p2 wavefile')
    sys.exit()


def check(args):#コマンドライン引数のチェック
    '''
    想定している引数
    1. python filename
    2. python -p1 filename -p2 filename
    3. python -p2 filename -p1 filename
    - オプションは自由な順番でつけれる 
    '''
    
    #引数の数
    argc = len(args)
    
    
    #初期化 f:filename, p:option flag
    f,f1,f2 = 0,0,0,
    optionlist = [0,0]
    
    #探索
    for i in range(1,argc):
        
        #助けを呼んでいたら
        if(args[i] == '--help' or args[i] == '-h'):
            printhelp('I come here to help you!')
        
        elif(args[i] == '-p1'):
            #引数が配列外参照していたら
            if(i+1 >= argc):
                printhelp('Over array access')
            optionlist[0] = optionlist[0] + 1
            f1 = args[i+1]
        
        elif(args[i] == '-p2'):
            #引数が配列外参照していたら
            if(i+1 >= argc):
                printhelp('Over array access')
            optionlist[1] = optionlist[1] + 1
            f2 = args[i+1]
            
        elif(args[i][0] == '-'):
            printhelp('I don\'t know this option')
        
    #もし同じオプションを指定していたら
    if(optionlist[0] > 1 or optionlist[1] > 1):
        printhelp('You use same options')
            
    #もしオプション指定無しだったら
    #このプログラムではargs[1]のfilenameを返している
    if(argc == 2 and args[1][0] != '-'):
        f = args[1]
        return optionlist,f,f1,f2
    
    return optionlist,f,f1,f2


def main(args):
    
    #コマンドライン引数チェック
    #ol:option list
    ol,f,f1,f2 = check(args)
    
    
    if(ol[0] == 1):
        print('p1:',f1) 
    
    if(ol[1] == 1):
        print('p2:',f2)
    
    if(ol[0] == 0 and ol[1] == 0 and f != 0):
        print('f:',f)
    
    
    return print('Finished program')
    
    

if __name__ == '__main__':
    args = sys.argv
    main(args)
