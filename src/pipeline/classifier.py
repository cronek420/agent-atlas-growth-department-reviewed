from typing import Dict, Any

class ReplyClassifier:
    """
    Classifies incoming replies to determine if they are genuine human responses,
    auto-responders, bounces, or opt-outs.
    """

    @staticmethod
    def classify(reply_body: str, subject: str) -> str:
        """
        Return one of: 'HUMAN_REPLY', 'AUTO_RESPONDER', 'BOUNCE', 'OPT_OUT'
        """
        body_lower = reply_body.lower()
        subject_lower = subject.lower()

        if "out of office" in subject_lower or "out of office" in body_lower or "ooo" in subject_lower:
            return "AUTO_RESPONDER"
        
        if "unsubscribe" in body_lower or "remove me" in body_lower or "opt out" in body_lower:
            return "OPT_OUT"

        if "undeliverable" in subject_lower or "bounce" in subject_lower:
            return "BOUNCE"

        # If it doesn't match known automated patterns, treat it as a human reply to be surfaced.
        return "HUMAN_REPLY"
