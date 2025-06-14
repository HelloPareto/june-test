import re
from email import policy
from email.parser import BytesParser
from pathlib import Path


def find_emails(base_dir: str):
    subdirs = ["cur", "new", "tmp"]
    emails = []
    for subdir in subdirs:
        full_path = Path(base_dir) / subdir
        if full_path.exists():
            for email_file in full_path.iterdir():
                if email_file.is_file():
                    emails.append(email_file)
    return emails


def load_email(email_path: Path):
    with open(email_path, "rb") as f:
        message = BytesParser(policy=policy.default).parse(f)  # pyright: ignore
    return message


def match_regex_or_exact(text: str, pattern: str) -> bool:
    if not text or not pattern:
        return False
    try:
        return re.search(pattern, text, re.IGNORECASE) is not None
    except re.error:
        # Fallback to exact match if regex is invalid
        return pattern.lower() in text.lower()


def validate_subject(msg, pattern: str) -> bool:
    return match_regex_or_exact(msg.get("subject", ""), pattern)


def validate_recipient(msg, pattern: str) -> bool:
    return match_regex_or_exact(msg.get("to", ""), pattern)


def validate_body(msg, pattern: str) -> bool:
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                if match_regex_or_exact(part.get_content(), pattern):
                    return True
    else:
        if match_regex_or_exact(msg.get_content(), pattern):
            return True
    return False


class Email:
    """Helper client to to verifications against local emails."""

    def __init__(
        self,
        home: str,
        email_dir: str,
    ):
        self.base_dir = str(Path(home, email_dir))

    def setup(self):
        pass

    @property
    def messages(self):
        email_files = find_emails(self.base_dir)
        return [load_email(email_file) for email_file in email_files]

    def check_email_with_details_exists(
        self,
        subject_pattern: str | None = None,
        recipient_pattern: str | None = None,
        body_pattern: str | None = None,
    ) -> bool:
        """Checks if there's an email matching the given patterns. All str args use patterns for matching, use
        ^$ for exact matchees.
        If a pattern is None, that check is skipped.
        """
        for msg in self.messages:
            if subject_pattern is not None:
                if not validate_subject(msg, subject_pattern):
                    continue

            if recipient_pattern is not None:
                if not validate_recipient(msg, recipient_pattern):
                    continue

            if body_pattern is not None:
                if not validate_body(msg, body_pattern):
                    continue

            return True

        return False
