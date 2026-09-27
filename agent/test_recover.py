from agent.recover import recover


def test_recover_contract_without_api_key(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    result = recover(
        {"outstanding_amount": 80000, "days_overdue": 10},
        {"summary": "Previous call"},
        [{"date": "2026-09-25", "summary": "Customer missed promised payment", "type": "experience"}],
        "What should I do?",
    )
    assert set(result) == {"summary", "action", "reason", "tone", "message", "memory_evidence"}
    assert result["memory_evidence"]
