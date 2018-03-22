# OPUS-Lemmas

This repository is part of an ongoing project to create a frequency list of Hebrew words from OPUS's [OpenSubtitles2018] collection, which is a mega-corpus of cleaned, tokenized, and parsed versions of XML files originally obtained from [opensubtitles.org]. My word list consists of Hebrew lemmas, and is arranged based on a combination of raw frequency, range, and dispersion.

- Latest version of my word list: [HebrewLemmaCount.csv](HebrewLemmaCount.csv)
- Latest version of my main script: [HebrewLemmaCount.py](HebrewLemmaCount.py)


This repo also includes a script to extract information on all movies in the corpus: the IMDB ID, title, year, and original language. The script uses [Derrick Gilland]'s [omdb.py library], which is a Python wrapper around the [OMDb API (Open Movie Database API)]. OMDb is, in turn, is a project that makes use of [IMDb (Internet Movie Database)] for its data.

- Latest versions of my movie lists:
    - [movie-info-to-89.md](movie-info-to-89.md)
    - [movie-info-90s.md](movie-info-90s.md)
- Latest version of my fetch script: [OMDb-fetch.py](OMDb-fetch.py)


[OpenSubtitles2018]: http://opus.nlpl.eu/OpenSubtitles2018.php
[opensubtitles.org]: http://opensubtitles.org
[Derrick Gilland]: https://github.com/dgilland
[omdb.py library]: https://github.com/dgilland/omdb.py
[OMDb API (Open Movie Database API)]: http://omdbapi.com
[IMDb (Internet Movie Database)]: http://www.imdb.com


This is part of my master's thesis at the University of Texas at Austin. More information is forthcoming.
