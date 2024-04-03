from queue import deque

def ls_R(file_path):
        list_of_files = []
        cur_listing = dbutils.fs.ls(file_path)

        # if nothing specified, do nothing
        if not file_path: return list_of_files

        # if path is a single file 
        if len(cur_listing) == 1 and cur_listing[0].isFile():
          list_of_files.append(file_path)
          return list_of_files
        
        file_path = file_path if file_path.endswith("/") else file_path + "/"

        directories = deque([file_path])
        while directories:
            cur_dir = directories.pop()
            files = [f.name for f in dbutils.fs.ls(cur_dir)]
            for f in files:  
                if (f.endswith('/')):
                    directories.appendleft(cur_dir+f)
                else:  
                   list_of_files.append(cur_dir+f)
        return list_of_files

# example
#  path = "dbfs:/FileStore/diabetes_lr.model"
#  ls_R(path)
