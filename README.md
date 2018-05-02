# Frequency Dictionary and Scripts

This repository houses all the scripts and files used to create the *Frequency Dictionary of Spoken Hebrew* (FDOSH), along with the dictionary itself. This project was created as part of my MA thesis at the University of Texas at Austin in 2018. The thesis itself describes the creation process—and the use of each script—in depth, and can be found in the [University of Texas thesis repository](https://repositories.lib.utexas.edu/handle/2152/11). A GitHub repository for the thesis manuscript can also be found at <https://github.com/juandpinto/thesis-manuscript>.

The scripts make use of OPUS's [OpenSubtitles2018](http://opus.nlpl.eu/OpenSubtitles2018.php) collection, which is a mega-corpus of cleaned, tokenized, and parsed versions of XML files originally obtained from [opensubtitles.org](http://opensubtitles.org). The final frequency dictionary consists of Hebrew lemmas, and is arranged based on a usage coefficient of Gries' (2008) deviation of proportions, or *U~DP~*. It also includes frequency and range measures for each entry.

The most important files in this repository are listed below.

- The *Frequency Dictionary of Spoken Hebrew* (FDOSH): [export/frequency-dictionary.tsv](export/frequency-dictionary.tsv)
- The main script used for creating the dictionary: [create-freq-list.py](create-freq-list.py)
- The script used to clean the OpenSubtitles2018 corpus: [single_file_extract.py](single_file_extract.py)
- The script used to fetch movie metadata for each subtitle file in the corpus: [OMDb-fetch.py](OMDb-fetch.py)
- The script used to find the shared entries in two different frequency lists: [list_comparison.py](list_comparison.py)

The script used to fetch movie metadata ([OMDb-fetch.py](OMDb-fetch.py)) uses [Derrick Gilland](https://github.com/dgilland)'s [omdb.py library](https://github.com/dgilland/omdb.py), which is a Python wrapper around the [OMDb API (Open Movie Database API)](http://omdbapi.com). OMDb is, in turn, a project that makes use of [IMDb (Internet Movie Database)](http://www.imdb.com) for its data. For each subtitle file in the corpus, the script finds the IMDB ID, title, year, and original language(s). The [movies-info](movies-info/) folder contains extensive lists of the metadata found for the movies used to create the FDOSH.

Each script includes detailed notes within the comments to allow them to be clear and easily customizable. This project is licensed under the [MIT License](LICENSE), so feel free to clone and use as you see fit. Suggestions and pull requests are also welcome.
