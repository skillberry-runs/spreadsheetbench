import json
with open('./trajectories/48620__cand_0002__t0.json') as f:
    data = json.load(f)
    for turn in data['rollout']['trace']:
        if turn['role'] == 'assistant' and '```python' in turn['content']:
            lines = turn['content'].split('\n')
            for i, line in enumerate(lines):
                print(f'{i}: {line}')
