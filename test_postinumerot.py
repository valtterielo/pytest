import postinumerot

#Tuloksia ei löydy
def test_none_found():
    #listan alustus tyhjäksi
    postinumerot.results = []
    postinumerot.etsi_postinumerot("Oslo", postinumerot.postinumerolista)
    assert len(postinumerot.results) == 0
    
test_none_found()

#Tuloksia löytyy 1 kpl
def test_one_found():
    #listan alustus tyhjäksi
    postinumerot.results = []
    postinumerot.etsi_postinumerot("Tainus", postinumerot.postinumerolista)
    assert len(postinumerot.results) == 1

test_one_found()

#Tuloksia löytyy useampi
def test_multiple_found():
    #listan alustus tyhjäksi
    postinumerot.results = []
    postinumerot.etsi_postinumerot("Helsinki", postinumerot.postinumerolista)
    assert len(postinumerot.results) >= 1

test_multiple_found()
