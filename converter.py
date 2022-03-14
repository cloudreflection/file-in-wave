import wave
import sys
def f2w(filename: str):
    f=wave.open(filename+'.wav','wb')
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(48000)
    with open(filename,"rb") as g:
        byte=g.read()
    f.writeframes(byte)
    f.close()
    print('波形写出成功，文件名：'+filename+'.wav')

def w2f(wavename: str):
    f=wave.open(wavename,'rb')
    with open('file_out','wb') as g:
        g.write(f.readframes(f.getnframes()+1))
    f.close()
    print('文件写出成功，文件名：file_out，请自行修改原始名称和后缀名')

if __name__=="__main":
    if len(sys.argv)!=3:
        print('文件wav互转工具 by cloudreflection\nuseage: python converter.py [option]\n   -f <文件名> 将文件转换为wav\n   -w <文件名> 将此工具生成的wav转换回文件')
    elif sys.argv[1]=='-f':
        f2w(sys.argv[2])
    elif sys.argv[1]=='-w':
        w2f(sys.argv[2])
    else:
        print('文件wav互转工具 by cloudreflection\nuseage: python converter.py [option]\n   -f <文件名> 将文件转换为wav\n   -w <文件名> 将此工具生成的wav转换回文件')