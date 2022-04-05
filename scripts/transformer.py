def construct_inventory_file(inventoryFile, servers):
    targetServers = []
    with open(inventoryFile, "w") as file:
        file.write("[MiddlewareServers]\n")
        for server in targetServers:
            serverInventory = "%s\n" % server
            file.write(serverInventory)
            targetServers.append(serverInventory)
        execution.setVariable('targetServers', targetServers)
        file.write("\n")
        file.write("[MiddlewareServers:vars]\n")
        file.write("ansible_connecton=ssh\n")

def print_from_inventory_file(inventoryFile):
    with open(inventoryFile, "r") as file:
        data = file.read()
    return data

if __name__ in [ "__main__" ]:
    construct_inventory_file(inventoryFile, servers)
    data = print_from_inventory_file(inventoryFile)
    print(data)