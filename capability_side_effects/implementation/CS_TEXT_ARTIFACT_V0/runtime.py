"""
runtime.py — Execution-only host for CS_TEXT_ARTIFACT_V0.

Responsibilities:
- Persist rendered protocol artifacts as text documents beneath a policy-declared root
- Translate backend errors into CEP-visible result_status values

The root is policy, never an input. A caller that named its own destination could write anywhere the
process can reach, and where generated artifacts land is a governance decision belonging to the
runtime binding rather than to whoever dispatched the workflow.
"""

from pathlib import Path
from typing import Any, Dict, Set


class TextArtifactRuntime:
    """Execution-only host for CS_TEXT_ARTIFACT_V0."""

    capability_kind = "CS"
    _default_capability_code = "CS_TEXT_ARTIFACT_V0"

    def __init__(self, config: Dict[str, Any], metadata: Dict[str, Any],
                 capability_code: str | None = None):
        self._metadata = dict(metadata)
        assert isinstance(self._metadata, dict), "metadata must be dict"
        assert "capability" in self._metadata, "metadata must contain 'capability'"

        root = (config or {}).get("root")
        if not root:
            raise ValueError("CS_TEXT_ARTIFACT_V0 requires a policy 'root'")
        self._root = Path(root)
        self._capability_code = capability_code or self._default_capability_code
        self._supported_operation_specs: Set[str] = set(
            self._metadata["capability"].get("supported_operation_specs", [])
        )

    @property
    def capability_code(self) -> str:
        return self._capability_code

    @property
    def supported_operation_specs(self) -> Set[str]:
        return self._supported_operation_specs

    def execute(self, *, op: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            handler = getattr(self, f"_{op.lower()}", None)
            if handler is None:
                return {"result_status": "BACKEND_ERROR",
                        "error": f"No backend handler for op: {op}"}
            return handler(payload or {})
        except (OSError, PermissionError) as exc:
            return {"result_status": "BACKEND_ERROR", "error": str(exc)}

    def _resolve(self, relative: str) -> Path:
        """A path beneath the declared root, or a refusal.

        An artifact path arrives from a rendered design, and a design that named `../` would write
        outside the root the binding declared. Containment is checked rather than assumed.
        """
        target = (self._root / relative).resolve()
        if not str(target).startswith(str(self._root.resolve())):
            raise ValueError(f"path escapes the declared root: {relative}")
        return target

    def _write_all(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Persist every rendered document in one operation.

        A capability contract is a fixed pipeline with no iteration, so persisting twenty-five
        artifacts one call at a time is not expressible. The whole set is written together, which
        also makes it atomic in the sense that matters: either the construction was persisted or it
        was not.
        """
        documents = payload.get("documents")
        if not isinstance(documents, list) or not documents:
            return {"result_status": "VIOLATION",
                    "error": "documents must be a non-empty array of {path, text}"}

        written = []
        for document in documents:
            path = document.get("path")
            text = document.get("text")
            if not path or not isinstance(text, str):
                return {"result_status": "VIOLATION",
                        "error": f"document is not {{path, text}}: {document!r}"}
            target = self._resolve(path)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            written.append(str(target))

        return {"result_status": "SUCCESS", "written": len(written), "paths": sorted(written)}

    def _list(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self._root.exists():
            return {"result_status": "NOT_FOUND", "paths": []}
        return {"result_status": "SUCCESS",
                "paths": sorted(str(p) for p in self._root.rglob("*.md"))}
