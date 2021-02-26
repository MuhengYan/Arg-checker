# Arg-checker

A tool for checking the inferred argument components in fake news articles.

The data is sampled from the full collection based on the 2(credible/not) x 4(topic cluster) grids.

From each grid, the 5 articles with the highest proportion of each type of argument components (assumption, anecdote, testimony, statistic, common-ground) are included. In total there are 5 x 5 x 8 = 200 articles in the sampled data.

The data is provided in a csv format, with the following columns:

- credible: whether the article is from a credible source
- topic_cluster: the major topic cluster 
- topic: the topic (15 topics in total) of the article
- sample_reason: the argument component type why an article is taken (have highest proportion among articles, but may not be the dominant argument component type within the article)
- text: text of the article
- tags: inferred argument component tags, each correspond to one token in the "text" field
- url: url of the article

To visualize the tags and the texts together, check the codes in the notebook
