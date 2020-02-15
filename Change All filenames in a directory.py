import os
path = 'C:\\Users\\Username\\Desktop\\dataset_train'

i = 0
for filename in os.listdir(path):
    yeniname = 'eng.special.exp'+str(i)+'.JPG'
    old_file = os.path.join(path,filename)
    new_file = os.path.join(path,yeniname)
    os.rename(old_file, new_file)
    i +=1

print ("Successfully renamed.")


