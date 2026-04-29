def decide(toxic, spam, hate):
    print("[Coordinator] Aggregating results...")

    reasons = []

    if hate:
        reasons.append("Hate Speech")
    if toxic:
        reasons.append("Toxic Content")
    if spam:
        reasons.append("Spam")

    if reasons:
        return "Rejected (" + ", ".join(reasons) + ")"
    else:
        return "Approved"