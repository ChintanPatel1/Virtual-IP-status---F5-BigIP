# Virtual-IP-status---F5-BigIP

The script will take an input file and fetch the Virtual IPs and its member servers with individual status and generate two text files - "VIP_status.txt" and "VIP_statusUP.txt"
Input file should be a text file containing the output of the command "b virtual show" from the load blancer.
VIP_status.txt will have the list of all the F5 Virtual IPs and its corrosponding member server status.
VIP_status.txt will have the list of all the Virtual IPs that are UP on the F5 load balancer.
