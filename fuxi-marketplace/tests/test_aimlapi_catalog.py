import json
import unittest
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1] / "plugins" / "fuxi-plugins"
PLUGIN = ROOT / "external_plugins" / "aimlapi"


class AimlapiCatalogTests(unittest.TestCase):
    def test_catalog_entry_resolves_to_plugin(self):
        catalog = json.loads((ROOT / ".fuxi-plugin/marketplace.json").read_text())
        entries = [entry for entry in catalog["plugins"] if entry["name"] == "aimlapi"]
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual((ROOT / entry["source"]).resolve(), PLUGIN.resolve())
        manifest = json.loads((PLUGIN / ".fuxi-plugin/plugin.json").read_text())
        for field in ("name", "description", "author"):
            self.assertEqual(entry[field], manifest[field])
        self.assertIn("pay-as-you-go", manifest["description"])
        self.assertIn("free", manifest["description"])

    def test_credentials_scoped_to_exact_https_endpoint(self):
        config = json.loads((PLUGIN / ".mcp.json").read_text())
        self.assertEqual(list(config), ["mcpServers"])
        self.assertEqual(list(config["mcpServers"]), ["aimlapi"])
        server = config["mcpServers"]["aimlapi"]
        self.assertEqual(server["type"], "http")
        self.assertEqual(server["url"], "https://mcp.aimlapi.com/mcp")
        self.assertEqual(urlsplit(server["url"]).netloc, "mcp.aimlapi.com")
        self.assertEqual(server["headers"], {"Authorization": "Bearer ${AIMLAPI_API_KEY}"})
        self.assertEqual(set(server), {"type", "url", "headers"})

    def test_documents_opt_in_costs_and_authentication(self):
        readme = (PLUGIN / "README.md").read_text()
        for text in ("opt-in", "OAuth", "AIMLAPI_API_KEY", "embeddings", "tools_run",
                     "account checks are free", "cross-host redirects"):
            self.assertIn(text, readme)


if __name__ == "__main__":
    unittest.main()
