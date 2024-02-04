#!/usr/bin/env python3
"""modeule for client"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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
    def test_org(self, org_name: str,
                 expected_url: Dict,
                 mock_get_json: MagicMock) -> None:
        """Test GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(expected_url)
        self.assertFalse(mock_get_json.called)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org) -> None:
        """Test GithubOrgClient._public_repos_url."""
        expected_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        mock_org.return_value = expected_payload
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, expected_payload["repos_url"])