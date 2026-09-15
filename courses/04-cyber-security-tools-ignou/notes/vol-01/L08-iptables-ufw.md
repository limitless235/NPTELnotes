# L08: Linux Packet Filtering with iptables & UFW

## iptables — purpose

Linux kernel netfilter framework for packet filtering, NAT, and mangling.

## iptables — usage steps

```bash
# View current rules
sudo iptables -L -v -n

# Default deny incoming
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Allow established connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH from lab subnet
sudo iptables -A INPUT -p tcp -s 192.168.56.0/24 --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80,443 -j ACCEPT

# Log then drop everything else
sudo iptables -A INPUT -j LOG --log-prefix "IPTABLES-DROP: "
sudo iptables -A INPUT -j DROP

# Save rules (Debian/Ubuntu)
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

## UFW — simplified frontend

```bash
sudo ufw default deny incoming
sudo ufw allow from 192.168.56.0/24 to any port 22
sudo ufw allow 80,443/tcp
sudo ufw enable
sudo ufw status verbose
```

## Countermeasures

- Automate rule deployment (Ansible, Puppet).
- Never expose management ports to the internet.
- Test with `nmap` after rule changes.
- Monitor `/var/log/kern.log` for DROP entries.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
