import img2pdf
import os

# multiple inputs (variant 2)
def Converttopdf(pdfname,imagefiles):
    if os.path.exists(pdfname) == True:
        os.remove(pdfname)
    with open(pdfname,"wb") as f:
        f.write(img2pdf.convert(imagefiles))
def start():
    # 打开文件
    path = r'.'

    for root, dirs, files in os.walk(path, topdown=False):
        rootpath = root
        pdfname =os.path.join(rootpath,str(rootpath.split('\\')[-1]) +'.pdf')
        print(rootpath)
        pages = []
        bool =False
        for f in os.listdir(rootpath):
            suffix = str(os.path.splitext(f)[-1][1:]).lower()
            if suffix =='jpg':
                pages.append(os.path.join(rootpath, f))
                bool =True
        if bool ==True:
            Converttopdf(pdfname,pages)
if __name__=='__main__':
    start()