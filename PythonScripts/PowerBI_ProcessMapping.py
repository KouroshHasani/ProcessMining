import pandas as pd
import pm4py

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.discovery.alpha import variants
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from src import DATA_DIR

event_log = pm4py.format_dataframe(
    log_csv,
    case_id = 'case_id',
    activity_key = 'activity',
    timestamp_key = 'timestamp', 
    timest_format = '%Y-%m-%d %H:%M:%S%z'
)

pm4py.write_xes(event_log, DATA_DIR / 'running-example.xes')

log = pm4py.read_xes(str(DATA_DIR / 'running-example.xes'))

# Miner
petri_net, initial_marking, final_marking = alpha_miner.apply(log, variant=variants.classic)

# GraphViz
gviz = pn_visualizer.apply(petri_net, initial_marking, final_marking)

# Save
pn_visualizer.save(gviz, 'alpha_miner_classic_petri_default.png')

# View
img = mpimg.imread('alpha_miner_classic_petri_default.png')
imgplot = plt.imshow(img)
plt.show()