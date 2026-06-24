import unittest

from restaurant_ops_toolkit.channels import apply_channel_rules
from restaurant_ops_toolkit.metrics import compare_periods, summarize_records


class MetricsTests(unittest.TestCase):
    def test_summary_and_reconciliation(self):
        records = [
            {
                "store_id": "S001",
                "revenue": 1000,
                "dine_in": 700,
                "delivery": 250,
                "takeaway": 50,
                "orders": 20,
                "channel_group_buy": 300,
                "channel_member": 200,
                "channel_offline": 500,
            }
        ]
        result = summarize_records(records)
        self.assertEqual(result["store_count"], 1)
        self.assertEqual(result["average_ticket"], 50)
        self.assertTrue(result["service_types"]["closed"])
        self.assertTrue(result["channels"]["closed"])

    def test_comparison(self):
        current = [{"store_id": "S001", "revenue": 120, "orders": 12}]
        previous = [{"store_id": "S001", "revenue": 100, "orders": 10}]
        result = compare_periods(current, previous)
        self.assertEqual(result["comparison"]["revenue"]["change_rate"], 0.2)
        self.assertEqual(result["comparison"]["average_ticket"]["change_rate"], 0.0)

    def test_configurable_channel_rules(self):
        rules = {
            "metric_basis": "revenue",
            "residual_channel": "channel_offline",
            "channels": {
                "channel_group_buy": ["payment_group_buy"],
                "channel_member": ["payment_member"],
            },
        }
        rows, audit = apply_channel_rules(
            [
                {
                    "store_id": "S001",
                    "revenue": 1000,
                    "payment_group_buy": 300,
                    "payment_member": 200,
                }
            ],
            rules,
        )
        self.assertEqual(rows[0]["channel_group_buy"], 300)
        self.assertEqual(rows[0]["channel_member"], 200)
        self.assertEqual(rows[0]["channel_offline"], 500)
        self.assertEqual(audit["missing_fields"], [])

    def test_missing_channel_field_is_audited(self):
        rules = {
            "metric_basis": "revenue",
            "residual_channel": "channel_offline",
            "channels": {
                "channel_group_buy": ["payment_missing"],
            },
        }
        rows, audit = apply_channel_rules([{"revenue": 100}], rules)
        self.assertEqual(rows[0]["channel_offline"], 100)
        self.assertEqual(audit["missing_fields"], ["payment_missing"])


if __name__ == "__main__":
    unittest.main()
