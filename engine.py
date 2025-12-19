
def overlap(user, ref):
    if not user:
        return 0
    return len(set(user) & set(ref)) / len(set(user))

def compute_probability(user, ref, weights):
    score = 0
    max_score = 0

    for k,w in weights.items():
        if k in ["karar","merkez","agaz","alt","ust"]:
            if user.get(k) and ref.get(k):
                max_score += w
                if user[k] == ref[k]:
                    score += w

    max_score += weights["asil"]
    score += overlap(user.get("asil",[]), ref.get("asil",[])) * weights["asil"]

    max_score += weights["nim"]
    score += overlap(user.get("nim",[]), ref.get("nim",[])) * weights["nim"]

    return round((score/max_score)*100,1) if max_score else 0
