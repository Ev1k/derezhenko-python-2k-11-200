import pytest
from multiprocessing import normalization


@pytest.mark.parametrize("href, expected_result", [
    (normalization("https://http.cat/200.jpg", "http.cat"), "https://http.cat/200.jpg"),
    (normalization("//http.cat/200.jpg", "http.cat"), "https://http.cat/200.jpg"),
    (normalization("/200.jpg", "http.cat"), "https://http.cat/200.jpg")
])
def test_normalization(href, expected_result):
    assert "https://http.cat/200.jpg" == href

