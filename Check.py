import os,subprocess
import pandas as pd
from PyPDF2 import PdfFileReader
import mimetypes

exe = "hachoir-metadata"
output_df = pd.DataFrame()
list1=[]
for root, dirs, files in os.walk(r'C:\Users\user\Desktop\PythonAssignment\Data'):
    for name in files:
        a=r'C:\Users\user\Desktop\PythonAssignment\Data\{}'.format(name)
        print("FileName\n",a)
        print("Mimetype \n",mimetypes.guess_type(name))
        if a.endswith(r'.pdf'):
            with open(a, 'rb') as f:
                pdf = PdfFileReader(f)
                info = pdf.getDocumentInfo()
                print("Meta Data Details \n",info)
        else:
            process = subprocess.Popen([exe, a], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
            for output in process.stdout:
                print("Meta Data Details",output.strip())



        # b'- Image DPI width: 72 DPI\r\n' --> Lines are start with b and ends with \r\n
        #for removing that universal_newlines=True
        #strip(0) is used for the unwanted spaces between output
        

