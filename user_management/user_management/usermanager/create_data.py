import mmap 
import json 

with open('userapp.txt','wb') as userapp_file:
    userapp_file.write(json.dumps(str({"id":"user1","roles":["role1","role3"]})))


