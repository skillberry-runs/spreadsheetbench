import json
with open('./trajectories/416-15__seed__t0.json') as f:
    d = json.load(f)
for msg in d['rollout']['trace']:
    if msg.get('role') == 'assistant' and '```python' in msg.get('content', ''):
        print(msg.get('content'))
