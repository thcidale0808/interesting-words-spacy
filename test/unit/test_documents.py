import pytest
from documents import DocumentWizard
from fixtures.documents import *

def test_interesting_words_with_data(document_with_three_sentences):
    
    document_wizard = DocumentWizard(document_with_three_sentences)
    
    sentences = document_wizard.get_sentences()

    assert len(sentences) == 3

    result = document_wizard.find_interesting_words()
    
    assert result[0]['word'] == "London"

    assert len(result[0]['sentences']) == 2

    assert result[0]['frequency'] == 2

    assert result[1]['word'] == "city"

    assert len(result[1]['sentences']) == 2

    assert result[1]['frequency'] == 2

    assert result[2]['word'] == "restaurants"

    assert len(result[2]['sentences']) == 1

    assert result[2]['frequency'] == 1


def test_interesting_words_with_no_data(document_with_no_sentences):
    
    document_wizard = DocumentWizard(document_with_no_sentences)
    
    sentences = document_wizard.get_sentences()

    assert len(sentences) == 0

    result = document_wizard.find_interesting_words()

    assert result == []

def test_interesting_words_with_dummy_data(document_with_dummy_content):
    
    document_wizard = DocumentWizard(document_with_dummy_content)
    
    sentences = document_wizard.get_sentences()

    assert len(sentences) == 1

    result = document_wizard.find_interesting_words() 

    assert len(result) == 4
