import os
def delete_in_out():
    for root,dirs,files in os.walk("./"):
        for file in files:
            if file == "test.out" or file == "test.inp":
                os.remove(os.path.abspath(root+"\\"+file))

delete_in_out()