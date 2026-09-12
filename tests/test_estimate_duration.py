import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "estimate_duration.py"


class EstimateDurationTests(unittest.TestCase):
    def run_json(self, *args: str) -> dict:
        output = subprocess.check_output([sys.executable, str(SCRIPT), *args], text=True)
        return json.loads(output)

    def test_explicit_constraint_math(self) -> None:
        result = self.run_json(
            "--units", "418", "--cpm-min", "120", "--cpm-max", "120",
            "--pause-seconds", "3",
        )
        self.assertEqual(result["speech_seconds"], {"min": 209.0, "max": 209.0})
        self.assertEqual(result["total_seconds"], {"min": 212.0, "max": 212.0})

    def test_text_count_excludes_spacing_and_punctuation(self) -> None:
        result = self.run_json("--text", "你好，AI 2026！")
        self.assertEqual(result["spoken_units"], 8)
        self.assertEqual(result["counting_method"], "unicode_alphanumeric_characters")
        self.assertNotIn("warning", result)

    def test_english_heavy_text_warns_against_chinese_cpm(self) -> None:
        result = self.run_json(
            "--text", "This English sentence needs a separately calibrated speaking rate."
        )
        self.assertIn("Chinese character-per-minute", result["warning"])

    def test_invalid_rate_fails(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--units", "10", "--cpm-min", "300", "--cpm-max", "220"],
            text=True,
            capture_output=True,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("cpm-min cannot exceed cpm-max", completed.stderr)


if __name__ == "__main__":
    unittest.main()
