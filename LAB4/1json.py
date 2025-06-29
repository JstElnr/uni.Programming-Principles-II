import json
with open("sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    desc = attributes.get("descr", " ")
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {desc:<20} {speed:<10} {mtu:<10}")

