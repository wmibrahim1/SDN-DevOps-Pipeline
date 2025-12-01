# controller/controller.py

import yaml
from sdn_simulator import SDNSimulator

def load_policy(path="policy.yaml"):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data.get("rules", [])

def apply_policy():
    rules = load_policy()
    sdn = SDNSimulator()
    sdn.apply_policy(rules)

    # For demo: print results
    print("Applied rules:")
    for r in rules:
        print(f"{r['action'].upper()}: {r['source']} -> {r['destination']}")

if __name__ == "__main__":
    apply_policy()
