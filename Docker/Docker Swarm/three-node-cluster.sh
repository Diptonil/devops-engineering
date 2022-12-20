# The VMs are called as vm1, vm2 and vm3
# The leader VM is vm1 while vm2 and vm3 are both manager VMs

# vm1
docker swarm init --advertise-addr <publicip>

# vm2
docker swarm join --token <tokenvalue>

# vm3
docker swarm join --token <tokenvalue>

# vm1
docker node ls
docker node update --role manager node2
docker node update --role manager node3
docker node ls
docker service craete --replicas 3 alpine ping 8.8.8.8
docker service ls
docker node ps
