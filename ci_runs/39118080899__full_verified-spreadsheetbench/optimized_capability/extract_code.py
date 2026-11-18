import json
import os
tasks = ['51-12', '267-18', '395-36', '560-12', '50768', '7902', '37456', '43436', '48527', '53647']
for task in tasks:
    print(f'--- Task {task} ---')
    path = f'./trajectories/{task}__cand_0002__t0.json'
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
            trace = data.get('rollout', {}).get('trace', [])
            for turn in trace:
                content = turn.get('content', '')
                if '```python' in content:
                    print(content)
    else:
        print('File not found')
