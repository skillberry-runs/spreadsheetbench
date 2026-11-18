import json
import os
import glob

def get_feedback(task_id):
    path = f'./trajectories/{task_id}__seed__t0.json'
    if not os.path.exists(path): return None
    with open(path) as f:
        d = json.load(f)
    return d['score']['feedback']

# Get all trajectories
files = glob.glob('./trajectories/*.json')
task_ids = [f.split('__')[0].split('/')[-1] for f in files]

# Separate based on reward
results = []
for tid in task_ids:
    path = f'./trajectories/{tid}__seed__t0.json'
    with open(path) as f:
        d = json.load(f)
    reward = d['score'].get('reward', 0)
    feedback = d['score'].get('feedback', '')
    results.append({'id': tid, 'reward': reward, 'feedback': feedback})

# Filter failing
failing = [r for r in results if r['reward'] < 1.0]

print(f"Total tasks analyzed: {len(task_ids)}")
print(f"Failing tasks: {len(failing)}")
print("\n--- Detailed Feedbacks ---")
for r in failing:
    print(f"Task {r['id']} (Reward {r['reward']}): {r['feedback']}")

