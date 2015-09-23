import io

log = open("/var/log/system76-driver.log", "r")

for line in log:
	temp_val = line.find("kernel")
	if temp_val != -1:
		print line[:temp_val] + line[temp_val:]




