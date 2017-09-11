



try:
    from dp import DP
    from acl import ACL
    from port import Port
    from vlan import VLAN
    from valve_table import ValveTable, ValveGroupTable
except ImportError:
    from faucet.dp import DP
    from faucet.acl import ACL
    from faucet.port import Port
    from faucet.vlan import VLAN
    from faucet.valve_table import ValveTable, ValveGroupTable


class BGPRouteCacheController:
    
    def __init__(self, bgp_cache_valve, bgp_all_valve, logname):
        self.bgp_cache = bgp_cache_valve
        self.bgp_all = bgp_all_valve
        # will probably need to do more things here 
    
    def add_rule_to_precache(self, ip_address, next_hop):
        #TODO: create add flow msg with /24 or /56 and next hop to bgp_all precache
    
    def send_poller_bgp_all_precache(self):
        #TODO: send msg to get rule and counters from bgp_all precache
    
    def poller_return(self, """to be added"""):
        #TODO: loop through rules if count > x add rule to bgp_cache fib
    
    def send_poller_bgp_cache_fib(self):
        #TODO: implement 
    
    
    
    
