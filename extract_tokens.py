import json

INPUT_FILE = "token.json"
OUTPUT_FILE = "tokens.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

tokens = []

# 遍历所有顶层 key（如 ssoBasic 等），提取每个条目里的 token
for key, entries in data.items():
    if isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, dict) and "token" in entry:
                tokens.append(entry["token"])

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(tokens) + "\n")

print(f"共提取 {len(tokens)} 个 token，已写入 {OUTPUT_FILE}")
