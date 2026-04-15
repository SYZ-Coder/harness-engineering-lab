import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ServiceCatalogDemoTests(unittest.TestCase):
    def setUp(self):
        self.catalog_text = (ROOT / "catalog-info.yaml").read_text(encoding="utf-8")
        self.service_text = (ROOT / "service.yaml").read_text(encoding="utf-8")
        self.dependencies_text = (
            ROOT / "dependencies" / "services.yaml"
        ).read_text(encoding="utf-8")

    def test_catalog_and_service_name_match(self):
        self.assertIn("name: order-query-service", self.catalog_text)
        self.assertIn("name: order-query-service", self.service_text)

    def test_owner_and_system_exist(self):
        self.assertIn("owner: team-order-platform", self.catalog_text)
        self.assertIn("system: commerce-platform", self.catalog_text)
        self.assertIn("team: team-order-platform", self.service_text)
        self.assertIn("system: commerce-platform", self.service_text)
        self.assertIn("lifecycle: production", self.catalog_text)
        self.assertIn("lifecycle: production", self.service_text)

    def test_api_and_dependencies_are_declared(self):
        self.assertIn("providesApis:", self.catalog_text)
        self.assertIn("- order-query-api", self.catalog_text)
        self.assertIn("id: order-query-api", self.service_text)
        self.assertIn("path: apis/openapi-order-query.yaml", self.service_text)
        self.assertIn("name: customer-service", self.dependencies_text)
        self.assertIn("name: inventory-service", self.dependencies_text)
