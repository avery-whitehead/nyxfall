import argparse
from unittest.mock import patch
from pytest import CaptureFixture
from nyxfall.__main__ import run_cli


def test_cli_require_query_or_random(capfd: CaptureFixture[str]):
    args = argparse.Namespace(query=None, random=None)
    run_cli(args)
    assert (
        capfd.readouterr().out
        == "You must either supply a query or use the --random flag\n"
    )


def test_cli_search_random():
    with patch("nyxfall.__main__.search_random") as search_random:
        args = argparse.Namespace(query=None, random=True, ascii=False)
        run_cli(args)
        search_random.assert_called_once()


def test_cli_search_exact():
    with patch("nyxfall.__main__.search_exact") as search_exact:
        args = argparse.Namespace(
            query="Lightning Bolt", random=None, exact=True, ascii=False
        )
        run_cli(args)
        search_exact.assert_called_once_with("Lightning Bolt")
