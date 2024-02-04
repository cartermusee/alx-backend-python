#!/usr/bin/env python3
"""modeule for client"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch("utils.get_json")
    def test_org(self, org_name, expected_url, mock_get_json):
        """Test GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(expected_url)
        self.assertFalse(mock_get_json.called)
