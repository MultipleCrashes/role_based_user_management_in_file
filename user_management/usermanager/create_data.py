import mmap 
import json 

with open('userapp.txt','wb') as userapp_file:
    #user
    userapp_file.write(json.dumps(str({"id":"user1","roles":["role1","role3"]})))
    userapp_file.write("\n")
    #roles
    userapp_file.write(json.dumps(str({"id":"role1","permissions":["perm1","perm5"]})))
    userapp_file.write("\n")
    userapp_file.write(json.dumps(str({"id":"role3","permissions":["perm6","perm7"]})))
    userapp_file.write("\n")
    #permissions
    userapp_file.write(json.dumps(str({"id":"perm1","name":"Can check balance"})))
    userapp_file.write("\n")
    userapp_file.write(json.dumps(str({"id":"perm5","name":"Can deposit"})))
    userapp_file.write("\n")
    userapp_file.write(json.dumps(str({"id":"perm6","name":"Can Transfer"})))
    userapp_file.write("\n")
    userapp_file.write(json.dumps(str({"id":"perm7","name":"Can withdraw"})))

