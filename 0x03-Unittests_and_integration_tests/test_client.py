#!/usr/bin/env python3
"""modeule for client"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch("utils.get_json")
    def test_org(self, org_name: str, expected_url: Dict, mock_get_json: MagicMock) -> None:
        """Test GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(expected_url)
        self.assertFalse(mock_get_json.called)
