#!/usr/bin/env python3
"""Remove state entries for summaries that no longer exist, so they get regenerated."""

import json
import os

state_path = os.path.join(os.path.dirname(__file__), "summaries/.summary-state.json")
summaries_dir = os.path.join(os.path.dirname(__file__), "summaries/")

with open(state_path) as f:
    state = json.load(f)

existing = set(os.listdir(summaries_dir))
missing = [k for k in state if k not in existing]

if not missing:
    print("Nothing to reset — all state entries have corresponding summary files.")
else:
    for k in missing:
        del state[k]
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)
    print(f"Reset {len(missing)} entries:")
    for k in sorted(missing):
        print(f"  {k}")
