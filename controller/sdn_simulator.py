# controller/sdn_simulator.py

class SDNSimulator:
    def __init__(self):
        # store rules in memory for demo
        self.rules = []

    def apply_policy(self, rules):
        """
        rules: list of dicts like {'action': 'allow', 'source': 'host1', 'destination': 'host2'}
        """
        self.rules = rules

    def check_traffic(self, source, destination):
        """
        Returns 'allowed' or 'blocked' based on current rules
        """
        for rule in self.rules:
            if rule["source"] == source and rule["destination"] == destination:
                return "allowed" if rule["action"] == "allow" else "blocked"
        # default deny
        return "blocked"
