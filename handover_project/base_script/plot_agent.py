import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') 

# 1. Read and process the original data
df = pd.read_csv('HTA_agent_log.csv')
df['learning_step'] = np.arange(len(df))
df["learning_step"] = df["learning_step"] // 20

# 2. Generate the Seaborn plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='learning_step', y='reward')
#plt.ylim(0,1)
#plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.savefig('reward.png', dpi=300)
plt.close() # Closes the figure to free up memory

# 3. Extract and export the aggregated data for TikZ/pgfplots
# We calculate the mean and standard deviation to replicate seaborn's behavior in LaTeX.
tikz_data = df.groupby('learning_step')['reward'].agg(
    reward_mean='mean',
    reward_std='std'
).reset_index()

tikz_data['reward_std'] = tikz_data['reward_std'].fillna(0)

# 1. Get the exact folder where THIS python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Join it with the new filename
csv_filename = os.path.join(script_dir, 'reward_tikz.csv')

# 3. Save it
tikz_data.to_csv(csv_filename, index=False)
