


#package and dataset impportation
from streamroot_global_visualization_true import consumer_data_content_true
dataframe = consumer_data_content_true.ix[: , 'stream_id' : ]

import matplotlib.pyplot as plt

#setting the streaming identification
list_stream_ids = list(dataframe['stream_id'])
fig = plt.figure()
fig.suptitle('p2p and cdn data per streaming_content')
k = 0
div_stock0 = []
div_stock1 = []

#plotting of the amount of p2p and cdn data regarding the streaming identification
for stream_id in list_stream_ids:
    k = k + 1
    #dataset with streaming identification = stream_id
    current_dataframe = dataframe[dataframe['stream_id'] == stream_id]
    division =[float(current_dataframe['%p2p'] ), float(current_dataframe['%cdn'])] 
    activites = ['p2p' , 'cdn']
    couleurs = ['lightgreen','lightblue']
    fig.set_size_inches(12.5, 7.5)
    plt.subplot(3,3,k)
    line1 = plt.pie(division , labels=activites, colors=couleurs, startangle=90, autopct='%1.1f%%')
    plt.title('stream_id : ' +  str(stream_id))

plt.show()
