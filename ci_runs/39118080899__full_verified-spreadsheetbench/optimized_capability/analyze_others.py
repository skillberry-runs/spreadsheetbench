import json
import os

def analyze(task_id):
    path = f'./trajectories/{task_id}__seed__t0.json'
    if not os.path.exists(path):
        print(f"File {path} not found")
        return
    with open(path) as f:
        d = json.load(f)
    print(f"--- Task {task_id} ---")
    print("Feedback:", d['score']['feedback'])
    for msg in d['rollout']['trace']:
        if msg.get('role') == 'assistant' and '```python' in msg.get('content', ''):
            print("Python Code:")
            print(msg.get('content'))
    print("------------------")

tasks = ["227-40", "267-18", "38462", "39046", "43436", "463-17"]
for t in tasks:
    analyze(t)
