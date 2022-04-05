def construct_inventory_file(inventoryFile, targets):
    targetList = []
    with open(inventoryFile, "w") as f:
        f.write("[MiddlewareServers]\n")
        for target in targets:
            serverInventory = "%s\n" % target
            f.write(serverInventory)
            targetList.append(serverInventory)
        execution.setVariable('targetList', targetList)
        f.write("\n")
        f.write("[MiddlewareServers:vars]\n")
        f.write("ansible_connecton=ssh\n")
        f.write("scp_if_ssh = True")

def print_from_inventory_file(inventoryFile):
    with open(inventoryFile, "r") as file:
        data = file.read()
    return data

if __name__ in [ "__main__", "__builtin__" ]:
    print("Executing transformer.py")
    construct_inventory_file(inventoryFile, targets)
    data = print_from_inventory_file(inventoryFile)
    print(data)