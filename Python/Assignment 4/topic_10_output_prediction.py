"""Topic 10: Output prediction and execution flow (Q71-Q75)."""

# Q71: 85 meets the first condition, so the later elif is skipped.
print("Q71 prediction: Pass")

# Q72: The given ordering checks the highest threshold first.
print("Q72 predictions: 95 -> A, 85 -> B, 50 -> Pass, 30 -> Fail")

# Q73: The outer age condition is checked before has_id.
print("Q73 predictions: (20, True) -> Entry Allowed; (20, False) -> ID Required; (16, True) -> Underage")

# Q74: case _ catches any choice not matched by a numbered case.
print("Q74 predictions: 1 -> Add, 3 -> Delete, 5 -> Invalid Choice")

# Q75: Attendance is checked first; marks are classified only if attendance >= 75.
print("Q75 predictions: (82, 80) -> Grade B; (92, 80) -> Grade A; (55, 80) -> Pass; (92, 60) -> Not Eligible")
