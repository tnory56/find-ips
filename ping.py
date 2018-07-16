# Import modules
import subprocess
import ipaddress

# Prompt the user to input a network address
net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24)(might need to add u in front of ip address): ")

# Create the network
ip_net = ipaddress.ip_network(net_addr)

# Get all hosts on that network
all_hosts = list(ip_net.hosts())

# Configure subprocess to hide the console window
#info = subprocess.STARTUPINFO()
#info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#info.wShowWindow = subprocess.SW_HIDE

online=0
# For each IP address in the subnet, 
# run the ping command with subprocess.popen interface
for i in range(len(all_hosts)):
    output = subprocess.Popen(['ping', str(all_hosts[i]), '-c', '1', '-W', '2'],stdout=subprocess.PIPE).communicate()[0]
   
#    print output.decode('utf-8')
    if "Destination host unreachable" in output.decode('utf-8'):
        print str(all_hosts[i]), "is Offline"
    elif "Request timed out" in output.decode('utf-8'):
        print str(all_hosts[i]), "is Offline"
    elif "100% packet loss" in output.decode('utf-8'):
        print str(all_hosts[i]), "is Offline"
    elif "0% packet loss" in output.decode('utf-8'):
#        print output.decode('utf-8')
        online =online+1
        print str(all_hosts[i]), "is Online"
    else:
        print "Cannot determine information"

print "Hosts online: " + str(online)
