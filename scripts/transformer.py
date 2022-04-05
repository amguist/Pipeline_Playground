def construct_inventory_file(inventoryFile, targets):
    targetList = []
    with open(inventoryFile, "w") as file:
        file.write("[MiddlewareServers]\n")
        for target in targets:
            serverInventory = "%s\n" % target
            file.write(serverInventory)
            targetServers.append(serverInventory)
        execution.setVariable('targetList', targetList)
        file.write("\n")
        file.write("[MiddlewareServers:vars]\n")
        file.write("ansible_connecton=ssh\n")

def print_from_inventory_file(inventoryFile):
    with open(inventoryFile, "r") as file:
        data = file.read()
    return data

if __name__ in [ "__main__" ]:
    construct_inventory_file(inventoryFile, targets)
    data = print_from_inventory_file(inventoryFile)
    print(data)