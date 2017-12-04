class FileOwners:

    @staticmethod
    def group_by_owners(files):
          file = {}
          for k in files:
            file[files[k]] = 0
    
          for k in files:
            if file[files[k]] == 0:
      
              file[files[k]] = [k]
      
            elif len(file[files[k]])>=1:
      
              file[files[k]].append(k)
      
          return file   

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))