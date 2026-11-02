import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts import harvest


class HarvestTests(unittest.TestCase):
    def make_repo(self, root, name, lines):
        repo = (root / name).resolve()
        log = repo / ".roblox-ai-toolbox" / "LEARNINGS.md"
        log.parent.mkdir(parents=True)
        log.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return repo, log

    def template_lines(self):
        template = Path(__file__).resolve().parents[1] / "templates" / "LEARNINGS.md"
        return template.read_text(encoding="utf-8").splitlines()

    def test_template_has_no_entries_or_warnings(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, _ = self.make_repo(Path(tmp), "game", self.template_lines())
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = harvest.main([str(repo)])
            self.assertEqual(result, 0)
            self.assertEqual(stdout.getvalue(), "No unharvested learning entries.\n")
            self.assertEqual(stderr.getvalue(), "")

    def test_ads_entry_after_template_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            template = self.template_lines()
            entry = "- [ads] A launch campaign brought in early players. Evidence: session length and return play were recorded. Status: observed. Added: 2026-10-31. Harvested: no"
            repo, log = self.make_repo(
                Path(tmp), "game", template + [entry]
            )
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = harvest.main([str(repo)])
            self.assertEqual(result, 0)
            self.assertIn(f"[ads]\n{log}:{len(template) + 1}: {entry}", stdout.getvalue())
            self.assertEqual(stderr.getvalue(), "")

    def test_malformed_bullet_outside_fence_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            template = self.template_lines()
            repo, log = self.make_repo(
                Path(tmp), "game", template + ["- [metrics] incomplete"]
            )
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = harvest.main([str(repo)])
            self.assertEqual(result, 0)
            self.assertEqual(stdout.getvalue(), "No unharvested learning entries.\n")
            self.assertIn(
                f"{log}:{len(template) + 1}: malformed learning entry",
                stderr.getvalue(),
            )

    def test_prints_only_unharvested_entries_grouped_by_area(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo, log = self.make_repo(
                root,
                "game",
                [
                    "# Learning log",
                    "- [metrics] A shorter tutorial improved completion. Evidence: completion rose in the weekly cohort. Status: observed. Added: 2026-10-31. Harvested: no",
                    "- [game-design] A clearer goal reduced early exits. Evidence: the next weekly cohort changed. Status: observed. Added: 2026-10-31. Harvested: v0.2.0",
                ],
            )
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = harvest.main([str(repo)])
            output = stdout.getvalue()
            self.assertEqual(result, 0)
            self.assertIn("[metrics]", output)
            self.assertIn(f"{log}:2:", output)
            self.assertIn("Harvested: no", output)
            self.assertNotIn("Harvested: v0.2.0", output)
            self.assertEqual(stderr.getvalue(), "")

    def test_json_output_and_malformed_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, _ = self.make_repo(
                Path(tmp),
                "game",
                [
                    "# Learning log",
                    "- [publishing] A private test caught a missing flag. Evidence: release review found it before publish. Status: observed. Added: 2026-10-31. Harvested: no",
                    "- [unknown] malformed entry",
                ],
            )
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = harvest.main(["--json", str(repo)])
            payload = json.loads(stdout.getvalue())
            self.assertEqual(result, 0)
            self.assertEqual(len(payload["publishing"]), 1)
            self.assertIn(":2", payload["publishing"][0]["source"])
            self.assertIn("malformed learning entry", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
