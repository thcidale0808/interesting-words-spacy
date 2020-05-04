import pytest
import os

@pytest.fixture()
def document_with_three_sentences(tmpdir):
    
    temp_directory = tmpdir.mkdir("files")
    
    temp_file = temp_directory.join("document.txt")
    
    temp_file.write("London is a fine great city to live.\n It has great restaurants.\n Also it's very safe but London is not a cheap city.")
    
    assert temp_file.read()=="London is a fine great city to live.\n It has great restaurants.\n Also it's very safe but London is not a cheap city."

    yield os.path.join(temp_file.dirname, temp_file.basename)

@pytest.fixture()
def document_with_no_sentences(tmpdir):
    
    temp_directory = tmpdir.mkdir("files")
    
    temp_file = temp_directory.join("document.txt")
    
    temp_file.write("")
    
    assert temp_file.read()==""

    yield os.path.join(temp_file.dirname, temp_file.basename)

@pytest.fixture()
def document_with_dummy_content(tmpdir):
    
    temp_directory = tmpdir.mkdir("files")
    
    temp_file = temp_directory.join("document.txt")
    
    temp_file.write("Philadelfia, Love, Food, see the sea")
    
    assert temp_file.read()=="Philadelfia, Love, Food, see the sea"

    yield os.path.join(temp_file.dirname, temp_file.basename)
