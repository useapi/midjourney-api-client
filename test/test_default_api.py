# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest

from midjourney_api_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_account_get(self) -> None:
        """Test case for account_get

        """
        pass

    def test_jobs_blend_post(self) -> None:
        """Test case for jobs_blend_post

        """
        pass

    def test_jobs_button_post(self) -> None:
        """Test case for jobs_button_post

        """
        pass

    def test_jobs_cancel_get(self) -> None:
        """Test case for jobs_cancel_get

        """
        pass

    def test_jobs_describe_post(self) -> None:
        """Test case for jobs_describe_post

        """
        pass

    def test_jobs_get(self) -> None:
        """Test case for jobs_get

        """
        pass

    def test_jobs_get_list(self) -> None:
        """Test case for jobs_get_list

        """
        pass

    def test_jobs_imagine_post(self) -> None:
        """Test case for jobs_imagine_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
