from plone_vercel_test import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if plone_vercel_test is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IPloneVercelTestLayer is registered."""
        from plone_vercel_test.interfaces import IPloneVercelTestLayer

        assert IPloneVercelTestLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240522001"
