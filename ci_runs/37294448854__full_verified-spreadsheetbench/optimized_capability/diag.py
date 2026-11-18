import json, os
traj_dir = './trajectories'
tasks = ['80-42', '395-36', '227-40', '560-12']
for task in tasks:
    files = [f for f in os.listdir(traj_dir) if f.startswith(task)]
    if not files: continue
    with open(os.path.join(traj_dir, files[0])) as f:
        data = json.load(f)
        print(f'--- Task {task} ---')
        print(f'Score Feedback: {data.get("score", {}).get("feedback", "N/A")}')
        trace = data.get('rollout', {}).get('trace', [])
        for turn in trace:
            if turn['role'] == 'assistant' and '```python' in turn['content']:
                print('Assistant Plan/Code:')
                print(turn['content'][:1000])
                break
        print('\n')
