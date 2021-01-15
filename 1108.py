def defangIpaddr(address: str) -> str:
    lst = address
    ret = ""
    for i in lst:
        if(i != "."):
            ret += i
        else:
            ret += "[.]"
    return ret

print(defangIpaddr("255.100.50.0"))
