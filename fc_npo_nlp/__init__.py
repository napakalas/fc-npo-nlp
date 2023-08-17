from npoexplorer import SPARQLConnection, NPOExplorer
from npoexplorer import ENDPOINT_BLAZEGRAPH, ENDPOINT_STARDOG


def create_nlp_embeddings():

    npo = NPOExplorer(ENDPOINT_BLAZEGRAPH)
    neurons_nlp = [n['id'] for n in npo.entity_knowledge('ilxtr:NeuronSparcNlp')['paths']]
    for neuron in neurons_nlp:
        knowledge = npo.entity_knowledge(neuron)
        print(knowledge)
    npo.close()