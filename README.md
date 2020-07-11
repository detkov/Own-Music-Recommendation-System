# Own music recommendation system and singers' embeddings analysis
> <b>The project was completed in September 2019.</b>

I wanted to understand if it is possible to create a good music recommendation system, which would use only the statistics of song lyrics, without using NLP and the sound waves themselves. To do that, I decided to create a simple few layers neural network and find the data to train it.  
Unfortunately, I did not find a suitable dataset, so I collected mine and it was the largest open dataset with a variety of metadata (Sep 2019). Then was decided to open-source it on [kaggle](https://www.kaggle.com/detkov/lyrics-dataset). Also, every related work and analysis will also be there.  

Dataset consists of:
* `songs_dataset.csv` contains 253k+ songs (different genres, decades and so on) with 10 features:  
`|Singer|Album|Song|Date|Featuring|Genre|Lyrics|Tags|Producers|Writers|`;
* `parts_dataset.csv` contains songs with lyrics split into parts (verse, chorus, hook, etc.).  
It's not that obvious due to the dirty (real-world) data.

Currently available notebooks:
* Data analysis and Plotly visualizations can be found [here](https://www.kaggle.com/detkov/starter-music-analysis-and-plotly-tutorial);  
* Creation of the simple dense NN and further exploration of received singers' embeddings can be found [here](https://www.kaggle.com/detkov/music-classification).

<b>UPD: dataset on [kaggle](https://www.kaggle.com/detkov/lyrics-dataset) was deleted, so now you can get it via [Google Drive](https://drive.google.com/drive/folders/10FOIW80rjwTsudtsB8wQhs0q9arn9_gj?usp=sharing).</b>

> Thanks to [Ilya Liyasov](https://github.com/Literman) for helping develop the songs parser.
