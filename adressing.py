import ipaddress


address = input("Enter an address : ")


# tady byla ta chyba musel jsem nastavit parametr strict na false, abych tam mohl data host bits
ip = ipaddress.ip_network(address, strict=False)

print(f"Network address : {ip.network_address}")
print(f"Mask : {ip.netmask}")
print(f"Broadcast : {ip.broadcast_address}")
print(f"Number of addresses : {ip.num_addresses}")
print(f"Number of hosts : {ip.num_addresses - 2}")
