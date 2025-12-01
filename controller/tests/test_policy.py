from controller.sdn_simulator import SDNSimulator

def test_blocked_by_default():
    sdn = SDNSimulator()
    assert sdn.check_traffic("host1", "host2") == "blocked"

def test_allow_rule():
    sdn = SDNSimulator()
    sdn.apply_policy([
        {"action": "allow", "source": "host1", "destination": "host2"}
    ])
    assert sdn.check_traffic("host1", "host2") == "allowed"

