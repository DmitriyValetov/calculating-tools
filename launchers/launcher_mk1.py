import subprocess, time
import os


def check_proc(proc_list, instance):
    if (len(proc_list) > 0):
        temp = proc_list
        # look for any terminated processes
        for i, proc in enumerate(temp):
            if (proc.poll() is not None): 
                proc_list.remove(proc)
                instance[0]-=1
    


print("Start...\n")


target_exe = "app.exe"
params = ""
launch_string1 ="START \"" + target_exe + "\" /WAIT /BELOWNORMAL \""
proc_list = []


temp = os.listdir()
dirs = []
root = os.getcwd()
#print(root)
for dir in temp:
    if os.path.isdir(os.path.join(root, dir)):
        dirs.append(os.path.join(root, dir))

    
cmd_list = []
for dir in dirs:
    launch_string2 = launch_string1+os.path.join(dir,str(target_exe)) + " \"" + " " + params  # + "> log.txt"
    cmd_list.append(launch_string2)

#print (cmd_list)

"""

proc1 = subprocess.Popen(proc_name+ " " + str(10), shell=True)
proc2 = subprocess.Popen(proc_name+ " " + str(50), shell=True)
proc3 = subprocess.Popen(proc_name+ " " + str(100), shell=True)
proc_list=[proc1, proc2, proc3]

"""

instance = [0]
instance_max = 3
number = 0
total_amount = len(cmd_list)

while len(cmd_list):

    if instance[0] < instance_max:
    
        for i, cmd in enumerate(cmd_list):
            number+=1
            print("calc {}/{}".format(number,total_amount))
            print(cmd+"\n\n")
            os.chdir(dirs[i]) # even the app can miss it's support files
            proc_list.append(subprocess.Popen(cmd, shell=True))
            instance[0]+=1
            cmd_list.remove(cmd)
            
            if instance[0] >= instance_max:
                break
                
    check_proc(proc_list, instance)
    time.sleep(1)
    
# wait for the last of them
while len(proc_list):
    check_proc(proc_list, instance)
    time.sleep(1)


print("End...")

shut_down = False
if shut_down:
    subprocess.call(["shutdown.exe", "/t", str(10)]) 
