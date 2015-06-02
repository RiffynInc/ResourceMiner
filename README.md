# ResourceMiner

[![Join the chat at https://gitter.im/RiffynInc/ResourceMiner](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/RiffynInc/ResourceMiner?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Getting started

1. Look through the [issues](https://github.com/RiffynInc/ResourceMiner/issues) here in the GitHub repo and the [wiki](https://github.com/RiffynInc/ResourceMiner/wiki).
2. Check out these [useful resources](https://github.com/RiffynInc/ResourceMiner/wiki/Useful-Resources)
3. Fork the repo and start coding!

See also the [details](#details) section. Papers can be accessed through our MongoDB server: `mongodb://mozsprint:plos@ec2-52-26-49-156.us-west-2.compute.amazonaws.com/plos`.

### About Riffyn

Billions of dollars are lost each year on material and life science research with 10% reproducibility rates, and multi-million dollar failures during process transfer to manufacturing. Riffyn addresses this problem with a cloud-based operating system for laboratory R&D processes that combines computer-aided design of structured protocols including controlled vocabularies, real-time data acquisition, and automated statistical quality analytics.

### Details

We would like to develop a natural language processing toolkit for extracting controlled vocabularies (ontologies) of research resources used in the scientific literature, and organizing them into an associative knowledge graph. The tool will report on the frequency and context of use of terms that are fed to it from Riffyn’s (or any) ontology of research resources.

To build the knowledge graph, the tool will annotate the ontology terms with keywords and subject area tags obtained from article annotations in PLOS and other journals. If time permits, the tool may also be extended to extract additional ontology terms from journal articles using a predictive algorithm. The tag information could also be engineered to flow in the reverse direction (from the ontology to the journal) to suggest tags for articles, analogous to when LinkedIn suggests skills of a person for you to endorse.

The toolkit will be developed via two subprojects (deliverables) below.

### Deliverables

1. A Python package to calculate usage statistics in PLOS articles of a given list of terms. For our test case, we will have two products:
    * a report of usage statistics for Riffyn’s 50,000+ resource term set
    * a JSON file associating PLOS subject area tags and terms from Riffyn's ontology

2. A predictive model for resource terms in a research paper. Train a model to identify additional terms to add to the term set. Train on the PLoS library using Riffyn’s ontologies. The goal is to identify additional terms to incorporate.

### Structure

* `config` -- configuration files
* `data/papers` -- plaintext paper content
* `data/terms` -- term lists
* `docs` -- further documentation
* `src` -- code
* `test` -- reference files for testing

### Getting started

1. Check out the issues here in the GitHub repo
2. Check out these [useful resources](https://github.com/RiffynInc/ResourceMiner/wiki/Useful-Resources)
