import pandas as pd
import os
import random

# === Ayarlar ===
input_csv = "val.csv"   # senin CSV dosyan
output_dir = "split_groups"
os.makedirs(output_dir, exist_ok=True)

# === CSV oku ===
df = pd.read_csv(input_csv)

# === 5 grup oluştur ===
groups = {i: [] for i in range(5)}  # group_0 ... group_4

# === 5'erli blokları sırayla işle ===
for i in range(0, len(df), 5):
    block = df.iloc[i:i+5]
    indices = list(range(len(block)))
    random.shuffle(indices)
    for j, idx in enumerate(indices):
        groups[j].append(block.iloc[idx])

# === Grupları kaydet ===
for g_idx, rows in groups.items():
    group_df = pd.DataFrame(rows)
    out_path = os.path.join(output_dir, f"group_{g_idx+1}.csv")
    group_df.to_csv(out_path, index=False)
    print(f"✅ Saved {out_path} ({len(group_df)} rows)")

print("\nAll done! 5 balanced random groups created 🎯")