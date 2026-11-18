import json
with open('./trajectories/48620__cand_0002__t0.json') as f:
    data = json.load(f)
    for turn in data['rollout']['trace']:
        if turn['role'] == 'assistant' and '```python' in turn['content']:
            with open('code_48620.txt', 'w') as out:
                out.write(turn['content'])
